import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    DEEPSEEK_TOKEN = os.getenv("DEEPSEEK_TOKEN") # Hugging Face Token
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    VOICE_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'VoiceData')
    LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
    VOICE_HISTORY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'voice_history')

    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN not found in .env")
        # Проверяем, что есть хотя бы один из ключей
        if not cls.DEEPSEEK_TOKEN and not cls.OPENROUTER_API_KEY:
            raise ValueError("Please set either DEEPSEEK_TOKEN (Hugging Face) or OPENROUTER_API_KEY in .env")
        os.makedirs(cls.VOICE_DATA_DIR, exist_ok=True)
        os.makedirs(cls.LOGS_DIR, exist_ok=True)
        os.makedirs(cls.VOICE_HISTORY_DIR, exist_ok=True)
