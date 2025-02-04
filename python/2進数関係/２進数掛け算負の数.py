import random
def Sintwo(n, bits=32):
    if n < 0:
        # 負の数の場合、2の補数を求める
        return bin((1 << bits) + n)[2:]
    return bin(n)[2:]

p=int(input("1つめの数"))
p1=int(input("2つめの数"))
#p=random.randint(0,255)
#p1=random.randint(0,255)
print(p,Sintwo(p))
print(p1,Sintwo(p1))
print(p1*p,Sintwo(p1*p))