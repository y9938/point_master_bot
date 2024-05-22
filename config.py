import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Токен бота
TOKEN = os.getenv('BOT_TOKEN')

# Путь к файлу данных
DATA_FILE = 'data.pkl'
