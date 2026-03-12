# 🤖 Иру — Интеллектуальный ИИ-Ассистент

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-blue?style=for-the-badge&logo=telegram)
![AI](https://img.shields.io/badge/AI-Transformer-orange?style=for-the-badge)

**Иру** — это продвинутый Telegram-бот, построенный на базе современных нейросетевых архитектур (**Transformer**). Он умеет вести осмысленный диалог, понимать голосовые сообщения и анализировать эмоции пользователя.

---

## ✨ Ключевые особенности

- 🧠 **Умный диалог**: Работает на базе модели **Qwen2.5-72B** (через Hugging Face API).
- 📜 **Контекстная память**: Бот помнит историю разговора (последние 10 реплик).
- 🎙️ **Голосовой ввод**: Автоматическое распознавание речи (Speech-to-Text).
- 🎭 **Эмоциональный интеллект**: Анализ тональности текста и автоматические реакции эмодзи.
- 📂 **Архивация**: Полное логирование чатов и сохранение голосовых сообщений.
- 🏗️ **Модульная архитектура**: Чистый и расширяемый код.

---

## 🛠️ Стек технологий

- **Язык**: Python 3.9+
- **Интерфейс**: `pyTelegramBotAPI`
- **ИИ-ядро**: `Hugging Face Inference API` (Qwen2.5)
- **Звук**: `SpeechRecognition` (Google Engine), `SoundFile`
- **Безопасность**: `python-dotenv`

---

## 🚀 Быстрый запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/rusln4/chat_ai_tgbot.git
cd chat_ai_tgbot
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создайте файл `.env` в корне проекта и добавьте ваши токены:
```env
BOT_TOKEN=ваш_токен_телеграм_бота
DEEPSEEK_TOKEN=ваш_токен_hugging_face
```

### 4. Запуск
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 src/main.py
```

---

## 📁 Структура проекта

- `src/main.py` — Точка входа.
- `src/services/` — Логика ИИ и обработки голоса.
- `src/handlers/` — Обработчики команд Telegram.
- `src/config/` — Конфигурация проекта.
- `logs/` — История переписки.
- `data/voice_history/` — Архив голосовых сообщений.

---

## 👨‍💻 Автор
[rusln4](https://github.com/rusln4)

---
*Проект разработан для демонстрации возможностей современных LLM в мессенджерах.*
