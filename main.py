from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8841744903:AAGLRpnTj00af2rj1QLDh2vMfKr2AK6GMYQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Bot ishlayapti ✅")

if name == "main":
    executor.start_polling(dp, skip_updates=True)
