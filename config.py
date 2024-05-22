import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Токен бота, загружаемый из переменной окружения
TOKEN = os.getenv('BOT_TOKEN')

# Путь к файлу данных
DATA_FILE = 'data.pkl'

# Язык по умолчанию
DEFAULT_LANGUAGE = 'ru'
