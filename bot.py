from locale import LC_ALL, setlocale
from time import sleep
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices

setlocale(LC_ALL,"ru")
telegram_bot_token = 'TOKEN'

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"⚜️Токен: {coin}\nЦена: ${price:,.2f}\nИзменение за час: {change_hour:.3f}%\nИзменение за день: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


dispatcher.add_handler(CommandHandler("price", start))
updater.start_polling()