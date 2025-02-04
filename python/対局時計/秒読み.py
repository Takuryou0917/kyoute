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
fi=int(input("秒読みの時間を入力してください(秒)"))
fic=fi
sentes=3
gotes=3
sys.stdout.write("\033[H\033[J")
sys.stdout.flush()

print("fで終了")
print("スペースキー　　　　　エンターキー")

teban=1

while True:
    while teban==1:
        sh=1
        if sentes==0 and gotes!=0: #先手だけ持ち時間なし
            print(f"\r▲先手 秒読み {fi}秒   後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            while sh!=101:
                time.sleep(0.01)
                sh=sh+1
                if keyboard.is_pressed('left shift'):
                    teban=2
                    fi=fic+1
                    break
                if keyboard.is_pressed('f'):
                    sys.exit()
            fi=fi-1
            if fi==0:
                print(f"\r▲先手 時間切れ    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sys.exit()
        elif sentes!=0 and gotes==0: #後手だけ持ち時間なし
            print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   後手 秒読み {fic}秒", end='', flush=True)
            while sh!=101:
                time.sleep(0.01)
                sh=sh+1
                if keyboard.is_pressed('left shift'):
                    teban=2
                    sentes=sentes+1
                    break
                if keyboard.is_pressed('f'):
                    sys.exit()
            sentes=sentes-1
        elif sentes==0 and gotes==0: #どっちも持ち時間なし
            print(f"\r▲先手 秒読み {fi}秒   後手 秒読み {fic}秒", end='', flush=True)
            while sh!=101:
                time.sleep(0.01)
                sh=sh+1
                if keyboard.is_pressed('left shift'):
                    teban=2
                    fi=fic+1
                    break
                if keyboard.is_pressed('f'):
                    sys.exit()
            fi=fi-1
            if fi==0:
                print(f"\r▲先手 時間切れ    後手 {fic}秒", end='', flush=True)
                sys.exit()
        else: #両方持ち時間あり
            print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
            while sh!=101:
                time.sleep(0.01)
                sh=sh+1
                if keyboard.is_pressed('left shift'):
                    teban=2
                    sentes=sentes+1
                    break
                if keyboard.is_pressed('f'):
                    sys.exit()
            sentes=sentes-1

        while teban==2:
            gh=1
            if gotes==0 and sentes!=0: #後手だけ持ち時間なし
                print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   後手 秒読み {fi}秒", end='', flush=True)
                while gh!=101:
                    time.sleep(0.01)
                    gh=gh+1
                    if keyboard.is_pressed('right shift'):
                        teban=1
                        fi=fic+1
                        break
                    if keyboard.is_pressed('f'):
                        sys.exit()
                fi=fi-1
                if fi==0:
                    print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 時間切れ", end='', flush=True)
                    sys.exit()
            elif gotes!=0 and sentes==0: #先手だけ持ち時間なし
                    print(f"\r▲先手 秒読み {fic}秒   後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                    while gh!=101:
                        time.sleep(0.01)
                        gh=gh+1
                        if keyboard.is_pressed('right shift'):
                            teban=1
                            gotes=gotes+1
                            break
                        if keyboard.is_pressed('f'):
                            sys.exit()
                    gotes=gotes-1
            elif sentes==0 and gotes==0: #どっちも持ち時間なし
                print(f"\r▲先手 秒読み {fic}秒   後手 秒読み {fi}秒", end='', flush=True)
                while gh!=101:
                    time.sleep(0.01)
                    gh=gh+1
                    if keyboard.is_pressed('right shift'):
                        teban=1
                        fi=fic+1
                        break
                    if keyboard.is_pressed('f'):
                        sys.exit()
                fi=fi-1
                if fi==0:
                    print(f"\r▲先手 秒読み {fic}秒    後手 時間切れ", end='', flush=True)
                    sys.exit()
            else: #両方持ち時間あり
                print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                while gh!=101:
                    time.sleep(0.01)
                    gh=gh+1
                    if keyboard.is_pressed('right shift'):
                        teban=1
                        gotes=gotes+1
                        break
                    if keyboard.is_pressed('f'):
                        sys.exit()
                gotes=gotes-1