from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}"
                         f"\n\nBotdan foydalanish uchun YouTube havolasini yuboring!"
                         f"\n\nEslatma Bot test rejimida ishlamoqda")