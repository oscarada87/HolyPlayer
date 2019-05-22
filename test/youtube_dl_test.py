from unittest import TestCase
import youtube_dl

class TestYoutubeDl(TestCase):
    # 執行每個函數前會先執行這個
    def setUp(self):
        self.ytdl_options = {
            'format': 'bestaudio/best',        #下載格式，這邊設定是音訊檔
            'outtmpl': 'test\\data\\%(title)s',  #下載檔名和位置
            'restrictfilenames': True,         #檔名是否可以出現'&'和空白
            'noplaylist': False,               #接不接受歌單
            'nocheckcertificate': True,        #要不要驗證SSL
            'ignoreerrors': False,             #當出現錯誤時是否繼續
            'logtostderr': False,              #Log messages to stderr instead of stdout
            'quiet': True,                     #不要輸出訊息在 stdout
            'no_warnings': True,               #不要輸出警告
            'default_search': 'auto',          #當輸入的 url 不符合時，是否搜尋
            'source_address': '0.0.0.0'        # bind to ipv4 since ipv6 addresses cause issues sometimes
        }
        self.ytdl = youtube_dl.YoutubeDL(self.ytdl_options)
        self.song_url = "https://www.youtube.com/watch?v=L3oDm5ff1to&ab_channel=SmashRegz"
        self.song_list_url = "https://www.youtube.com/playlist?list=PLRR3Za6-4AAL_VvOXL-eqPIWnFfB8QmD8"

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_youtube_info(self):
        data = self.ytdl.extract_info(self.song_url, download=False)
        self.assertEqual("Trout Fresh/呂士軒 - 通勤打理 (Official Music Video)", data.get('title'))
        # self.assertEqual("https://www.youtube.com/watch?v=L3oDm5ff1to&ab_channel=SmashRegz", data.get('url'))
        # youtube 連結跟 youtube_dl 載的連結不太一樣，因為 youtube 影片的連結好像不是唯一，所以沒法測試
        self.assertEqual(234, data.get('duration'))
        self.assertEqual("SmashRegz", data.get('uploader'))