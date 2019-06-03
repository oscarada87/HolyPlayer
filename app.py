from src import bot
from config import BOT_TOKEN

if __name__ == '__main__':
    bot.run(BOT_TOKEN, bot=True, reconnect=True)
