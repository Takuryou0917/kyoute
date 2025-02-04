print("="*20)
print("テストの教科(スペースあけて入力)")
s=["国 語","英 R ","英 L ","数1 A","数2BC","物 理","化 学","地 理","情 報"]
n=len(s)
t=[]
d={}
print("="*20)
for i in range(n):
    print(s[i],"の点数は？")
    tensu=input("→")
    t.append(str(tensu))
    print("="*20)

#　tの数をたくプログラムtにもどす
for i in range(n):
    u=0
    if t[i][0]=="g":
        t[i]=int(t[i].replace("g",""))
    else:
        for j in range(0,len(t[i])):
            u=u+int(t[i][j])
        t[i]=u
for i in range(n):
    print(s[i],t[i])
print("="*20)
for i in range(n):
    d[t[i]]=s[i]
print("合計点は",sum(t),"点で",sep='')
print("平均点は",(sum(t))/n,"点だよ",sep='')
print("="*20)
nt=sorted(t, reverse=True)
print("点数の高い順")
for i in range(n):
    if i==0:
        print(nt[i],"点","→",d[nt[i]],"  ","得点率"," ",int((nt[i]/200)*100),"%",sep='')
    else:
        print(nt[i],"点","→",d[nt[i]],"  ","得点率"," ",int((nt[i]/100)*100),"%",sep='')
print("="*20)