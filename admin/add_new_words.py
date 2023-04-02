from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from DataBase import add_words, find_words
from aiogram.dispatcher import Dispatcher
from loader import bot
from Kb import admin_btn

class FSM_add_words(StatesGroup):
    english_word = State()
    russian_word = State()


ID = None


# @dp.message_handler(commands=['admin'], is_chat_admin=True)
async def check_admin(message: Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что нужно хозяин???', reply_markup=admin_btn)
    await message.delete()
    print(ID)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(check_admin, commands=['admin'], is_chat_admin=True)


# @dp.message_handler(commands=['add'], state=None)
async def english(message: Message):
    print(ID)
    if message.from_user.id == ID:
        await FSM_add_words.english_word.set()
        await message.reply("Введите слово на английском")


# @dp.message_handler(state=FSM_add_words.english_word)
async def russian(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['word_English'] = message.text
        await FSM_add_words.next()
        await message.reply('Введите перевод на русском')


# @dp.message_handler(state=FSM_add_words.russian_word)
async def finish(message: Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['translate_word_on_Russian'] = message.text

        await add_words(state)
        await message.answer(text='в базу данных сохранено')
        await state.finish()


def register_massage_handler(dp: Dispatcher):
    dp.register_message_handler(english, commands=['add'], state=None)
    dp.register_message_handler(russian, state=FSM_add_words.english_word)
    dp.register_message_handler(finish, state=FSM_add_words.russian_word)
