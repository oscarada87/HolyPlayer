import youtube_dl

class Builder():
    def __init__(self, keyword, user):
        self.__ytdl_options = {
            'format': 'bestaudio/best',             #下載格式，這邊設定是音訊檔
            'outtmpl': 'downloads/%(id)s.mp3',  #下載檔名和位置
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
        self.__ytdl = youtube_dl.YoutubeDL(self.ytdl_options)
        self.__song_info = {
            'id': None,
            'url': None,
            'title': None,
            'duration': None,
            'uploader': None,
            'request': user,
            'file_locat': None
        }
        self.__song_list_info = {
            'title': None,
            'uploader': None
        }
        self.__keyword = keyword
    
    def extract_info():
        YOUTUBE_WEBSITE = "https://www.youtube.com/watch?v="
        data = self.__ytdl.extract_info(self.__keyword, download=False)
        # url 為一首歌曲
        if data.get('_type') is None or data.get('_type') == 'video':
            self.__song_info['id'] = data.get('id')
            self.__song_info['url'] = YOUTUBE_WEBSITE + data.get('id')
            self.__song_info['title'] = data.get('title')
            self.__song_info['duration'] = int(data.get('duration'))
            self.__song_info['uploader'] = data.get('uploader')
            self.__song_info['file_locat'] = '..\\downloads\\' + data.get('title')
        # url 為歌單
        else if 'youtu' in self.__keyword and data.get('_type') == 'playlist':
            self.__song_list_info['title'] = data.get('title')
            self.__song_list_info['uploader'] = data.get('uploader')
            
