# PointMaster Bot

[PointMaster Bot](https://t.me/point_master_bot) is a Telegram bot designed to track and manage team scores over an 8-day period. The bot provides a user-friendly interface for adding points to teams, viewing current scores, and checking scores for previous days.

[PointMaster Bot](https://t.me/point_master_bot) — это Telegram-бот, предназначенный для отслеживания и управления счетами команд в течение 8 дней. Бот предоставляет удобный интерфейс для добавления очков командам, просмотра текущего счета и проверки счетов за предыдущие дни.

## Screenshots / Скриншоты

<img src="images/1.jpg" alt="Screenshot 1" width="250">
<img src="images/2.jpg" alt="Screenshot 2" width="250">
<img src="images/3.jpg" alt="Screenshot 3" width="250">
<img src="images/4.jpg" alt="Screenshot 4" width="250">

## Installation / Установка

1. **Clone the repository or download the project archive / Клонируйте репозиторий или скачайте архив с проектом**:

    ```bash
    git clone https://github.com/y9938/point_master_bot.git
    cd point_master_bot
    ```

2. **Create and activate a virtual environment / Создайте и активируйте виртуальное окружение**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: .\venv\Scripts\activate
    ```

3. **Install the dependencies / Установите зависимости**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file and add your Telegram bot token / Создайте файл `.env` и добавьте в него токен вашего Telegram-бота**:

    ```plaintext
    BOT_TOKEN=your_bot_token_here
    ```

## Running the Bot / Запуск

1. **Activate the virtual environment (if not already activated) / Активируйте виртуальное окружение (если оно еще не активировано)**:

    ```bash
    source venv/bin/activate  # For Windows: venv\Scripts\activate / Для Windows: venv\Scripts\activate
    ```

2. **Start the bot / Запустите бота**:

    ```bash
    python bot.py
    ```

## Usage / Использование

- **`/start`**: Starts the bot and greets the user / Запускает бота и приветствует пользователя.
- **`Add points 🏆` / `Добавить очки 🏆`**: Allows adding points to a team / Позволяет добавить очки команде.
- **`Score today 📊` / `Счет сегодня 📊`**: Shows the current score / Показывает текущий счет.
- **`Score for the day 📅` / `Счет за день 📅`**: Allows viewing scores for previous days / Позволяет посмотреть счет за предыдущие дни.
- **`Reset score 🔄` / `Сбросить счет 🔄`**: Resets the score / Сбрасывает счет.
- **`/language`**: Switches the bot's language between English and Russian / Переключает язык бота между английским и русским.

## License / Лицензия

This project is licensed under the [MIT License](LICENSE).

Этот проект распространяется под лицензией [MIT](LICENSE).
