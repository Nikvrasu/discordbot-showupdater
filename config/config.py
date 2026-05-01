from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent.parent / ".env")

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DISCORD_API_KEY = os.getenv("DISCORD_API_KEY")
TMDB_READ_ACCESS_KEY = os.getenv("TMDB_READ_ACCESS_KEY")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))