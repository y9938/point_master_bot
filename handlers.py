from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime, timedelta
from keyboards import create_main_keyboard, create_team_buttons, create_day_buttons
from localization import get_text, get_team_name
from data_handler import save_data, update_daily_totals

# Определение состояний для FSM
class PointsForm(StatesGroup):
    waiting_for_points = State()
    waiting_for_remove_points = State()

# Регистрация всех обработчиков команд и коллбеков
def register_handlers(router: Router, data: dict):
    @router.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        # Обработчик команды /start
        await message.answer(get_text('start'), reply_markup=create_main_keyboard())

    @router.message(F.text.in_([get_text('add_points')]))
    async def add_points_handler(message: Message):
        # Обработчик для добавления очков
        await message.answer(get_text('choose_team'), reply_markup=create_team_buttons('add_points_team_'))

    @router.message(F.text.in_([get_text('remove_points')]))
    async def remove_points_handler(message: Message):
        # Обработчик для отнимания очков
        await message.answer(get_text('choose_team'), reply_markup=create_team_buttons('remove_points_team_'))

    @router.callback_query(F.data.startswith('add_points_team_'))
    async def process_team_callback(callback_query: CallbackQuery, state: FSMContext):
        # Обработчик для выбора команды для добавления очков
        team = int(callback_query.data.split('_')[-1])
        await callback_query.message.answer(get_text('enter_points'))
        await state.update_data(team=team)
        await state.set_state(PointsForm.waiting_for_points)

    @router.callback_query(F.data.startswith('remove_points_team_'))
    async def process_remove_team_callback(callback_query: CallbackQuery, state: FSMContext):
        # Обработчик для выбора команды для отнимания очков
        team = int(callback_query.data.split('_')[-1])
        await callback_query.message.answer(get_text('enter_points'))
        await state.update_data(team=team)
        await state.set_state(PointsForm.waiting_for_remove_points)

    @router.message(PointsForm.waiting_for_points)
    async def process_entered_points(message: Message, state: FSMContext):
        # Обработчик для обработки введенных очков
        user_data = await state.get_data()
        team = user_data['team']
        try:
            points = int(message.text)
            today = str(datetime.now().date())
            if today not in data['daily_totals']:
                data['daily_totals'][today] = {i: 0 for i in range(1, 7)}
            data['daily_totals'][today][team] += points
            save_data(data)
            await message.answer(get_text('points_added', team=get_team_name(team), points=data["daily_totals"][today][team]))
            await state.clear()
        except ValueError:
            await message.answer(get_text('invalid_number'))

    @router.message(PointsForm.waiting_for_remove_points)
    async def process_entered_remove_points(message: Message, state: FSMContext):
        # Обработчик для обработки введенных очков для отнимания
        user_data = await state.get_data()
        team = user_data['team']
        try:
            points = int(message.text)
            today = str(datetime.now().date())
            if today not in data['daily_totals']:
                data['daily_totals'][today] = {i: 0 for i in range(1, 7)}
            data['daily_totals'][today][team] -= points
            save_data(data)
            await message.answer(get_text('points_removed', team=get_team_name(team), points=data["daily_totals"][today][team]))
            await state.clear()
        except ValueError:
            await message.answer(get_text('invalid_number'))

    @router.callback_query(F.data.startswith('add_') & F.data.contains('_points_to_'))
    async def process_points_callback(callback_query: CallbackQuery):
        # Обработчик для добавления очков команде
        parts = callback_query.data.split('_')
        points = int(parts[1])
        team_number = int(parts[-1])
        today = str(datetime.now().date())
        update_daily_totals(data, team_number, points)
        await callback_query.message.answer(get_text('points_added', team=get_team_name(team_number), points=data["daily_totals"][today][team_number]))

    @router.callback_query(F.data.startswith('remove_') & F.data.contains('_points_from_'))
    async def process_remove_points_callback(callback_query: CallbackQuery):
        # Обработчик для отнимания очков у команды
        parts = callback_query.data.split('_')
        points = int(parts[1])
        team_number = int(parts[-1])
        today = str(datetime.now().date())
        update_daily_totals(data, team_number, -points)
        await callback_query.message.answer(get_text('points_removed', team=get_team_name(team_number), points=data["daily_totals"][today][team_number]))

    @router.message(F.text.in_([get_text('today_score')]))
    async def daily_total(message: Message):
        # Обработчик для отображения счета на сегодня
        today = str(datetime.now().date())
        total = sum(data['daily_totals'][today].values())
        message_text = '\n'.join([f'{get_team_name(team)}: {score}' for team, score in data['daily_totals'][today].items()])
        await message.answer(get_text('score_today', date=today, scores=message_text, total=total), reply_markup=create_main_keyboard())

    @router.message(F.text.in_([get_text('reset_score')]))
    async def reset_scores(message: Message):
        # Обработчик для сброса счета
        today = str(datetime.now().date())
        data['daily_totals'][today] = {i: 0 for i in range(1, 7)}
        save_data(data)
        await message.answer(get_text('scores_reset'), reply_markup=create_main_keyboard())

    @router.message(F.text.in_([get_text('day_score')]))
    async def select_day_handler(message: Message):
        # Обработчик для выбора дня
        await message.answer(get_text('choose_day'), reply_markup=create_day_buttons())

    @router.callback_query(F.data.startswith('day_'))
    async def process_day_callback(callback_query: CallbackQuery):
        # Обработчик для отображения счета за определенный день
        day = int(callback_query.data.split('_')[-1])
        date = str((datetime.now() - timedelta(days=day-1)).date())
        if date in data['daily_totals']:
            total = sum(data['daily_totals'][date].values())
            message_text = '\n'.join([f'{get_team_name(team)}: {score}' for team, score in data['daily_totals'][date].items()])
            await callback_query.message.answer(get_text('score_for_day', day=day, date=date, scores=message_text, total=total))
        else:
            await callback_query.message.answer(get_text('no_data_for_day', day=day, date=date))
