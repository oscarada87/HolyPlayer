import os
import inspect
import asyncio
from async_timeout import timeout

import discord
from discord.ext import commands


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

class PlayList(metaclass=SingletonArgs):
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """

    __slots__ = ('bot', '_guild', '_channel', '_cog', 'queue', 'next', 'current')

    def __init__(self, ctx):
        self.bot = ctx.bot
        self._guild = ctx.guild
        self._channel = ctx.channel
        self._cog = ctx.cog

        self.queue = asyncio.PriorityQueue(maxsize=30) # 最大歌單數目訂為30
        self.next = asyncio.Event()

        self.current = None

        ctx.bot.loop.create_task(self.player_loop())

    async def player_loop(self):
        """Our main player loop."""
        await self.bot.wait_until_ready()

        while not self.bot.is_closed():
            self.next.clear()

            try:
                # Wait for the next song. If we timeout cancel the player and disconnect...
                async with timeout(300):  # 5 minutes...
                    song = await self.queue.get()
            except asyncio.TimeoutError:
                return self.destroy(self._guild)
            song = song[1]
            self.current = song
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.file_locat))
            self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
            await self._channel.send('**:musical_note:現正播放：musical_note: **\n {} \n:ballot_box_with_check:requested by\n{}'.format(song.info['title'], song.info['request']))
            # source.volume = self.volume
            # print(self.next.is_set())
            await self.next.wait()
            # print(self.next.is_set())
            # print("finish waiting")

            # Make sure the FFmpeg process is cleaned up.
            source.cleanup()
            try:
                os.remove(song.file_locat)
            except OSError:
                print("File Not Found!")
            self.current = None

    def destroy(self, guild):
        """Disconnect and cleanup the player."""
        return self.bot.loop.create_task(self._cog.cleanup(guild))



# class PlayList():
#     def __init__(self, ctx):
#         self.bot = ctx.bot
#         self._guild = ctx.guild
#         self._channel = ctx.channel
#         self._cog = ctx.cog

#         self._current_playing = None
#         # self._play_list = []
#         # self._priority_list = []

#         # self.np = None
#         self.queue = asyncio.Queue()
#         self.next = asyncio.Event()
#         ctx.bot.loop.create_task(self.player_loop())

#     @property
#     def guild(self):
#         return self._guild

#     @property
#     def current_playing(self):
#         return self._current_playing

#     async def player_loop(self):
#         """Our main player loop."""
#         await self.bot.wait_until_ready()

#         while not self.bot.is_closed():
#             self.next.clear()
#             try:
#                 # Wait for the next song. If we timeout cancel the player and disconnect...
#                 async with timeout(300):  # 5 minutes...
#                     song = await self.queue.get()
#             except asyncio.TimeoutError:
#                 return self.destroy(self._guild)

#             # if not isinstance(song, YTDLSource):
#             #     # Source was probably a stream (not downloaded)
#             #     # So we should regather to prevent stream expiration
#             #     try:
#             #         source = await YTDLSource.regather_stream(song, loop=self.bot.loop)
#             #     except Exception as e:
#             #         await self._channel.send(f'There was an error processing your song.\n'
#             #                                  f'```css\n[{e}]\n```')
#             #         continue

#             # source.volume = self.volume
#             self._current_playing = song
#             source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.file_locat))
#             self._guild.voice_client.play(source, after=lambda _: self.bot.loop.call_soon_threadsafe(self.next.set))
#             await self._channel.send('**Now Playing:**\n {} \nrequested by {}'.format(song.info['title'], song.info['request']))
#             print("add to queue")
#             print(self.next.is_set())
#             await self.next.wait()
#             print(self.next.is_set())
#             print("finish waiting")

#             # Make sure the FFmpeg process is cleaned up.
#             source.cleanup()
#             self._current_playing = None
#             # try:
#             #     # We are no longer playing this song...
#             #     await self.np.delete()
#             # except discord.HTTPException:
#             #     pass

#     def destroy(self, guild):
#         """Disconnect and cleanup the player."""
#         return self.bot.loop.create_task(self._cog.cleanup(guild))

