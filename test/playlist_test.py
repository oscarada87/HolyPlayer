from unittest import TestCase
import pytest
from src.playlist import PlayList
from src.builder import Builder

class TestPlayList(TestCase):
    # 執行每個函數前會先執行這個
    def setUp(self):
        self.server1 = {
            'server_id': 123,
            'server_name': 'Server1'
        }
        self.server2 = {
            'server_id': 456,
            'server_name': 'Server2'
        }

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_play_list(self):
        playList1 = PlayList(self.server1['server_id'], self.server1['server_name'])
        playList2 = PlayList(self.server2['server_id'], self.server2['server_name'])
        self.assertEqual('Server1', playList1.server_name)
        self.assertEqual('Server2', playList2.server_name)
        playList1.add(Builder("https://www.youtube.com/watch?v=7M6nsbieMks&ab_channel=SmashRegz", "Oscar").get_item())
        playList1.add(Builder("你我可以", "Eric").get_item())
        it = iter(playList1)
        song = next(it)
        self.assertEqual('7M6nsbieMks', song.info['id'])
        song = next(it)
        self.assertEqual('B6J-URwBIRU', song.info['id'])