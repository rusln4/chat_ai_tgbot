import os
import sys
import subprocess
import signal
import time

def kill_old_instances():
    """Завершает все старые процессы бота, чтобы избежать дублирования сообщений."""
    print("🔍 Проверка запущенных копий бота...")
    try:
        # Ищем процессы, в которых есть 'src/main.py'
        cmd = "ps aux | grep 'python3 src/main.py' | grep -v grep | awk '{print $2}'"
        pids = subprocess.check_output(cmd, shell=True).decode().split()
        
        if pids:
            print(f"🛑 Найдено {len(pids)} активных процессов. Завершаю их...")
            for pid in pids:
                try:
                    os.kill(int(pid), signal.SIGTERM)
                except ProcessLookupError:
                    pass
            time.sleep(1) # Ждем завершения
            print("✅ Все старые процессы завершены.")
        else:
            print("✅ Активных копий не найдено.")
    except Exception as e:
        print(f"⚠️ Не удалось автоматически завершить старые процессы: {e}")

def run_bot():
    """Запускает бота с правильными настройками окружения."""
    # Устанавливаем корневую директорию проекта в PYTHONPATH
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.environ['PYTHONPATH'] = project_root
    
    print("\n🚀 Запускаю Иру...")
    print(f"📂 Корневая папка: {project_root}")
    
    try:
        # Запускаем основной файл бота
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
