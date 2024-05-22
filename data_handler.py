import os
import pickle
from datetime import datetime, timedelta
from config import DATA_FILE

# Функция для загрузки данных из файла
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            data = pickle.load(f)
            if not isinstance(data, dict) or 'commands' not in data or 'daily_totals' not in data:
                raise ValueError("Invalid data structure in file")
            return data
    else:
        # Инициализация данных, если файл не существует
        return {
            'commands': {i: 0 for i in range(1, 7)},
            'daily_totals': {str((datetime.now() - timedelta(days=i)).date()): {i: 0 for i in range(1, 7)} for i in range(8)}
        }

# Функция для сохранения данных в файл
def save_data(data):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)

# Функция для сброса данных за старые дни
def reset_old_days(data):
    today = datetime.now().date()
    # Удаление данных за старые дни (старше 7 дней)
    for i in range(8, 15):
        old_day = str(today - timedelta(days=i))
        if old_day in data['daily_totals']:
            del data['daily_totals'][old_day]
    # Инициализация данных за последние 7 дней, если их нет
    for i in range(8):
        new_day = str(today - timedelta(days=i))
        if new_day not in data['daily_totals']:
            data['daily_totals'][new_day] = {i: 0 for i in range(1, 7)}
    save_data(data)

# Функция для обновления ежедневных итогов
def update_daily_totals(data, team, value):
    today = str(datetime.now().date())
    if today not in data['daily_totals']:
        data['daily_totals'][today] = {i: 0 for i in range(1, 7)}
    data['daily_totals'][today][team] += value
    save_data(data)
