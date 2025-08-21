import telebot

bot = telebot.TeleBot("your_telegram_bot_token")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! How can I assist you?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Example usage
bot.polling()
