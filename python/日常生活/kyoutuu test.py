print("="*20)
print("テストの教科(スペースあけて入力)")
s=["国 語","英 R ","英 L ","数1 A","数2BC","物 理","化 学","地 理","情 報"]
n=len(s)
t=[]
d={}
g=[0,0,0,0,0,0,0,0,0]
print("="*20)

for i in range(n):
    print(s[i],"の点数は？")
    tensu=input("→")
    t.append(str(tensu))
    print("="*20)

for i in range(n):
    u=0
    if t[i][0]=="g":
        t[i]=int(t[i].replace("g",""))
    else:
        for j in range(0,len(t[i])):
            u=u+int(t[i][j])
        t[i]=u

for i in range(n):
    if i ==0:
        g[i]=(t[i]/200)*100
    else:
        g[i]=(t[i]/100)*100

for i in range(n):
    d[g[i]]=s[i]
print("合計点は",sum(t),"点で",sep='')
print("平均点は",round((sum(t))/n,2),"点だよ",sep='')
print("="*20)
print("得点")

for i in range(n):
    print(s[i],"→",t[i],"点",sep='')
print("="*20)

print("点数率")
for i in range(n):
    if i==0:
        print(s[i]," → ",round((t[i])*100/200,1),"%",sep='')
    else:
        print(s[i]," → ",round((t[i])*100/100,1),"%",sep='')
print("="*20)