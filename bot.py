import logging
from telegram.ext import Application, CommandHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=== ЗАПУСК БОТА ===")

TOKEN = "8458816425:AAGW5r8Xa7W5FrjOwOztgLr3bHFJqi8HaLI"

async def start(update, context):
    await update.message.reply_text('🎉 Бот работает на Render!')

def main():
    print("Создаю приложение...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()
