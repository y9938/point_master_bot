from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from localization import get_text, get_team_name, get_day_name

def create_main_keyboard(language):
    """
    Создание основной клавиатуры.
    """
    keyboard = [
        [KeyboardButton(text=get_text(language, 'today_score'))],
        [KeyboardButton(text=get_text(language, 'add_points'))],
        [KeyboardButton(text=get_text(language, 'remove_points'))],
        [KeyboardButton(text=get_text(language, 'day_score'))],
        [KeyboardButton(text=get_text(language, 'reset_score'))]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def create_team_buttons(language, callback_prefix):
    """
    Создание inline-кнопок для выбора команды.
    """
    keyboard = [
        [InlineKeyboardButton(text=get_team_name(language, i), callback_data=f'{callback_prefix}{i}') for i in range(1, 4)],
        [InlineKeyboardButton(text=get_team_name(language, i), callback_data=f'{callback_prefix}{i}') for i in range(4, 7)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def create_day_buttons(language):
    """
    Создание inline-кнопок для выбора дня.
    """
    keyboard = [
        [InlineKeyboardButton(text=get_day_name(language, i), callback_data=f'day_{i}') for i in range(1, 5)],
        [InlineKeyboardButton(text=get_day_name(language, i), callback_data=f'day_{i}') for i in range(5, 9)]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
