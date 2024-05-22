LANGUAGES = {
    'ru': {
        'start': 'Привет! Я твой бот для управления командами. Выбери действие:',
        'today_score': 'Счет сегодня 📊',
        'add_points': 'Добавить очки 🏆',
        'remove_points': 'Отнять очки 🏅',
        'day_score': 'Счет за день 📅',
        'reset_score': 'Сбросить счет 🔄',
        'enter_points': 'Пожалуйста, введите количество очков:',
        'choose_team': 'Выберите команду:',
        'choose_points': 'Выберите количество очков для Команды {team}:',
        'points_added': 'Команда {team} теперь имеет {points} очков',
        'points_removed': 'Команда {team} теперь имеет {points} очков',
        'invalid_number': 'Неверное число. Пожалуйста, введите действительное число.',
        'score_today': 'Счет на сегодня ({date}):\n{scores}\nОбщий счет: {total} очков',
        'scores_reset': 'Все счета сброшены.',
        'choose_day': 'Выберите день:',
        'score_for_day': 'Счет за {day} день ({date}):\n{scores}\nОбщий счет: {total} очков',
        'no_data_for_day': 'Нет данных за {day} день ({date})',
        'language_changed': 'Язык изменен на русский',
        'team': 'К{number}',
        'day': 'Д{number}'
    },
    'en': {
        'start': 'Hello! I am your team management bot. Choose an action:',
        'today_score': 'Score today 📊',
        'add_points': 'Add points 🏆',
        'remove_points': 'Remove points 🏅',
        'day_score': 'Score for the day 📅',
        'reset_score': 'Reset score 🔄',
        'enter_points': 'Please enter the number of points:',
        'choose_team': 'Choose a team:',
        'choose_points': 'Choose the number of points for Team {team}:',
        'points_added': 'Team {team} now has {points} points',
        'points_removed': 'Team {team} now has {points} points',
        'invalid_number': 'Invalid number. Please enter a valid number.',
        'score_today': 'Score for today ({date}):\n{scores}\nTotal score: {total} points',
        'scores_reset': 'All scores have been reset.',
        'choose_day': 'Choose a day:',
        'score_for_day': 'Score for day {day} ({date}):\n{scores}\nTotal score: {total} points',
        'no_data_for_day': 'No data for day {day} ({date})',
        'language_changed': 'Language changed to English',
        'team': 'T{number}',
        'day': 'D{number}'
    }
}

def get_text(language, key, **kwargs):
    """
    Получение текста на нужном языке.
    """
    return LANGUAGES[language].get(key, '').format(**kwargs)

def get_team_name(language, number):
    """
    Получение имени команды на нужном языке.
    """
    return get_text(language, 'team', number=number)

def get_day_name(language, number):
    """
    Получение имени дня на нужном языке.
    """
    return get_text(language, 'day', number=number)