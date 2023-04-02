from loader import dp
from aiogram.types import Message
from Kb import kb_clicker
from DataBase import find_words, game_words, check_word
from random import randint

random = 0


@dp.message_handler(commands=['start'])  # на start будет отвечать приветствием по имени
async def com_start(update: Message):
    await update.answer(f'{update.from_user.first_name}, тебе здесь не рады!', reply_markup=kb_clicker)
