import json

from platforms.tmdb import Tmdb
from platforms.youtube import Youtube
from datetime import date


class Notifier():
    def __init__(self, keys):
        self.youtube_key = keys['YOUTUBE_API_KEY']
        self.tmdb_key = keys['TMDB_API_KEY']
        self.discord_channel_id = int(keys['DISCORD_CHANNEL_ID'])
        self.youtube = Youtube(self.youtube_key)
        self.tmdb = Tmdb(self.tmdb_key)

    async def check_for_updates(self, bot):
        todays_date = date.today()
        channels = json.load(open('data/channels.json'))
        for channel in channels:
            if channel['platform'] == 'youtube':
                print(f"Fetching latest content for YouTube channel: {channel['name']} (ID: {channel['channel_id']})")
                latest_video = self.youtube.get_latest_content(channel['channel_id'])
                print(latest_video['snippet']['publishTime'] + " - " + latest_video['snippet']['title'] + " - " + latest_video['snippet']['channelTitle'])
                if todays_date.isoformat() in latest_video['snippet']['publishTime']:
                     await self.send_notification(bot, f"New video from {latest_video['snippet']['channelTitle']} published today!")
                     await self.send_notification(bot, f"{latest_video['snippet']['channelTitle']} - {latest_video['snippet']['title']} aired today!")
            if channel['platform'] == 'tmdb':
                print(f"Fetching latest content for TMDB channel: {channel['name']} (ID: {channel['channel_id']})")
                latest_content = self.tmdb.get_latest_content(channel['channel_id'])
                # print(latest_content['last_episode_to_air']['air_date'] + " - " + latest_content['name'] + " - " + latest_content['last_episode_to_air']['name'])
                # print(todays_date.isoformat() + " - " + latest_content['last_episode_to_air']['air_date'])
                if todays_date.isoformat() in latest_content['last_episode_to_air']['air_date']:
                    await self.send_notification(bot, f"New episode of {latest_content['name']} published today!")
                    await self.send_notification(bot, f"{latest_content['name']} - {latest_content['last_episode_to_air']['name']} aired today!")

    async def send_notification(self, bot, content):
        channel = bot.get_channel(self.discord_channel_id)
        await channel.send(content)