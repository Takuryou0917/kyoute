import time
import keyboard
import sys

def format_number(n):
    if 0 <= n < 61:
        return f"{n:02}"
    else:
        return str(n)

sys.stdout.write("\033[H\033[J")
sys.stdout.flush()

sentes=int(input("先手の持ち時間を入力してください(分)"))*60
gotes=int(input("後手の持ち時間を入力してください(分)"))*60

sys.stdout.write("\033[H\033[J")
sys.stdout.flush()

print("fで終了")
print("スペースキー　　　　　エンターキー")

teban=1
finish=1

while True:
        while teban==1:
            print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            sh=1
            while sh!=101:
                time.sleep(0.01)
                sh=sh+1
                if keyboard.is_pressed('space'):
                    teban=2
                    sentes=sentes+1
                    break
                if keyboard.is_pressed('f'):
                    sys.exit()
            sentes=sentes-1
            if sentes==0:
                print(f"\r▲先手 時間切れ    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sys.exit()

        while teban==2:
            print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            gh=1
            while gh!=101:
                time.sleep(0.01)
                gh=gh+1
                if keyboard.is_pressed('enter'):
                    teban=1
                    gotes=gotes+1
                    break
                if keyboard.is_pressed('f'):
                    sys.exit()
            gotes=gotes-1
            if gotes==0:
                print(f"\r先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 時間切れ", end='', flush=True)
                sys.exit()