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

clear()
print("時間方式:[切れ負け→左SHIFT] [秒読み→SPACE] [フィッシャー→右SHIFT]")

while True:
    if keyboard.is_pressed('left shift'):

        print("切れ負け方式ロード中")
        time.sleep(1)

        clear()

        print("切れ負け方式")
        sentes=int(input("先手の持ち時間を入力してください(分)"))*60
        gotes=int(input("後手の持ち時間を入力してください(分)"))*60
        teban=1
        clear()

        print("切れ負け方式　fで終了")
        print(" ")
        print("左Shift　　　　　右Shift")

        while True:
            while teban==1:
                print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sh=1
                while sh!=11:
                    time.sleep(0.1)
                    sh=sh+1
                    if keyboard.is_pressed('left shift'):
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
                while gh!=11:
                    time.sleep(0.1)
                    gh=gh+1
                    if keyboard.is_pressed('right shift'):
                        teban=1
                        gotes=gotes+1
                        break
                    if keyboard.is_pressed('f'):
                        sys.exit()
                gotes=gotes-1
                if gotes==0:
                    print(f"\r先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 時間切れ", end='', flush=True)
                    sys.exit()

    elif keyboard.is_pressed('space'):
        print("秒読み方式をロード中")
        time.sleep(1)

        clear()

        print("秒読み方式")
        sentes=int(input("先手の持ち時間を入力してください(分)"))*60
        gotes=int(input("後手の持ち時間を入力してください(分)"))*60
        fi=int(input("秒読みの時間を入力してください(秒)"))
        fic=fi
        teban=1

        clear()

        print("秒読み方式　fで終了")
        print(" ")
        print("左Shift　　　　　右Shift")

        while True:
            while teban==1:
                sh=1
                if sentes==0 and gotes!=0: #先手だけ持ち時間なし
                    print(f"\r▲先手 秒読み {fi}秒   後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                    while sh!=11:
                        time.sleep(0.1)
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
                    while sh!=11:
                        time.sleep(0.1)
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
                    while sh!=11:
                        time.sleep(0.1)
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
                    while sh!=11:
                        time.sleep(0.1)
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
                    print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}  △後手 秒読み {fi}秒", end='', flush=True)
                    while gh!=11:
                        time.sleep(0.1)
                        gh=gh+1
                        if keyboard.is_pressed('right shift'):
                            teban=1
                            fi=fic+1
                            break
                        if keyboard.is_pressed('f'):
                            sys.exit()
                    fi=fi-1
                    if fi==0:
                        print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 時間切れ", end='', flush=True)
                        sys.exit()

                elif gotes!=0 and sentes==0: #先手だけ持ち時間なし
                        print(f"\r 先手 秒読み {fic}秒   △後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                        while gh!=11:
                            time.sleep(0.1)
                            gh=gh+1
                            if keyboard.is_pressed('right shift'):
                                teban=1
                                gotes=gotes+1
                                break
                            if keyboard.is_pressed('f'):
                                sys.exit()
                        gotes=gotes-1

                elif sentes==0 and gotes==0: #どっちも持ち時間なし
                    print(f"\r 先手 秒読み {fic}秒   △後手 秒読み {fi}秒", end='', flush=True)
                    while gh!=11:
                        time.sleep(0.1)
                        gh=gh+1
                        if keyboard.is_pressed('right shift'):
                            teban=1
                            fi=fic+1
                            break
                        if keyboard.is_pressed('f'):
                            sys.exit()
                    fi=fi-1
                    if fi==0:
                        print(f"\r 先手 秒読み {fic}秒   △後手 時間切れ", end='', flush=True)
                        sys.exit()

                else: #両方持ち時間あり
                    print(f"\r 先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                    while gh!=11:
                        time.sleep(0.1)
                        gh=gh+1
                        if keyboard.is_pressed('right shift'):
                            teban=1
                            gotes=gotes+1
                            break
                        if keyboard.is_pressed('f'):
                            sys.exit()
                    gotes=gotes-1

    elif keyboard.is_pressed('right shift'):
        print("フィッシャー方式をロード中")
        time.sleep(1)

        clear()
        print("フィッシャー方式")
        sentes=int(input("先手の持ち時間を入力してください(分)"))*60
        gotes=int(input("後手の持ち時間を入力してください(分)"))*60
        fi=int(input("一手ごとの追加時間[秒]"))+1
        teban=1

        clear()

        print("フィッシャー方式　fで終了")
        print("")
        print("左Shift　　　　　右Shift")

        while True:
            while teban==1:
                print(f"\r▲先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}    後手 {gotes//3600}:{format_number((gotes-(gotes//3600)*3600)//60)}:{format_number(gotes%60)}", end='', flush=True)
                sh=1
                while sh!=11:
                    time.sleep(0.1)
                    sh=sh+1
                    if keyboard.is_pressed('left shift'):
                        teban=2
                        sentes=sentes+fi
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
                while gh!=11:
                    time.sleep(0.1)
                    gh=gh+1
                    if keyboard.is_pressed('right shift'):
                        teban=1
                        gotes=gotes+fi
                        break
                    if keyboard.is_pressed('f'):
                        sys.exit()
                gotes=gotes-1
                if gotes==0:
                    print(f"\r先手 {sentes//3600}:{format_number((sentes-(sentes//3600)*3600)//60)}:{format_number(sentes%60)}   △後手 時間切れ", end='', flush=True)
                    sys.exit()