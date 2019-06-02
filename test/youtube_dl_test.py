from unittest import TestCase
from youtube_dl import YoutubeDL


class YoutubeDlTest(TestCase):
    """測試 youtube_dl"""

    def setUp(self):
        """測試前先建立好環境"""
        options = {
            'format': 'bestaudio/best',         # 下載的格式（這裡是設定音訊檔）
            'outtmpl': 'test/data/%(title)s',   # 下載的位置和檔名
            'restrictfilenames': True,          # 檔名是否接受「&」和空白
            'noplaylist': False,                # 是否接受歌單
            'nocheckcertificate': True,         # 是否驗證 SSL 憑證
            'ignoreerrors': False,              # 出現錯誤時是否繼續
            'logtostderr': False,               # 是否把 log 輸出到 stderr
            'quiet': True,                      # 安靜模式
            'no_warnings': True,                # 是否不要輸出警告
            'default_search': 'auto',           # 當輸入的不是 URL 時是否改為搜尋
        }

        # 建立 YoutubeDL 實例
        self.youtube_dl = YoutubeDL(options)

    def tearDown(self):
        """測試結束後收拾環境"""
        pass

    def test_youtube_song(self):
        """測試取得 YouTube 歌曲資訊"""
        url = 'https://www.youtube.com/watch?v=L3oDm5ff1to'

        info = self.youtube_dl.extract_info(url, download=False)

        # 歌曲標題
        self.assertEqual(
            'Trout Fresh/呂士軒 - 通勤打理 (Official Music Video)', info.get('title'))
        # 歌曲上傳者
        self.assertEqual("SmashRegz", info.get('uploader'))
        # 歌曲長度（秒）
        self.assertEqual(234, info.get('duration'))
        # 歌曲連結
        self.assertTrue(info.get('url'))
        # 歌曲預覽圖
        self.assertTrue(info.get('thumbnail'))

    def test_youtube_list(self):
        """測試取得 YouTube 歌單資訊"""
        url = 'https://www.youtube.com/playlist?list=PLRR3Za6-4AAL_VvOXL-eqPIWnFfB8QmD8'

        info = self.youtube_dl.extract_info(url, download=False)

        # 歌單標題
        self.assertEqual('TEST', info.get('title'))
        # 歌單內含歌曲數量
        self.assertEqual(2, len(info['entries']))

        song1_info = info['entries'][0]

        # 歌曲一標題
        self.assertEqual(
            'Snail\'s House  - Grape Soda [Tasty Release]', song1_info.get('title'))
        # 歌曲一上傳者
        self.assertEqual('Tasty', song1_info.get('uploader'))
        # 歌曲一長度（秒）
        self.assertEqual(194, song1_info.get('duration'))
        # 歌曲一連結
        self.assertTrue(song1_info.get('url'))
        # 歌曲一預覽圖
        self.assertTrue(song1_info.get('thumbnail'))

        song2_info = info['entries'][1]

        # 歌曲二標題
        self.assertEqual(
            'TheFatRat - Never Be Alone [Tasty Release]', song2_info.get('title'))
        # 歌曲二上傳者
        self.assertEqual('Tasty', song2_info.get('uploader'))
        # 歌曲二長度（秒）
        self.assertEqual(260, song2_info.get('duration'))
        # 歌曲二連結
        self.assertTrue(song2_info.get('url'))
        # 歌曲二預覽圖
        self.assertTrue(song2_info.get('thumbnail'))