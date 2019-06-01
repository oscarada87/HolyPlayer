# class Singleton(type):
#     def __init__(cls,name,bases,dic):
#         super(Singleton,cls).__init__(name,bases,dic)
#         cls.instance=None
#     def __call__(cls,*args,**kw):
#         if cls.instance is None:
#             cls.instance=super(Singleton,cls).__call__(*args,**kw)
#         return cls.instance
import inspect

class SingletonArgs(type):
    _instances = {}
    _init = {}
    # dct 是 傳進來參數的字典
    def __init__(cls, name, bases, dct):
        cls._init[cls] = dct.get('__init__', None)

    def __call__(cls, *args, **kwargs):
        init = cls._init[cls]
        # print(init)
        # frozenset 會回傳一個不可再更動的集合
        # inspect 是用來看 python 源碼和類型檢查的 module
        # getcallargs 將args和kwargs参数到绑定到为func的参数名；返回字典，對應参数名及其值
        if init is not None:
            key = (cls, frozenset(inspect.getcallargs(init, None, *args, **kwargs).items()))
        else:
            key = cls

        if key not in cls._instances:
            cls._instances[key] = super(SingletonArgs, cls).__call__(*args, **kwargs)
        return cls._instances[key]
# class PlayList():
#     __instances = {}
#     def __init__():

#     def __new__(cls, server_id):
#         if server_id in cls.__instances:
#             return cls.__instances[server_id]
#         elif:
#             cls.__instances[server_id] = super(PlayList, cls).__new__(cls, server_id)
        
class PlayList(metaclass=SingletonArgs):
    def __init__(self, server_id, server_name):
        self._server_id = server_id
        self._server_name = server_name
        self._current_playing = None
        self._play_list = []
        self._priority_list = []

    @property
    def server_id(self):
        return self._server_id
    
    @property
    def server_name(self):
        return self._server_name
    
    @property
    def current_playing(self):
        return self._current_playing

    def add(self, item):
        for song in item:
            self._play_list.append(song)
    
    def remove(self, num):
        if not isinstance(num, int):
            raise TypeError("Remove song need to enter integer!")
        count = 1
        for song in self._priority_list:
            if count == num:
                self._priority_list.remove(song)
                return
            else:
                count += 1
        for song in self._play_list:
            if count == num:
                self._play_list.remove(song)
                return
            else:
                count += 1
        raise ValueError("Index out of playlist length!")

    def next_download(self):
        if len(self._priority_list) > 0:
            self._current_playing = self._priority_list[0]
            self._priority_list.pop(0)
            return self._current_playing
        elif len(self._play_list) > 0:
            self._current_playing = self._play_list[0]
            self._play_list.pop(0)
            return self._current_playing
        else:
            return None

    # iterator
    def __iter__(self):
        for song in self._priority_list:
            yield song
        for song in self._play_list:
            yield song
