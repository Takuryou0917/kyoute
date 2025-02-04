import random
atari=[]
for i in range(0,5,1):
    k=int(random.randint(1,100))
    atari.append(k)
print(atari)
m=int(input("くじ引き当たるかな？1~100の数字"))
j=0
for i in range(0,5):
    if m==atari[i]:
        print("あたり")
        j=1
        break
if j==0:
    print("はずれ")