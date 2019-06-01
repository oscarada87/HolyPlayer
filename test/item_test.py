from unittest import TestCase
import pytest
from src.item import Item, Song, SongList 

class TestSong(TestCase):
    def setUp(self):
        self.song_info = {
            'id': '7M6nsbieMks',
            'url': 'https://www.youtube.com/watch?v=7M6nsbieMks',
            'title': 'Trout Fresh/呂士軒 - 愛吃味 (Official Music Video)',
            'duration': 257,
            'uploader': 'SmashRegz',
            'request': 'Oscar',
            'file_locat': '/downloads/7M6nsbieMks.mp3'
        }

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_Song(self):
        song = Song(self.song_info)
        self.assertEqual(self.song_info['id'], song.info['id'])
        self.assertEqual(self.song_info['url'], song.info['url'])
        self.assertEqual(self.song_info['title'], song.info['title'])
        self.assertEqual(self.song_info['duration'], song.info['duration'])
        self.assertEqual(self.song_info['uploader'], song.info['uploader'])
        self.assertEqual(self.song_info['request'], song.info['request'])
        self.assertEqual(self.song_info['file_locat'], song.file_locat)
        self.assertTrue(self.song_info['id'], song)
        with self.assertRaises(TypeError) as context:
            song.add_song()
        self.assertEqual('Song type can\'t add another Song!', str(context.exception))
        it = iter(song)
        self.assertEqual(self.song_info['id'], next(it).info['id'])

class TestSongList(TestCase):
    def setUp(self):
        self.song1_info = {
            'id': '7M6nsbieMks',
            'url': 'https://www.youtube.com/watch?v=7M6nsbieMks',
            'title': 'Trout Fresh/呂士軒 - 愛吃味 (Official Music Video)',
            'duration': 257,
            'uploader': 'SmashRegz',
            'request': 'Oscar',
            'file_locat': '/downloads/7M6nsbieMks.mp3'
        }
        self.song2_info = {
            'id': 'VUTGGdx4KJM',
            'url': 'https://www.youtube.com/watch?v=VUTGGdx4KJM',
            'title': 'Trout Fresh / 呂士軒『誤入奇途』 - 03 狐群狗黨',
            'duration': 294,
            'uploader': 'SmashRegz',
            'request': 'Oscar',
            'file_locat': '/downloads/VUTGGdx4KJM.mp3'
        }
        self.song3_info = {
            'id': '08Ca5FAxThg',
            'url': 'https://www.youtube.com/watch?v=08Ca5FAxThg',
            'title': '熊仔 Presents BOWZ RETRO WORLD -【假朋友真兄弟 FFRH】Official Music Video',
            'duration': 291,
            'uploader': '熊仔',
            'request': 'Oscar',
            'file_locat': '/downloads/08Ca5FAxThg.mp3'
        }
        self.song_list_info = {
            'title': '饒舌',
            'uploader': 'Oscar'
        }

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_Song(self):
        song_list = SongList(self.song_list_info)
        song_list.add_song(Song(self.song1_info))
        song_list.add_song(Song(self.song2_info))
        self.assertEqual(551, song_list.info['duration'])
        self.assertEqual(self.song_list_info['title'], song_list.info['title'])
        self.assertEqual(self.song_list_info['uploader'], song_list.info['uploader'])
        song_list.add_song(Song(self.song3_info))
        self.assertEqual(842, song_list.info['duration'])
        it = iter(song_list)
        self.assertEqual(self.song1_info['id'], next(it).info['id'])
        self.assertEqual(self.song2_info['id'], next(it).info['id'])
        self.assertEqual(self.song3_info['id'], next(it).info['id'])
        song_list.remove_song_by_id(self.song2_info['id'])
        self.assertEqual(548, song_list.info['duration'])
