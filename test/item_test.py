from unittest import TestCase
from src.item import Item, Song, SongList


class SongTest(TestCase):
    """測試 Song"""

    def setUp(self):
        """測試前先建立好環境"""
        self.song_info = {
            'id': '7M6nsbieMks',
            'url': 'https://www.youtube.com/watch?v=7M6nsbieMks',
            'title': 'Trout Fresh/呂士軒 - 愛吃味 (Official Music Video)',
            'duration': 257,
            'uploader': 'SmashRegz',
            'request': 'Oscar',
            'file_locat': '/downloads/7M6nsbieMks.mp3',
            'playlist': None,
        }
        self.song = Song(self.song_info)

    def tearDown(self):
        """測試結束後收拾環境"""
        pass

    def test_song(self):
        """測試 Song 各個屬性和方法"""
        self.assertEqual(self.song_info['id'], self.song.info['id'])
        self.assertEqual(self.song_info['url'], self.song.info['url'])
        self.assertEqual(self.song_info['title'], self.song.info['title'])
        self.assertEqual(self.song_info['duration'], self.song.info['duration'])
        self.assertEqual(self.song_info['uploader'], self.song.info['uploader'])
        self.assertEqual(self.song_info['request'], self.song.info['request'])
        self.assertEqual(self.song_info['file_locat'], self.song.file_locat)

        with self.assertRaises(TypeError) as context:
            self.song.add_song()
        self.assertEqual('Song type can\'t add another Song!',
                         str(context.exception))

        it = iter(self.song)
        self.assertEqual(self.song_info['id'], next(it).info['id'])


class SongListTest(TestCase):
    """測試 SongList"""

    def setUp(self):
        """測試前先建立好環境"""
        self.song1_info = {
            'id': '7M6nsbieMks',
            'url': 'https://www.youtube.com/watch?v=7M6nsbieMks',
            'title': 'Trout Fresh/呂士軒 - 愛吃味 (Official Music Video)',
            'duration': 257,
            'uploader': 'SmashRegz',
            'request': 'Oscar',
            'file_locat': '/downloads/7M6nsbieMks.mp3',
            'playlist': '饒舌'
        }
        self.song1 = Song(self.song1_info)

        self.song2_info = {
            'id': 'VUTGGdx4KJM',
            'url': 'https://www.youtube.com/watch?v=VUTGGdx4KJM',
            'title': 'Trout Fresh / 呂士軒『誤入奇途』 - 03 狐群狗黨',
            'duration': 294,
            'uploader': 'SmashRegz',
            'request': 'Oscar',
            'file_locat': '/downloads/VUTGGdx4KJM.mp3',
            'playlist': '饒舌'
        }
        self.song2 = Song(self.song2_info)

        self.song3_info = {
            'id': '08Ca5FAxThg',
            'url': 'https://www.youtube.com/watch?v=08Ca5FAxThg',
            'title': '熊仔 Presents BOWZ RETRO WORLD -【假朋友真兄弟 FFRH】Official Music Video',
            'duration': 291,
            'uploader': '熊仔',
            'request': 'Oscar',
            'file_locat': '/downloads/08Ca5FAxThg.mp3',
            'playlist': '饒舌'
        }
        self.song3 = Song(self.song3_info)

        self.song_list_info = {
            'title': '饒舌',
            'uploader': 'Oscar'
        }
        self.song_list = SongList(self.song_list_info)

    def tearDown(self):
        """測試結束後收拾環境"""
        pass

    def test_song_list(self):
        """測試 Song 各個屬性和方法"""
        self.song_list.add_song(self.song1)
        self.song_list.add_song(self.song2)

        self.assertEqual(551, self.song_list.info['duration'])
        self.assertEqual(
            self.song_list_info['title'], self.song_list.info['title'])
        self.assertEqual(
            self.song_list_info['uploader'], self.song_list.info['uploader'])

        self.song_list.add_song(self.song3)

        self.assertEqual(842, self.song_list.info['duration'])

        it = iter(self.song_list)
        self.assertEqual(self.song1_info['id'], next(it).info['id'])
        self.assertEqual(self.song2_info['id'], next(it).info['id'])
        self.assertEqual(self.song3_info['id'], next(it).info['id'])

        self.song_list.remove_song_by_id(self.song2.info['id'])
        self.assertEqual(548, self.song_list.info['duration'])
