from telegram.ext import Updater, CommandHandler
import logging
TOKEN = 'TOKEN'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я активировался")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()