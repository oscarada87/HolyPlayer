import asyncio
import discord
from pprint import pprint
from discord.ext import commands
import itertools
from random import shuffle

from .builder import Builder
from .player import Player
import urllib.parse
from youtube_dl import YoutubeDL

from .search import get_search2

class Music(commands.Cog):
    """Music related commands."""

    __slots__ = ('bot', 'players')

    def __init__(self, bot):
        self.bot = bot
        self._ytdl_options = {
            'format': 'bestaudio/best',             #下載格式，這邊設定是音訊檔
            'outtmpl': 'downloads/%(id)s.mp3',      #下載檔名和位置
            'extractaudio': True,                   #只留音訊檔
            'audioformat': "mp3",                   #指定mp3格式
            'restrictfilenames': True,              #檔名是否可以出現'&'和空白
            'noplaylist': False,                    #接不接受歌單
            'nocheckcertificate': True,             #要不要驗證SSL
            'ignoreerrors': False,                  #當出現錯誤時是否繼續
            'logtostderr': False,                   #Log messages to stderr instead of stdout
            'quiet': True,                          #不要輸出訊息在 stdout
            'no_warnings': True,                    #不要輸出警告
            'default_search': 'auto',               #當輸入的 url 不符合時，是否搜尋
            'source_address': '0.0.0.0'             # bind to ipv4 since ipv6 addresses cause issues sometimes
        }
        self._ytdl = YoutubeDL(self._ytdl_options)

    async def cleanup(self, guild):
        try:
            await guild.voice_client.disconnect()
        except AttributeError:
            pass
        Player.delete(guild)

    async def __local_check(self, ctx):
        """A local check which applies to all commands in this cog."""
        if not ctx.guild:
            raise commands.NoPrivateMessage('Please don\'t private message the bot!')
        return True

    def get_search(self, keyword):
        result = []
        text = urllib.parse.quote(keyword)
        YOUTUBE_SEARCH = "https://www.youtube.com/results?search_query={}&page=1".format(text)
        data = self._ytdl.extract_info(YOUTUBE_SEARCH, download=False)
        for song in data['entries']:
            # print(song.get('title'))
            songinfo = {}
            songinfo['url'] = song.get('webpage_url')
            songinfo['title'] = song.get('title')
            songinfo['duration'] = song.get('duration')
            result.append(songinfo)
        return result

    @commands.command(name='connect', aliases=['join'])
    async def connect_(self, ctx, *, channel: discord.VoiceChannel = None):
        # 若 author 的 voice 不為空（代表有在某個 channel 中）
        if ctx.author.voice:
            channel = ctx.author.voice.channel

            # 抓取 bot 當前的 voice_client
            vc = ctx.voice_client

            if vc is not None:
                # 若頻道相同則不做事
                if vc.channel.id == channel.id:
                    return

                try:
                    await vc.move_to(channel)
                except asyncio.TimeoutError:
                    raise commands.CommandError(
                        f'Moving to channel: <{channel}> timed out.')
            else:
                try:
                    await channel.connect()
                except asyncio.TimeoutError:
                    raise commands.CommandError(
                        f'Connecting to channel: <{channel}> timed out.')
        else:
            raise commands.CommandError(
                'No channel to join. Please either specify a valid channel or join one.')

        await ctx.send(f'Connected to: **{channel}**', delete_after=20)

    @commands.command(name='play', aliases=['sing'])
    async def play_(self, ctx, *, search: str):
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = Player(ctx)
        print(player)
        item = Builder(search, ctx.author).get_item()
        for song in iter(item):
            await player.queue.put((2, song))
            await ctx.send("成功加入歌曲：\n{}\n點歌者：\n{}".format(song.info['title'], song.info['request']))

    @commands.command(name='insert', aliases=['X', 'x', '插播', '插'])
    async def insert_(self, ctx, *, search: str):
        await ctx.trigger_typing()

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = Player(ctx)
        item = Builder(search, ctx.author).get_item()
        for song in iter(item):
            await player.queue.put((1, song))
            await ctx.send("成功插入歌曲:\n{}\n點歌者:\n{}".format(song.info['title'], song.info['request']))

    @commands.command(name='pause')
    async def pause_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            return await ctx.send('I am not currently playing anything!', delete_after=20)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f'**`{ctx.author}`**： 暫停了播放器！')

    @commands.command(name='resume')
    async def resume_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!', delete_after=20)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f'**`{ctx.author}`**： 恢復了播放器！')

    @commands.command(name='skip')
    async def skip_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!', delete_after=20)

        if vc.is_paused():
            pass
        elif not vc.is_playing():
            return

        vc.stop()
        await ctx.send(f'**`{ctx.author}`** 跳過了這首歌！')

    @commands.command(name='queue', aliases=['q', 'playlist'])
    async def queue_info(self, ctx, *, page=1):
        vc = ctx.voice_client
        page = int(page)
        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently connected to voice!', delete_after=20)

        player = Player(ctx)
        if player.queue.empty():
            return await ctx.send('There are currently no more queued songs.')

        # Grab up to 5 entries from the queue...
        upcoming = list(itertools.islice(
            player.queue._queue, (page-1)*10, page*10))
        fmt = ''
        for item in upcoming:
            duration = self.seconds_to_minutes_string(item[1].info['duration'])
            fmt += "**{} | {} \n:pencil2:by:{}`**\n".format(
                item[1].info["title"], duration, item[1].info['request'])
        embed = discord.Embed(title=f'播放佇列 - 第{page}頁', description=fmt)

        await ctx.send(embed=embed)

    def seconds_to_minutes_string(self, num):
        minutes = num//60
        seconds = num % 60
        result = str(minutes) + ":" + str(seconds)
        return result

    @commands.command(name='now_playing', aliases=['np', 'current', 'currentsong', 'playing'])
    async def now_playing_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently connected to voice!', delete_after=20)

        player = Player(ctx)
        if not player.current:
            return await ctx.send('I am not currently playing anything!')
        else:
            song = player.current
        await ctx.send('**:musical_note:現正播放:musical_note: **\n {} \n:ballot_box_with_check:requested by\n{}'.format(song.info['title'], song.info['request']))

    @commands.command(name='stop', aliases=['dc', 'fuckoff', '滾', '發大財'])
    async def stop_(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            return await ctx.send('I am not currently playing anything!', delete_after=20)

        await self.cleanup(ctx.guild)

    @commands.command(name='search', aliases=['s', '找'])
    async def search_(self, ctx, *, keyword):
        await ctx.trigger_typing()
        embed = discord.Embed(title='搜尋結果', describtion='**請輸入要選取搜尋結果的編號!**')
        results = get_search2(keyword)
        for index, song in enumerate(results):
            duration = self.seconds_to_minutes_string(song['duration'])
            text = "{} [{}]".format(song['title'], duration)
            title_text = str(index + 1)+'.'
            embed.add_field(name=title_text, value=text, inline=False)
        await ctx.send(embed=embed)

        def check(m):
            checklist = []
            for i in range(20):
                checklist.append(i+1)
            try:
                num = int(m.content)
            except:
                return False
            return m.author == ctx.author and m.channel == ctx.channel and num in checklist

        try:
            msg = await bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send(":x: 等候逾時! :x: ")
        except:
            await ctx.send(":x: 錯誤產生! :x: ")
            return

        vc = ctx.voice_client

        if not vc:
            await ctx.invoke(self.connect_)

        player = Player(ctx)
        item = Builder(results[int(msg.content)-1]
                       ['url'], ctx.author).get_item()
        for song in iter(item):
            await player.queue.put((2, song))
            await ctx.send("成功加入歌曲:\n{}\n點歌者:\n{}".format(song.info['title'], song.info['request']))

    @commands.command(name='shuffle', aliases=['random', 'r', '亂'])
    async def shuffle_(self, ctx):
        player = Player(ctx)      
        shuffle(player.queue._queue)
        await ctx.send("**{}** 成功搞砸歌單！:warning:".format(ctx.author))



bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    "?"), description='Holy Player!')


@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(Music(bot))
