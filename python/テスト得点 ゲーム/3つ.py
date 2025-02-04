import random
while True:
    pw=str(input("パスワードを入力してください"))
    if pw!="1234":
        print("パスワードが違います")
        continue
    else:
        print("ログイン完了")
        break
situ="何のゲームをプレイしますか？","1:数の大小","2:余りの数","3:余りの数(1桁)","4:ゲーム終了"
while True:
    try:
        n=int(input(situ))
        if n==1:
            print("数当てゲーム大小ver","1~100の数字を当ててね！")
            k=random.randint(1,100)
            #print(k,"答え")
            while True:
                try:
                    i=int(input("あなたの値は？"))
                    if i<1 or i>100:
                        print("話を聞け")
                        continue
                    if i>k:
                        print(i,"は大きいよ")
                        print("="*20)
                    elif i<k:
                        print(i,"は小さいよ")
                        print("="*20)
                    else:
                        print(i,"は正解だよ！！！")
                        print("="*20)
                        break
                except ValueError:
                    print("文字ではなく数字を入力してください")
                    print("="*20)
        elif n==2:
            w=random.randint(50,100)
            #print(w,"答え")
            print("1~49 割った余りが表示","50~100 正誤判定")
            while True:
                try:
                    i=int(input("あなたの値は？"))
                    if i==w:
                        print(i,"は正解だよ！！！")
                        print("="*20)
                        break
                    elif i!=w and 50<=i<=100:
                        print("不正解だよ")
                        print("="*20)
                    elif i<1 or i>100:
                        print("話を聞け！")
                        print("="*20)
                        continue
                    elif 1<=i<=49:
                        k=w%i
                        print(k)
                        print("="*20)
                except ValueError:
                    print("文字ではなく数字を入力してください")
                    print("="*20)
        elif n==3:
            w1=random.randint(1,100)
            #print(w1,"答え")
            print("1~99の数を打ってね","出てきた数はあまりの数の1の位の数だよ")
            while True:
                try:
                    i=int(input("あなたの値は？"))
                    if i==w1:
                        print("正解だよ")
                        print("="*20)
                        break
                    elif i<1 or i>=100:
                        print("話を聞け")
                        print("="*20)
                        continue
                    elif 1<=i<=99:
                        k=w1%i
                        a=k%10
                        print(a)
                        print("="*20)
                except ValueError:
                    print("文字ではなく数字を入力してください")
                    print("="*20)
        elif n==4:
            print("おしまい")
            break
        elif n!=1 and n!=2 and n!=3 and n!=4:
            print("1~4の数字を入力してください")
    except ValueError:
        print("文字ではなく数字を入力してください")