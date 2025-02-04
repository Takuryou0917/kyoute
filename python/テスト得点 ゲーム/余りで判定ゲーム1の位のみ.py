import random
r=random.randint(1,100)
#print(r,"答え")
print("1~99の数を打て","出てきた数はあまりの数の1の位の数だ")
while True:
    try:
        i=int(input("あなたの値は？"))
        if i==r:
            print("正解")
            break
        elif i<1 or i>=100:
            print("話を聞け")
            print("="*20)
            continue
        elif 1<=i<=99:
            k=r%i
            a=k%10
            print(a)
    except ValueError:
        print("文字ではなく数字を入力してください")