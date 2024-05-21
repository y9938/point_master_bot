LANGUAGES = {
    'en': {
        'start': 'Hello! I am your team management bot. Choose an action:',
        'add_points': 'Add points 🏆',
        'today_score': 'Score today 📊',
        'reset_score': 'Reset score 🔄',
        'day_score': 'Score for the day 📅',
        'choose_team': 'Choose a team:',
        'choose_points': 'Choose the number of points for Team {team}:',
        'points_added': 'Team {team} now has {points} points',
        'score_today': 'Score for today ({date}):\n{scores}\nTotal score: {total} points',
        'scores_reset': 'All scores have been reset.',
        'choose_day': 'Choose a day:',
        'score_for_day': 'Score for day {day} ({date}):\n{scores}\nTotal score: {total} points',
        'no_data_for_day': 'No data for day {day} ({date})',
        'language_changed': 'Language changed to English',
        'team': 'T{number}',
        'day': 'D{number}'
    },
    'ru': {
        'start': 'Привет! Я твой бот для управления командами. Выбери действие:',
        'add_points': 'Добавить очки 🏆',
        'today_score': 'Счет сегодня 📊',
        'reset_score': 'Сбросить счет 🔄',
        'day_score': 'Счет за день 📅',
        'choose_team': 'Выберите команду:',
        'choose_points': 'Выберите количество очков для Команды {team}:',
        'points_added': 'Команда {team} теперь имеет {points} очков',
        'score_today': 'Счет на сегодня ({date}):\n{scores}\nОбщий счет: {total} очков',
        'scores_reset': 'Все счета сброшены.',
        'choose_day': 'Выберите день:',
        'score_for_day': 'Счет за {day} день ({date}):\n{scores}\nОбщий счет: {total} очков',
        'no_data_for_day': 'Нет данных за {day} день ({date})',
        'language_changed': 'Язык изменен на русский',
        'team': 'К{number}',
        'day': 'Д{number}'
    }
}

def get_text(language, key, **kwargs):
    return LANGUAGES[language].get(key, '').format(**kwargs)

def get_team_name(language, number):
    return get_text(language, 'team', number=number)

def get_day_name(language, number):
    return get_text(language, 'day', number=number)
