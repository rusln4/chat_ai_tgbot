import telebot
from telebot import types
import os
from dotenv import load_dotenv
import speech_recognition as sr
import soundfile as sf

# Загрузка переменных окружения
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

user_sessions = {}

def get_full_commands():
    return [
        types.BotCommand("/start", "Запустить бота"),
        types.BotCommand("/help", "Показать справку"),
        types.BotCommand("/exit", "Завершить работу")
    ]

def get_start_only():
    return [
        types.BotCommand("/start", "Запустить бота")
    ]

# Слушатели
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id

    bot.set_my_commands(
        get_full_commands(),
        scope=types.BotCommandScopeChat(chat_id)
    )
    user_sessions[message.from_user.id] = True
    bot.reply_to(message, "Приветствую, Я Иру! В любой момент ты можешь написать мне. Благодаря, мне  Помогу чем смогу!")

    bot.set_message_reaction(message.chat.id, message.message_id, [telebot.types.ReactionTypeEmoji('🤝')])


@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        """
<b>Команды бота:</b>

/start - Запустить бота
/help - Показать справку о командах
/exit - Завершить сессию

Просто напиши мне что-нибудь, и я отвечу!
        """
    )
    # parse_mode='HTML' для html команд
    bot.send_message(message.chat.id, help_text, parse_mode='HTML')


@bot.message_handler(commands=['exit'])
def exit_command(message):
    chat_id = message.chat.id

    if user_sessions.get(message.from_user.id) is False:
        bot.send_message(message.chat.id, "Я тебя впервые вижу, напиши /start, познакомимся 🙂")
        return
    
    user_sessions[message.from_user.id] = False
    bot.set_my_commands(
        get_start_only(),
        scope=types.BotCommandScopeChat(chat_id)
    )
    bot.send_message(message.chat.id, "До связи! Если я снова понадоблюсь, напиши /start")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if user_sessions.get(message.from_user.id) is False:
        bot.send_message(message.chat.id, "Я тебя впервые вижу. Напиши /start, познакомимся 🙂")
        return
    if message.text == "Справка":
        help_command(message)
    elif message.text == "Выход":
        exit_command(message)
    else:
        bot.send_message(message.chat.id, "Я пока только учусь понимать обычный текст. Попробуй меню!")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    # Скачивание голосового сообщения
    file_info = bot.get_file(message.voice.file_id)
    downloaded_voice = bot.download_file(file_info.file_path)

    with open(os.path.join(os.path., '\\..\\VoiceData\\voice.ogg'), 'wb') as voice:
        voice.write(downloaded_voice)

    # Конвертация файла
    # data, samplerate = sf.read('voice.ogg')
    # sf.write('wav_voice.wav', data, samplerate)

    # recognizer = sr.Recognizer()
    # with sr.AudioFile('wav_voice.wav') as file:
    #     audio_data = recognizer.record(file)
    #     try:
    #         text = recognizer.recognize_bing(audio_data, language="ru-RU")
    #         bot.reply_to(message, f"Вы сказали: {text}")
    #     except:
    #         bot.reply_to(message, f"Я не совсем понял, что вы сказали")
 
bot.set_my_commands([
    types.BotCommand("/start", "Запустить бота"),
    types.BotCommand("/help", "Показать справку"),
    types.BotCommand("/exit", "Завершить работу")
])

# Запуск бота
bot.infinity_polling(timeout=5)