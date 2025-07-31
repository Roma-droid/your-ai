import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin  # Импортируем функции из bot_logic
from config import token
from ai_logic import get_calss
# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye,")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")


@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(content_types=['photo'])
def get_calss_on_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open('images/'+file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id ,text="Сохранено Пожалуйста подождите")
    class_name, score = get_calss('images/'+file_name)
    if class_name == "Неро" and score > 0.9:
        bot.send_message(message.chat.id, text="Это неросеть остирегайтесь")
    elif class_name == "Котики" and score > 0.9:
        bot.send_message(message.chat.id, text="Это настоящий кот")
    else:
        bot.send_message(message.chat.id, text="Я незнаю что это")

# Запускаем бота
bot.polling()