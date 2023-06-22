from aiogram.types import Message
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot import dp, BotDB
from handlers.organizer import organizer_start_cmd_handler



button_1 = InlineKeyboardButton(text="Guest", callback_data="guest")
button_2 = InlineKeyboardButton(text="Speaker", callback_data="speaker")
button_3 = InlineKeyboardButton(text="Organizer", callback_data="organizer")
keyboard = InlineKeyboardMarkup().row(button_1, button_2, button_3)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer('У нас скоро пройдет meetup посвященный языку программирования Python, подскажите нам, пожалуйста, вкачестве кого вы будете присутствовать:', 
                         reply_markup=keyboard)
    if (not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    user_is_org = True
    user_is_speaker = False
    user_is_guest = True
    if user_is_org:
        await organizer_start_cmd_handler(message)

    if user_is_speaker:
        pass

    if user_is_guest:
        pass


    #await message.answer(f"Привет {message.from_user.full_name}!\nРады снова видеть тебя!")
