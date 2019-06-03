from abc import ABCMeta, abstractmethod

class Item(object, metaclass=ABCMeta):
    def __init__(self, info):
        self._info = {}
        self._info['title'] = info['title']
        self._info['uploader'] = info['uploader']

    @abstractmethod
    def add_song(self):
        pass

    @property
    def info(self):
        return self._info


class Song(Item):
    def __init__(self, info):
        super(Song, self).__init__(info)
        # song 的唯一值為 id
        self._info['id'] = info['id']
        self._info['url'] = info['url']
        self._info['duration'] = info['duration']
        self._info['request'] = info['request']
        self._file_locat = info['file_locat']
    
    @property
    def file_locat(self):
        return self._file_locat

    # overload == operator for song ,compare with id
    def __eq__(self, other):
        if self._info['id'] == other:
            return True
        else:
            return False

    # overload < operator for song ,using in proirity queue
    def __lt__(self, other):
        return False

    def add_song(self):
        raise TypeError('Song type can\'t add another Song!')

    # iterator
    def __iter__(self):
        yield self
    
class SongList(Item):
    def __init__(self, info):
        super(SongList, self).__init__(info)
        self._info['duration'] = 0
        self._song_list = []

    def add_song(self, song):
        self._song_list.append(song)
        self._update_duration()

    def remove_song_by_id(self, id):
        self._song_list.remove(id)
        self._update_duration()

    def _update_duration(self):
        total = 0
        for song in self._song_list:
            total += song.info['duration']
        self._info['duration'] = total

    # iterator
    def __iter__(self):
        for song in self._song_list:
            yield song