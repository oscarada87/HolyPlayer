import urllib.parse
from youtube_dl import YoutubeDL

ytdl_options = {
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
ytdl = YoutubeDL(ytdl_options)

def get_search2(keyword):
    result = []
    text = urllib.parse.quote(keyword)
    YOUTUBE_SEARCH = "https://www.youtube.com/results?search_query={}&page=1".format(text)
    data = ytdl.extract_info(YOUTUBE_SEARCH, download=False)
    for song in data['entries']:
        # print(song.get('title'))
        songinfo = {}
        songinfo['url'] = song.get('webpage_url')
        songinfo['title'] = song.get('title')
        songinfo['duration'] = song.get('duration')
        result.append(songinfo)
    return result