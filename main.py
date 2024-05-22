import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from config import TOKEN
from data_handler import load_data, reset_old_days
from handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Создание объектов бота и диспетчера
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
router = Router()

# Загрузка данных
data = load_data()

# Регистрация обработчиков
register_handlers(router, data)
dp.include_router(router)

# Основная асинхронная функция
async def main() -> None:
    reset_old_days(data)
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
