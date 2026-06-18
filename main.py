import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8841744903:AAGLRpnTj00af2rj1QLDh2vMfKr2AK6GMYQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("Bot ishlayapti ✅")

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
