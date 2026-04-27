from platforms.base import BasePlatform
import requests

class Tmdb(BasePlatform):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_latest_content(self, channel_id):
        response = requests.get(
            f"https://api.themoviedb.org/3/tv/{channel_id}",
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch TMDB data: {response.status_code} - {response.text}")