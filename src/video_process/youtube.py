import youtube_dl
import urllib.parse
from pprint import pprint

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}


# url = 'https://www.youtube.com/watch?v=BaW_jenozKc'
# url = 'https://www.youtube.com/watch?v=ks2hGA1yV3Q&list=PLRR3Za6-4AAL_VvOXL-eqPIWnFfB8QmD8&index=2&t=0s'
keyword = urllib.parse.quote(input("請輸入關鍵字: \n"))
url = "https://www.youtube.com/results?search_query={}&page=1".format(keyword)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    data = ydl.extract_info(url, download=False)
    pprint(data)
    for song in data['entries']:
        pass
        # pprint(song.get('title'))
    # pprint(len(data['entries']))