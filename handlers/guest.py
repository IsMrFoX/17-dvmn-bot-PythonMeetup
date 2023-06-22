from aiogram.types import Message
from dispatcher import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@dp.message_handler(commands='guest')
async def guest_start_cmd_handler(message: Message):
    # if (not BotDB.user_exists(message.from_user.id)):
    #     BotDB.add_user(message.from_user.id)
    await message.answer(
        f"Рады приветсвовать вас, {message.from_user.full_name}! \nЯ - PythonMeetupBot ")
