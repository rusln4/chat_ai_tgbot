import os
import sys
import subprocess
import time

def kill_old_instances():
    """Надежно завершает все старые процессы бота, используя pkill."""
    print("🔍 Проверка и завершение запущенных копий бота...")
    try:
        # pkill -f 'шаблон' находит и завершает все процессы, 
        # в командной строке которых есть 'шаблон'.
        # Это гораздо надежнее, чем ps | grep | awk | xargs kill.
        command = "pkill -f 'python3 src/main.py'"
        # Мы ожидаем, что команда может завершиться с ошибкой, если процессов не найдено.
        # Поэтому мы не проверяем код возврата (check=False).
        subprocess.run(command, shell=True, check=False)
        print("✅ Проверка завершена. Все старые процессы (если они были) остановлены.")
        time.sleep(1) # Короткая пауза для освобождения ресурсов
    except Exception as e:
        print(f"⚠️ Не удалось автоматически завершить старые процессы: {e}")

def run_bot():
    """Запускает бота с правильными настройками окружения."""
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.environ['PYTHONPATH'] = project_root
    
    print("\n🚀 Запускаю Иру...")
    print(f"📂 Корневая папка: {project_root}")
    
    try:
        subprocess.run([sys.executable, "src/main.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Бот остановлен пользователем.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Ошибка при запуске бота: {e}")
    except Exception as e:
        print(f"\n❌ Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    kill_old_instances()
    run_bot()
