import time
import keyboard
import sys
import threading
stop_event = threading.Event()

def format_number(n): #１桁の整数を0?の形にする
    if 0 <= n < 61:
        return f"{n:02}"
    else:
        return str(n)

def kire_setting(a,b): #時間を秒にする
    global sentes,gotes
    sentes=a*60
    gotes=b*60

def clear(): #ターミナルリセット
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def sente_time():
    global sentes,gotes,teban
    while teban==1 and not stop_event.is_set():
        print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
        time.sleep(1)
        sentes=sentes-1
        if sentes<=0:
            print(f"\r▲先手 時間切れ    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            stop_event.set()

def gote_time():
    global sentes,gotes,teban
    while teban==2:
        print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
        time.sleep(1)
        gotes=gotes-1
        if gotes<=0:
            print(f"\r先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 時間切れ", end='', flush=True)
            stop_event.set()

sente_thread = threading.Thread(target=sente_time)
gote_thread = threading.Thread(target=gote_time)

def teban_fi(): #キーの入力認識
    global sentes,gotes,teban,sente_thread,gote_thread
    while not stop_event.is_set():
        if keyboard.is_pressed('Left shift') and teban == 1:
            if not sente_thread.is_alive():
                sente_thread = threading.Thread(target=sente_time)
                gote_thread = threading.Thread(target=gote_time)
                sente_thread.start()
            if  gote_thread.is_alive():
                sente_thread = threading.Thread(target=sente_time)
                gote_thread = threading.Thread(target=gote_time)
                gote_thread.join()
            time.sleep(1)
            teban = 2
        elif keyboard.is_pressed('Right shift') and teban == 2:
            if not gote_thread.is_alive():
                sente_thread = threading.Thread(target=sente_time)
                gote_thread = threading.Thread(target=gote_time)
                gote_thread.start()
            if sente_thread.is_alive():
                sente_thread = threading.Thread(target=sente_time)
                gote_thread = threading.Thread(target=gote_time)
                sente_thread.join()
            time.sleep(1)
            teban = 1
        elif keyboard.is_pressed('f'):
            stop_event.set()
            break

teban=1
clear()
kire_setting(int(input("先手")),int(input("後手")))
clear()

print("fで終了")
print("スペースキー　　　　　エンターキー")

teban_thread= threading.Thread(target=teban_fi)

teban_thread.start()
sente_thread.start()