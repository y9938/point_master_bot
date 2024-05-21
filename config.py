import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
DATA_FILE = 'data.pkl'
DEFAULT_LANGUAGE = 'ru'
