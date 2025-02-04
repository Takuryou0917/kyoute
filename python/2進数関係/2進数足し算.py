def Sintwo(n):
    if n < 0:
        raise ValueError("負の数はサポートされていません")
    return bin(n)[2:]
p=int(input("1つめの数"))
p1=int(input("2つめの数"))
print(p,Sintwo(p))
print(p1,Sintwo(p1))
print(p1+p,Sintwo(p1+p))