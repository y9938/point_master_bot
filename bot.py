import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime, timedelta
from config import TOKEN, DEFAULT_LANGUAGE
from data_handler import load_data, save_data, reset_old_days, update_daily_totals
from localization import get_text, get_team_name, get_day_name

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание объектов бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Загрузка данных
data = load_data()

# Функция для получения языка пользователя
def get_user_language(user_id):
    return data['languages'].get(user_id, DEFAULT_LANGUAGE)

# Функция для создания клавиатуры
def create_main_keyboard(language):
    keyboard = [
        [KeyboardButton(text=get_text(language, 'add_points'))],
        [KeyboardButton(text=get_text(language, 'today_score'))],
        [KeyboardButton(text=get_text(language, 'reset_score'))],
        [KeyboardButton(text=get_text(language, 'day_score'))]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Функция для создания inline-кнопок для выбора команды
def create_team_buttons(language):
    keyboard = [
        [InlineKeyboardButton(text=get_team_name(language, i), callback_data=f'add_points_team_{i}') for i in range(1, 4)],
        [InlineKeyboardButton(text=get_team_name(language, i), callback_data=f'add_points_team_{i}') for i in range(4, 7)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Функция для создания inline-кнопок для добавления очков
def create_points_buttons(team):
    keyboard = [
        [InlineKeyboardButton(text=f'+{i}', callback_data=f'add_{i}_points_to_{team}') for i in [10, 20]],
        [InlineKeyboardButton(text=f'+{i}', callback_data=f'add_{i}_points_to_{team}') for i in [50, 100]]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Функция для создания inline-кнопок для выбора дня
def create_day_buttons(language):
    keyboard = [
        [InlineKeyboardButton(text=get_day_name(language, i), callback_data=f'day_{i}') for i in range(1, 5)],
        [InlineKeyboardButton(text=get_day_name(language, i), callback_data=f'day_{i}') for i in range(5, 9)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Обработчик команды /start
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    language = get_user_language(message.from_user.id)
    await message.answer(get_text(language, 'start'), reply_markup=create_main_keyboard(language))

# Обработчик для добавления очков
@dp.message(lambda message: message.text in [get_text(get_user_language(message.from_user.id), 'add_points')])
async def add_points_handler(message: Message):
    language = get_user_language(message.from_user.id)
    await message.answer(get_text(language, 'choose_team'), reply_markup=create_team_buttons(language))

# Обработчик для выбора команды
@dp.callback_query(lambda c: c.data.startswith('add_points_team_'))
async def process_team_callback(callback_query: types.CallbackQuery):
    team = int(callback_query.data.split('_')[-1])
    language = get_user_language(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, get_text(language, 'choose_points', team=get_team_name(language, team)), reply_markup=create_points_buttons(team))

# Обработчик для добавления очков команде
@dp.callback_query(lambda c: c.data.startswith('add_') and '_points_to_' in c.data)
async def process_points_callback(callback_query: types.CallbackQuery):
    parts = callback_query.data.split('_')
    points = int(parts[1])
    team_number = int(parts[-1])
    language = get_user_language(callback_query.from_user.id)
    today = str(datetime.now().date())
    if today not in data['daily_totals']:
        data['daily_totals'][today] = {i: 0 for i in range(1, 7)}
    data['daily_totals'][today][team_number] += points
    save_data(data)
    await bot.send_message(callback_query.from_user.id, get_text(language, 'points_added', team=get_team_name(language, team_number), points=data["daily_totals"][today][team_number]))

# Обработчик для отображения счета на сегодня
@dp.message(lambda message: message.text in [get_text(get_user_language(message.from_user.id), 'today_score')])
async def daily_total(message: Message):
    today = str(datetime.now().date())
    language = get_user_language(message.from_user.id)
    total = sum(data['daily_totals'][today].values())
    message_text = '\n'.join([f'{get_team_name(language, team)}: {score}' for team, score in data['daily_totals'][today].items()])
    await message.answer(get_text(language, 'score_today', date=today, scores=message_text, total=total), reply_markup=create_main_keyboard(language))

# Обработчик для сброса счета
@dp.message(lambda message: message.text in [get_text(get_user_language(message.from_user.id), 'reset_score')])
async def reset_scores(message: Message):
    today = str(datetime.now().date())
    language = get_user_language(message.from_user.id)
    data['daily_totals'][today] = {i: 0 for i in range(1, 7)}
    save_data(data)
    await message.answer(get_text(language, 'scores_reset'), reply_markup=create_main_keyboard(language))

# Обработчик для выбора дня
@dp.message(lambda message: message.text in [get_text(get_user_language(message.from_user.id), 'day_score')])
async def select_day_handler(message: Message):
    language = get_user_language(message.from_user.id)
    await message.answer(get_text(language, 'choose_day'), reply_markup=create_day_buttons(language))

# Обработчик для отображения счета за определенный день
@dp.callback_query(lambda c: c.data.startswith('day_'))
async def process_day_callback(callback_query: types.CallbackQuery):
    day = int(callback_query.data.split('_')[-1])
    date = str((datetime.now() - timedelta(days=day-1)).date())
    language = get_user_language(callback_query.from_user.id)
    if date in data['daily_totals']:
        total = sum(data['daily_totals'][date].values())
        message_text = '\n'.join([f'{get_team_name(language, team)}: {score}' for team, score in data['daily_totals'][date].items()])
        await bot.send_message(callback_query.from_user.id, get_text(language, 'score_for_day', day=day, date=date, scores=message_text, total=total))
    else:
        await bot.send_message(callback_query.from_user.id, get_text(language, 'no_data_for_day', day=day, date=date))

# Обработчик для переключения языка
@dp.message(Command(commands=['language']))
async def change_language(message: Message):
    user_id = message.from_user.id
    current_language = get_user_language(user_id)
    new_language = 'en' if current_language == 'ru' else 'ru'
    data['languages'][user_id] = new_language
    save_data(data)
    await message.answer(get_text(new_language, 'language_changed'), reply_markup=create_main_keyboard(new_language))

# Основная асинхронная функция
async def main() -> None:
    reset_old_days(data)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
