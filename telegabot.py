from aiogram import Bot, executor , Dispatcher, types
from weather import get_the_weather_by_coordinates_now
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class fsm(StatesGroup):
    get_days = State()


memory = MemoryStorage()
bot = Bot("5820676043:AAFGa0G46AXJXT8MYge9GXxMbC9s3IMvJdc", parse_mode="HTML")
dp = Dispatcher(bot,memory)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton(text="get geo",request_location=True))
ik1 = InlineKeyboardButton(text="setings", callback_data="setings")
ikb = InlineKeyboardMarkup()
ikb.add(ik1)



@dp.message_handler(commands=["start"])
async def cmd_start(message: types.message):
    await bot.send_message(message.chat.id,
                     text="Юзай кнопочки",
                     reply_markup=kb)
    await bot.send_message(message.chat.id,
                           text="Настроить вывод погоды",
                           reply_markup=ikb)



@dp.message_handler(content_types=["location"])
async def loca(message: types.message):
    lat = message.location["latitude"]
    lng = message.location["longitude"]
    print("Получаю погоду по координатам")
    weather = get_the_weather_by_coordinates_now(0,lat, lng)
    print("Отправляю погоду")
    await bot.send_message(message.chat.id,text=weather)


@dp.callback_query_handler()
async def call_settings(callback: types.CallbackQuery):
    if callback.data == "setings":
        ikb1 = InlineKeyboardMarkup(row_width=4)
        i1 = InlineKeyboardButton(text="Дни",callback_data="days")
        i2 = InlineKeyboardButton(text="Назад",callback_data="back")
        ikb1.add(i1,i2)
        await callback.message.edit_text("Вы можете сменить настройки вывода погоды",
                                         reply_markup=ikb1)
        
    if callback.data == "back":
        await callback.message.edit_text(text="Настроить вывод погоды",
                                         reply_markup=ikb)
    
    if callback.data == "days":
        ikb1 = InlineKeyboardMarkup(row_width=4)
        i2 = InlineKeyboardButton(text="Отмена",callback_data="back")
        ikb1.add(i2)
        await callback.message.edit_text("На сколько дней вперёд вы хотите получить прогноз?",
                                         reply_markup=ikb1)
    



if __name__ == "__main__":
    executor.start_polling(dp, 
                           skip_updates=True)
    