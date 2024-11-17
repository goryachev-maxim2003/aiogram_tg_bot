import asyncio
from aiogram import Bot, Dispatcher, types, filters

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(filters.CommandStart())
async def process_start_command(message: types.Message):
    await message.answer("Привет!\nНапиши мне что-нибудь!")

@dp.message(filters.Command('help'))
async def process_help_command(message: types.Message):
    # Отправляем сообщение обратно пользователю
    await message.answer("Напиши что-нибудь. Я отправлю это в ответ")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())