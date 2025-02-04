import random
r=random.randint(1,100)
#print(r,"答え")
while True:
    try:
        i=int(input("あなたの値は？"))
        if i<1 or i>100:
            print("話を聞け")
            continue
        if i>r:
            print(i,"は大きいよ")
            print("="*20)
        elif i<r:
            print(i,"は小さいよ")
            print("="*20)
        else:
            print(i,"は正解だよ！！！")
            print("="*20)
            break
    except ValueError:
        print("文字ではなく数字を入力してください")