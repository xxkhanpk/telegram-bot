
from telegram.ext import Updater, CommandHandler

# Replace this with your actual bot token from BotFather
TOKEN = 'PASTE_YOUR_BOT_TOKEN_HERE'

def start(update, context):
    update.message.reply_text("Hello jaanu 😘 Your bot is running!")

def help_command(update, context):
    update.message.reply_text("I'm your sweet bot 💋 Use /start to test me!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
