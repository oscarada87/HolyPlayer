import pytest
from unittest import TestCase
from src.playlist import PlayList
from src.builder import Builder


# 暫時跳過此測試
@pytest.mark.skipif()
class PlayListTest(TestCase):
    """測試 PlayList"""

    def setUp(self):
        """測試前先建立好環境"""
        self.server1 = {
            'server_id': 123,
            'server_name': 'Server1'
        }
        self.play_list1 = PlayList(
            self.server1['server_id'], self.server1['server_name'])

        self.server2 = {
            'server_id': 456,
            'server_name': 'Server2'
        }
        self.play_list2 = PlayList(
            self.server2['server_id'], self.server2['server_name'])

    def tearDown(self):
        """測試結束後收拾環境"""
        pass

    def test_play_list(self):
        self.assertEqual(
            self.play_list1['server_name'], self.play_list1.server_name)
        self.assertEqual(
            self.play_list2['server_name'], self.play_list2.server_name)

        self.play_list1.add(Builder(
            'https://www.youtube.com/watch?v=7M6nsbieMks&ab_channel=SmashRegz', 'Oscar').get_item())
        self.play_list1.add(Builder('你我可以', 'Eric').get_item())

        it = iter(self.play_list1)
        self.assertEqual('7M6nsbieMks', next(it).info['id'])
        self.assertEqual('B6J-URwBIRU', next(it).info['id'])
