import random
r=random.randint(50,100)
#print(r,"答え")
print("1~49 割った余りが表示","50~100 正誤判定")
while True:
    try:
        i=int(input("あなたの値は？"))
        if i==r:
            print("正解")
            break
        elif i!=r and 50<=i<=100:
            print("不正解")
        elif i<1 or i>100:
            print("話を聞け")
            continue
        elif 1<=i<=49:
            k=r%i
            print(k)
    except ValueError:
        print("文字ではなく数字を入力してください")