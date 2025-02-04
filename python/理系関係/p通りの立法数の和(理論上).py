t=int(input("どの数までやりますか？"))+1
p=int(input("何通りの立法数の和で表せるやつを探しますか"))
print("")
count=0
t1=int(t**(1/3))+1
Ta=[]
for i in range(1,t):
    print(f"{(i/t):.1f}","%")
    count=0
    for j in range(1,t1):
        for k in range(1,t1):
            if j**3+k**3==i and j<=k:
                count=count+1
                if count==p:
                    for y in range(1,t1):
                        for x in range(1,t1):
                            if y**3+x**3==i and x>=y:
                                print(y,"^3","+",x,"^3","=",i)
                    Ta.append(i)
                    print(i,"は",p,"通りの立法数の和で表せる数です")
                    print("")
print(t-1,"以下の",p,"通り以上の立法数の和で表せる数一覧")
print(Ta)