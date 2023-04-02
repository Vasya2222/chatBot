from aiogram.utils import executor
from Handler.hd import dp
from DataBase import create_table
from admin import register_massage_handler, register_admin
from game import register_handler_game


async def on_start(_):
    try:
        create_table()
        print('DB запущен')
    except:
        print("DB не запущен")
    print("Бот запущен")
register_massage_handler(dp)
register_admin(dp)
register_handler_game(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_start)
