import time
import keyboard
import sys

def format_number(n):
    if 0 <= n < 61:
        return f"{n:02}"
    else:
        return str(n)

def clear():
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

def moti_time(a,b):
    global sentes,gotes
    sentes=a*60
    gotes=b*60

def one_sec():
    global sentes,gotes,teban,fi,byo,byoc
    for i in range(1,11):
        time.sleep(0.1)
        if keyboard.is_pressed('left shift') and teban==1:
            teban=2
            byo=byoc
            if sentes!=0:
                sentes+=fi
            elif sentes==0:
                byo=byoc+1
            break
        if keyboard.is_pressed('right shift') and teban==2:
            teban=1
            byo=byoc
            if gotes!=0:
                gotes+=fi
            elif gotes==0:
                byo=byoc+1
            break
        if keyboard.is_pressed('f'):
            sys.exit()

clear()
print("切れ負け→左SHIFT 秒読み→SPACE フィッシャー→右SHIFT")
while True:
    if keyboard.is_pressed('left shift'):
        moti_time(int(input("先手の持ち時間を入力してください[分]")),int(input("後手の持ち時間を入力してください[分]")))
        byo=0
        fi=1
        setei=1
        break
    elif keyboard.is_pressed('space'):
        moti_time(int(input("先手の持ち時間を入力してください[分]")),int(input("後手の持ち時間を入力してください[分]")))
        byo=int(input("秒読みの時間を入力してください[秒]"))
        fi=1
        setei=2
        break
    elif keyboard.is_pressed('right shift'):
        moti_time(int(input("先手の持ち時間を入力してください[分]")),int(input("後手の持ち時間を入力してください[分]")))
        byo=0
        fi=int(input("一手ごとの追加時間[秒]"))+1
        setei=3
        break
clear()
if setei==1:
    print("切れ負け 先手→右SHIFT 後手→左SHIFT")
elif setei==2:
    print("秒読み 先手→右SHIFT 後手→左SHIFT")
elif setei==3:
    print("フィッシャー 先手→右SHIFT 後手→左SHIFT")
teban=1
byoc=byo
while True:
    if byo<=0 and teban==1:
                print(f"\r▲先手 時間切れ    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sys.exit()
    if byo<=0 and teban==2:
                print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    △後手 時間切れ", end='', flush=True)
                sys.exit()
    if teban==1:
        if sentes!=0 and gotes!=0:
            print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            one_sec()
            sentes-=1
        elif sentes!=0 and gotes==0:
            print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   後手 秒読み {byoc}秒", end='', flush=True)
            one_sec()
            sentes-=1
        elif sentes==0 and gotes!=0:
            print(f"\r▲先手 秒読み {byo}秒   後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            one_sec()
            byo-=1
            if byo<=0:
                print(f"\r▲先手 時間切れ    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sys.exit()
        else:
            print(f"\r▲先手 秒読み {byo}秒   後手 秒読み {byoc}秒", end='', flush=True)
            one_sec()
            byo-=1
            if byo<=0:
                print(f"\r▲先手 時間切れ    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sys.exit()
    if teban==2:
        if sentes!=0 and gotes!=0:
            print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            one_sec()
            gotes-=1
        elif sentes!=0 and gotes==0:
            print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 秒読み {byo}秒", end='', flush=True)
            one_sec()
            byo-=1
            if byo<=0:
                print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    △後手 時間切れ", end='', flush=True)
                sys.exit()
        elif sentes==0 and gotes!=0:
            print(f"\r 先手 秒読み {byoc}秒  △後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            one_sec()
            gotes-=1
        else:
            print(f"\r 先手 秒読み {byoc}秒  △後手 秒読み {byo}秒", end='', flush=True)
            one_sec()
            byo-=1
            if byo<=0:
                print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 時間切れ", end='', flush=True)
                sys.exit()