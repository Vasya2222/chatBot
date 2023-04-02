from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from random import randint
from DataBase import game_words, check_word


random = 0


class FSM_game(StatesGroup):
    guess_the_word = State()


# @dp.message_handler(commands=['game'], state=None)
async def start_guesses_words(message: Message):
        await FSM_game.guess_the_word.set()
        global random
        random = (randint(1, 6),)
        await message.answer(text=f'Напишите правильно слово на русском')
        await message.answer(text=f'{game_words(random)}')


# @dp.message_handler(state=FSM_game.guess_the_word)
async def check_correct_word(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text
    print(random[0], check_word((message.text,))[0][0])
    if check_word((message.text,))[0][0] == random[0]:
        await message.answer(text="Вы правильно перевели слово")
    await state.finish()


def register_handler_game(dp: Dispatcher):
    dp.register_message_handler(start_guesses_words, commands=['game'], state=None)
    dp.register_message_handler(check_correct_word, state=FSM_game.guess_the_word)
