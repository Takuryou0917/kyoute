a=int(input("数字を入力してください"))
print("="*20)
print(int(a),end=",")
k=1
while True:
    if a==1:
        print(" ")
        print(int(k),"項")
        print("="*20)
        break
    elif a%2==0:
        a=a/2
        k=k+1
        print(int(a),end=",")
    else:
        a=a*3+1
        k=k+1
        print(int(a),end=",")