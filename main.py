import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

openai.api_key = 'your_api_key_here'

def generate_ai_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ошибка при генерации ответа: {e}"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, использующий ИИ для генерации ответов. Напиши мне что-нибудь!')
  
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    ai_response = generate_ai_response(user_message)
    update.message.reply_text(ai_response)

def main():
    updater = Updater("your_telegram_bot_token_here", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
