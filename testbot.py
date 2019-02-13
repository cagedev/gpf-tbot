from PhotoFrameBot import TELEGRAM_TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)

updater = Updater(token=TELEGRAM_TOKEN)
dispatcher = updater.dispatcher


# initialise bot
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# setup destination for media mirror - TODO
def setup(bot, update, args):
    for a in args:
        bot.send_message(chat_id=update.message.chat_id,
                         text=a.upper() )
start_handler = CommandHandler('setup', setup, pass_args=True)
dispatcher.add_handler(start_handler)


# error unknown commands - default behaviour
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


# echo non-commands - default behaviour
def save(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
