import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Your Telegram bot token
TOKEN = 'your_token'
# Link to the instruction channel
CHANNEL_URL = 'your_chanel'
# URL of your web application
WEB_APP_URL = 'your_url'

# Logging setup for debugging and monitoring the bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Asynchronous function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Keyboard with buttons
    keyboard = [
        [InlineKeyboardButton("📖 Instruction 📖", url=CHANNEL_URL)],
        [InlineKeyboardButton("🎰 Get Signal 🎰", web_app=WebAppInfo(url=WEB_APP_URL))],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    # Welcome message text with HTML formatting
    text = ('<b>🎉 Welcome to our telegram bot!!!</b>'
            '‼️ Guys, before using the software, we <b>STRONGLY</b> recommend reading the detailed manual, which will answer all your questions.'
            'It is available on our channel. By saving 5 minutes of your time, you risk losing your money.')

    # Opening the image for sending
    photo = open('welcome_image.jpg', 'rb')

    # Sending a message depending on the type of update (message or callback query)
    if update.message:
        await update.message.reply_photo(photo=photo, caption=text, parse_mode="HTML", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_photo(photo=photo, caption=text, parse_mode="HTML", reply_markup=reply_markup)

# Asynchronous function to handle button clicks
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Checking if the callback query is related to the /start command
    if query.data == 'start':
        await start(update, context)

if __name__ == '__main__':
    # Creating an application instance using the token
    application = ApplicationBuilder().token(TOKEN).build()

    # Creating handlers for the /start command and button clicks
    start_handler = CommandHandler('start', start)
    button_handler = CallbackQueryHandler(button)

    # Adding handlers to the application
    application.add_handler(start_handler)
    application.add_handler(button_handler)

    # Running the application in polling mode to process updates
    application.run_polling()
