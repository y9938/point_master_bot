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
    }
}

# Функция для получения текста на русском языке
def get_text(key, **kwargs):
    return LANGUAGES['ru'].get(key, '').format(**kwargs)

# Функция для получения имени команды на русском языке
def get_team_name(number):
    return get_text('team', number=number)

# Функция для получения имени дня на русском языке
def get_day_name(number):
    return get_text('day', number=number)
