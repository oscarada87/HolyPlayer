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
        if init is not None:
            # print(inspect.getcallargs(init, None, *args, **kwargs)['ctx'])
            key = (cls, inspect.getcallargs(init, None, *args, **kwargs)['ctx'].guild.id)
        else:
            key = cls
        
        if key not in cls._instances:
            cls._instances[key] = super(SingletonArgs, cls).__call__(*args, **kwargs)

        return cls._instances[key]


class Player(metaclass=SingletonArgs):
    """A class which is assigned to each guild using the bot for Music.
    This class implements a queue and loop, which allows for different guilds to listen to different playlists
    simultaneously.
    When the bot disconnects from the Voice it's instance will be destroyed.
    """
    _instances = {}

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
