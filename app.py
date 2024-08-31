from aiogram import types, Bot, Dispatcher, F
token = '7536121934:AAGa_2CbmqcMYPvXdT9mrgw5bi6NsAioqNI'
from aiogram.filters import CommandStart , Command
import  asyncio
db = Dispatcher()
bot = Bot(token=token)


@db.message(CommandStart())
async def start_bot(message:types.Message):
    await message.answer('salom ')

@db.message(Command('help'))
async def help(message:types.Message):
    await message.answer('Sizga qanday yordam bera olaman ')

@db.message(F.text)
async def text_handler(message:types.Message):
    await message.answer('text=message.text')

@db.message(F.photo)
async def get_photo(message:types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    width = photo.width
    height = photo.height
    file_size = photo.file_size
    await message.answer(text = f'Photo yubordingiz\n'
                         f'file_ID:{file_id}\n'
                         f'width: {width}\n'
                         f'height: {height}\n'
                         f'file_size: {file_size} byte')

@db.message(F.video)
async def get_video(message:types.Message):
    video = message.video
    file_duration =video.duration
    width = video.width
    height = video.height
    file_size = video.file_size
    await message.answer(text='Video yubordingiz\n'
                        f'file_duration:{file_duration}\n'
                        f'width: {width}\n'
                        f'height: {height}\n'
                        f'file_size: {file_size} byte')
async def main():
    await db.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
