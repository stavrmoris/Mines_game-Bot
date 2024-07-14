import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Токен вашего Telegram-бота
TOKEN = '7451759217:AAFdFhVfx6BSWSZHaJAO8M3Y624FvAUkH4M'
# Ссылка на канал с инструкцией
CHANNEL_URL = 'https://t.me/RichFamilyWin/6'
# URL вашего веб-приложения
WEB_APP_URL = 'https://stavrmoris.pythonanywhere.com/'

# Настройка логирования для отладки и мониторинга работы бота
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Асинхронная функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Клавиатура с кнопками
    keyboard = [
        [InlineKeyboardButton("📖 Инструкция 📖", url=CHANNEL_URL)],
        [InlineKeyboardButton("🎰 Получить сигнал 🎰", web_app=WebAppInfo(url=WEB_APP_URL))],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    # Текст приветственного сообщения с HTML-разметкой
    text = ('<b>🎉 Добро пожаловать в наш telegram-бот!!!</b>'
            '\n\n‼️ Ребят, перед использованием софта <b>НАСТОЯТЕЛЬНО</b> рекомендуем прочитать <a href="https://t.me/RichFamilyWin/6">подробный мануал</a>, который ответит на все Ваши вопросы. '
            '<a href="https://t.me/RichFamilyWin/6">📲 Находится он в нашем канале</a>. Сэкономя 5 минут своего времени Вы рискуете потерять свои деньги.'
            '\n\n💪 Для тех, кто уверен в себе: Вам необходимо зарегистрировать новый аккаунт на <a href="https://1wqsg.com/casino/list?open=register&p=z5ki">🎰 1win</a>, используя исключительно эту ссылку ⬇️⬇️️️️'
            '\nhttps://1wqsg.com/casino/list?open=register&p=z5ki')

    # Открытие изображения для отправки
    photo = open('welcome_image.jpg', 'rb')

    # Отправка сообщения в зависимости от типа обновления (сообщение или callback-запрос)
    if update.message:
        await update.message.reply_photo(photo=photo, caption=text, parse_mode="HTML", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.reply_photo(photo=photo, caption=text, parse_mode="HTML", reply_markup=reply_markup)

# Асинхронная функция для обработки нажатий на кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Проверка, если callback-запрос связан с командой /start
    if query.data == 'start':
        await start(update, context)

if __name__ == '__main__':
    # Создание экземпляра приложения с использованием токена
    application = ApplicationBuilder().token(TOKEN).build()

    # Создание обработчиков для команды /start и нажатий на кнопки
    start_handler = CommandHandler('start', start)
    button_handler = CallbackQueryHandler(button)

    # Добавление обработчиков в приложение
    application.add_handler(start_handler)
    application.add_handler(button_handler)

    # Запуск приложения в режиме polling для обработки обновлений
    application.run_polling()
