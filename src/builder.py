import youtube_dl
import urllib.parse
from src.item import Song, SongList
from pprint import pprint
import uuid

class Builder():
    def __init__(self, keyword, user):
        self._ytdl_options = {
            'format': 'bestaudio/best',             #下載格式，這邊設定是音訊檔
            'outtmpl': 'downloads/%(id)s.mp3',      #下載檔名和位置
            'extractaudio': True,                   #只留音訊檔
            'audioformat': "mp3",                   #指定mp3格式
            'restrictfilenames': True,              #檔名是否可以出現'&'和空白
            'noplaylist': False,                    #接不接受歌單
            'nocheckcertificate': True,             #要不要驗證SSL
            'ignoreerrors': False,                  #當出現錯誤時是否繼續
            'logtostderr': False,                   #Log messages to stderr instead of stdout
            'quiet': True,                          #不要輸出訊息在 stdout
            'no_warnings': True,                    #不要輸出警告
            'default_search': 'auto',               #當輸入的 url 不符合時，是否搜尋
            'source_address': '0.0.0.0'             # bind to ipv4 since ipv6 addresses cause issues sometimes
        }
        self._ytdl = youtube_dl.YoutubeDL(self._ytdl_options)
        self._song_info = {
            'id': None,
            'url': None,
            'title': None,
            'duration': None,
            'uploader': None,
            'request': user,
            'file_locat': None,
            'playlist': None
        }
        self._song_list_info = {
            'title': None,
            'uploader': None
        }
        self._keyword = keyword
    
    def get_item(self):
        extra_name = '_' + str(uuid.uuid1())[0:4]
        self._ytdl_options['outtmpl'] = 'downloads/%(id)s' + extra_name + '.mp3'
        self._ytdl = youtube_dl.YoutubeDL(self._ytdl_options)


        data = self._ytdl.extract_info(self._keyword, download=True)
        # keyword 為一首歌曲
        if data.get('_type') is None or data.get('_type') == 'video':
            self._song_info['id'] = data.get('id')
            self._song_info['url'] = data.get('webpage_url')
            self._song_info['title'] = data.get('title')
            self._song_info['duration'] = int(data.get('duration'))
            self._song_info['uploader'] = data.get('uploader')
            # self._song_info['file_locat'] = './downloads/' + data.get('id') + '.mp3'
            self._song_info['file_locat'] = './downloads/' + data.get('id') + extra_name + '.mp3'
            return Song(self._song_info)
        # keyword 為歌單
        elif 'youtu' in self._keyword and data.get('_type') == 'playlist':
            self._song_list_info['title'] = data.get('title')
            self._song_list_info['uploader'] = data.get('uploader')
            self._song_info['playlist'] = data.get('title')
            song_list = SongList(self._song_list_info)
            for song in data['entries']:
                self._ytdl.extract_info(song.get('webpage_url'), download=True)
                self._song_info['id'] = song.get('id')
                self._song_info['url'] = song.get('webpage_url')
                self._song_info['title'] = song.get('title')
                self._song_info['duration'] = int(song.get('duration'))
                self._song_info['uploader'] = song.get('uploader')
                # self._song_info['file_locat'] = './downloads/' + song.get('id') + '.mp3'
                self._song_info['file_locat'] = './downloads/' + song.get('id') + extra_name + '.mp3'
                song_list.add_song(Song(self._song_info))
            return song_list
        # keyword 為關鍵字
        elif data.get('_type') == 'playlist':
            self._song_info['id'] = data['entries'][0].get('id')
            self._song_info['url'] = data['entries'][0].get('webpage_url')
            self._song_info['title'] = data['entries'][0].get('title')
            self._song_info['duration'] = int(data['entries'][0].get('duration'))
            self._song_info['uploader'] = data['entries'][0].get('uploader')
            # self._song_info['file_locat'] = './downloads/' + data['entries'][0].get('id') + '.mp3'
            self._song_info['file_locat'] = './downloads/' + data['entries'][0].get('id') + extra_name + '.mp3'
            return Song(self._song_info)
        
        else:
            raise ValueError("Extract information failed!")
