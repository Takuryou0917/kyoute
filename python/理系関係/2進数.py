def Sinsu(n):
    k=0
    while True:
        if n<=2**k:
            result=[0]*(k)
            break
        else:
            k=k+1
    while True:
        if k<0:
            break
        elif n>=2**k:
            n=n-2**k
            result[k]=1
            k=k-1
        elif n<2**k:
            k=k-1
    return result


s=int(input("２進数に変換"))
l=str(Sinsu(s))
print(s,"  ",l.replace("[","").replace("]","").replace(",",""))