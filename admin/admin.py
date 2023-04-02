from loader import dp, bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message
from Kb import admin_btn

ID = 0


# @dp.message_handler(commands=['admin'], is_chat_admin=True)
async def check_admin(message: Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что нужно хозяин???', reply_markup=admin_btn)
    await message.delete()
    print(ID)

def register_admin(dp: Dispatcher):
    dp.register_message_handler(check_admin, commands=['admin'], is_chat_admin=True)
