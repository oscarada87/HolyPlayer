from unittest import TestCase
import pytest
from src.builder import Builder

# 暫時跳過
# @pytest.mark.skipif()
class TestBuilder(TestCase):
    def setUp(self):
        self.song_url = "https://www.youtube.com/watch?v=7M6nsbieMks&ab_channel=SmashRegz"
        self.song_list_url = "https://www.youtube.com/playlist?list=PLRR3Za6-4AAL_VvOXL-eqPIWnFfB8QmD8"
        self.keyword = "愛吃味"
        self.user = "Oscar"

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_song_builder(self):
        builder = Builder(self.song_url, self.user)
        song = builder.get_item()
        self.assertEqual('7M6nsbieMks', song.info['id'])
        self.assertEqual('https://www.youtube.com/watch?v=7M6nsbieMks', song.info['url'])
        self.assertEqual('Trout Fresh/呂士軒 - 愛吃味 (Official Music Video)', song.info['title'])
        self.assertEqual(258, song.info['duration'])
        self.assertEqual('SmashRegz', song.info['uploader'])
        self.assertEqual(self.user, song.info['request'])
        self.assertEqual('./downloads/7M6nsbieMks.mp3', song.file_locat)

    def test_keyword_builder(self):
        builder = Builder(self.keyword, self.user)
        song = builder.get_item()
        self.assertEqual('7M6nsbieMks', song.info['id'])
        self.assertEqual('https://www.youtube.com/watch?v=7M6nsbieMks', song.info['url'])
        self.assertEqual('Trout Fresh/呂士軒 - 愛吃味 (Official Music Video)', song.info['title'])
        self.assertEqual(258, song.info['duration'])
        self.assertEqual('SmashRegz', song.info['uploader'])
        self.assertEqual(self.user, song.info['request'])
        self.assertEqual('./downloads/7M6nsbieMks.mp3', song.file_locat)
    
    def test_song_list_builder(self):
        builder = Builder(self.song_list_url, self.user)
        song_list = builder.get_item()
        self.assertEqual('TEST', song_list.info['title'])
        self.assertEqual(454, song_list.info['duration'])
        self.assertEqual('俊廷江', song_list.info['uploader'])
        it = iter(song_list)
        song = next(it)
        self.assertEqual("Snail's House  - Grape Soda [Tasty Release]", song.info['title'])
        self.assertEqual(194, song.info['duration'])
        self.assertEqual("Tasty", song.info['uploader'])
        self.assertEqual("TEST", song.info['playlist'])
        song = next(it)
        self.assertEqual("TheFatRat - Never Be Alone [Tasty Release]", song.info['title'])       
        self.assertEqual(260, song.info['duration'])       
        self.assertEqual("Tasty", song.info['uploader'])
        self.assertEqual("TEST", song.info['playlist'])
