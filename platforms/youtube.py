from platforms.base import BasePlatform
from googleapiclient.discovery import build

class Youtube(BasePlatform):
    def __init__(self, api_key):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_latest_content(self, channel_id):
        results = []
        
        for duration in ['medium', 'long']:
            response = self.youtube.search().list(
                part='snippet',
                channelId=channel_id,
                order='date',
                maxResults=1,
                type='video',
                videoDuration=duration
            ).execute()
            
            items = response.get('items', [])
            results.extend(items)
        
        if not results:
            return None
        
        results.sort(
            key=lambda x: x['snippet']['publishTime'],
            reverse=True
        )

        return results[0]