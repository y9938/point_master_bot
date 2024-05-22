from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from localization import get_text, get_team_name, get_day_name

# Функция для создания основной клавиатуры
def create_main_keyboard():
    keyboard = [
        [KeyboardButton(text=get_text('today_score'))],
        [KeyboardButton(text=get_text('add_points'))],
        [KeyboardButton(text=get_text('remove_points'))],
        [KeyboardButton(text=get_text('day_score'))],
        [KeyboardButton(text=get_text('reset_score'))]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

# Функция для создания inline-кнопок для выбора команды
def create_team_buttons(callback_prefix):
    keyboard = [
        [InlineKeyboardButton(text=get_team_name(i), callback_data=f'{callback_prefix}{i}') for i in range(1, 4)],
        [InlineKeyboardButton(text=get_team_name(i), callback_data=f'{callback_prefix}{i}') for i in range(4, 7)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Функция для создания inline-кнопок для выбора дня
def create_day_buttons():
    keyboard = [
        [InlineKeyboardButton(text=get_day_name(i), callback_data=f'day_{i}') for i in range(1, 5)],
        [InlineKeyboardButton(text=get_day_name(i), callback_data=f'day_{i}') for i in range(5, 9)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
