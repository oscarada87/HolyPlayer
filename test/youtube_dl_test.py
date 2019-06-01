from unittest import TestCase
import youtube_dl
import pytest
import os

# 暫時跳過
@pytest.mark.skipif()
class TestYoutubeDl(TestCase):
    # 執行每個函數前會先執行這個
    def setUp(self):
        self.ytdl_options = {
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
        self.ytdl = youtube_dl.YoutubeDL(self.ytdl_options)
        self.song_url = "https://www.youtube.com/watch?v=L3oDm5ff1to&ab_channel=SmashRegz"
        self.song_list_url = "https://www.youtube.com/playlist?list=PLRR3Za6-4AAL_VvOXL-eqPIWnFfB8QmD8"

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_youtube_song_info(self):
        data = self.ytdl.extract_info(self.song_url, download=False)
        self.assertEqual("Trout Fresh/呂士軒 - 通勤打理 (Official Music Video)", data.get('title'))
        self.assertTrue(data.get('url'))
        self.assertEqual("L3oDm5ff1to", data.get('id'))
        # youtube 連結跟 youtube_dl 載的連結不太一樣，因為 youtube 影片的連結好像不是唯一，所以沒法測試
        self.assertEqual(234, data.get('duration'))
        self.assertEqual("SmashRegz", data.get('uploader'))
        self.assertTrue(data.get('thumbnail'))
        self.assertFalse(data.get('_type'))


    def test_youtube_song_list_info(self):
        data = self.ytdl.extract_info(self.song_list_url, download=False)
        self.assertEqual("TEST", data.get('title'))
        self.assertEqual("俊廷江", data.get('uploader'))
        # self.assertTrue(data.get('url'))
        # youtube 連結跟 youtube_dl 載的連結不太一樣，因為 youtube 影片的連結好像不是唯一，所以沒法測試
        self.assertEqual("Snail's House  - Grape Soda [Tasty Release]", data['entries'][0].get('title'))
        self.assertEqual("TheFatRat - Never Be Alone [Tasty Release]", data['entries'][1].get('title'))
        self.assertEqual(194, data['entries'][0].get('duration'))
        self.assertEqual(260, data['entries'][1].get('duration'))
        self.assertEqual("Tasty", data['entries'][1].get('uploader'))
        self.assertEqual("Tasty", data['entries'][1].get('uploader'))
        self.assertEqual('playlist', data.get('_type'))
    
    def test_youtube_search(self):
        data = self.ytdl.extract_info("你我可以", download=False)
        self.assertTrue(data['entries'][0].get('title'))
        self.assertEqual('playlist', data.get('_type'))