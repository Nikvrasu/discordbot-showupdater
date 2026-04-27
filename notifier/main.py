from platforms.youtube import Youtube
from platforms.tmdb import Tmdb
from config.config import YOUTUBE_API_KEY, DISCORD_API_KEY, TMDB_READ_ACCESS_KEY, TMDB_API_KEY
import json

if __name__ == "__main__":
    youtube = Youtube(YOUTUBE_API_KEY)
    tmdb = Tmdb(TMDB_API_KEY)
    channels = json.load(open('data/channels.json'))
    for channel in channels:
        if channel['platform'] == 'youtube':
            print(f"Fetching latest content for YouTube channel: {channel['name']} (ID: {channel['channel_id']})")
            latest_video = youtube.get_latest_content(channel['channel_id'])
            print(latest_video['snippet']['publishTime'] + " - " + latest_video['snippet']['title'] + " - " + latest_video['snippet']['channelTitle'])
        if channel['platform'] == 'tmdb':
            print(f"Fetching latest content for TMDB channel: {channel['name']} (ID: {channel['channel_id']})")
            latest_content = tmdb.get_latest_content(channel['channel_id'])
            print(latest_content['last_episode_to_air']['air_date'] + " - " + latest_content['name'] + " - " + latest_content['last_episode_to_air']['name'])
