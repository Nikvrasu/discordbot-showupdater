from bot.notifier import Notifier
from platforms.youtube import Youtube
from platforms.tmdb import Tmdb
from config.config import YOUTUBE_API_KEY, DISCORD_API_KEY, TMDB_READ_ACCESS_KEY, TMDB_API_KEY, DISCORD_CHANNEL_ID
from tasks.scheduler import Scheduler
from bot.bot import Bot

if __name__ == "__main__":
    keys = {"YOUTUBE_API_KEY": YOUTUBE_API_KEY, "DISCORD_API_KEY": DISCORD_API_KEY, "TMDB_READ_ACCESS_KEY": TMDB_READ_ACCESS_KEY, "TMDB_API_KEY": TMDB_API_KEY, "DISCORD_CHANNEL_ID": DISCORD_CHANNEL_ID}
    notifier = Notifier(keys)
    bot = Bot(notifier=notifier)
    bot.run(DISCORD_API_KEY)