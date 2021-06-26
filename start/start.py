from aiogram import Bot, Dispatcher, executor, types


bot = Bot('1815758515:AAEZ8-w5ya35zYCNhMckDik2YNDbHmmihww')
dp = Dispatcher(bot)

# хендлер
@dp.message_handler()
async def get_message(message: types.Message): # асинхронная функция куда попадают все сообщения кроме фоток
    chat_id = message.chat.id
    text = "какой то текст"

    sent_message = await bot.send_message(chat_id=chat_id, text=text)
    print(sent_message.to_python())

# сюда поступают и обрабатываются все наши апдейты, до попадания в хендлер
executor.start_polling(dp)
