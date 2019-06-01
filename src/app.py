# Config
from Config import BOT_TOKEN

# Library
import asyncio
import discord
from pprint import pprint
from discord.ext import commands

# Module

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """Joins a voice channel"""
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            if ctx.voice_client is not None:
                return await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()
        else:
            await ctx.send("You are not connected to a voice channel.")
            raise commands.CommandError("Author not connected to a voice channel.")

    # Testing Function
    # @commands.command()
    # async def play(self, ctx):
    #     """Plays a file from the local filesystem"""

    #     source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("../test/data/freaks.mp3"), volume=0.5)
    #     ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

    #     await ctx.send('Now playing: {}'.format("freaks.mp3"))

    # * 代表後面的參數是 **kwags
    @commands.command(aliases=['p', '播', '播放'])
    async def play(self, ctx, *, keyword):
        pprint(ctx.author.name)
        pprint(keyword)

    @commands.command(aliases=['dc', 'fuckoff'])
    async def disconnect(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()         

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"),
                description='Relatively simple music bot example')

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.add_cog(Music(bot))
bot.run(BOT_TOKEN)