import time
import keyboard

def display_time(seconds_remaining):
    minutes, seconds = divmod(seconds_remaining, 60)
    print(f"\r{minutes:02}:{seconds:02}", end='')

def main():
    total_seconds = 60
    start_time = time.time()

    while total_seconds > 0:
        if keyboard.is_pressed('space'):
            print("\nタイマーが停止しました。")
            break

        elapsed_time = time.time() - start_time
        total_seconds = max(0, 60 - int(elapsed_time))

        display_time(total_seconds)
        time.sleep(0.1)  # 0.1秒ごとにタイマーを更新

    if total_seconds == 0:
        print("\nタイマー終了")

if __name__ == "__main__":
    main()