print("="*20)
print("テストの教科(スペースあけて入力)")
s=input("→").split()
n=len(s)
t=[]
d={}
i=0
print("="*20)
while i!=n:
    try:
        print(s[i],"の点数は？")
        tensu=input("→")
        t.append(int(tensu))
        i=i+1
        print("="*20)
    except ValueError:
        print("数字を入力しろ")
for i in range(n):
    d[t[i]]=s[i]
print("合計点は",sum(t),"点で",sep='')
print("平均点は",(sum(t))/n,"点だよ",sep='')
print("="*20)
nt=sorted(t, reverse=True)
print("点数の高い順")
for i in range(n):
    print(nt[i],"点","→",d[nt[i]],sep='')
print("="*20)