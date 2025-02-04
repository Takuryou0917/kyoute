t=int(input("どの数までやりますか？"))+1
print("")
count=0
t1=int(t**(1/3))+1
Ta=[]
for i in range(1,t):
    count=0
    for j in range(1,t1):
        for k in range(1,t1):
            if j**3+k**3==i and j<=k:
                count=count+1
                if count==2:
                    for y in range(1,t1):
                        for x in range(1,t1):
                            if y**3+x**3==i and x>=y:
                                print(y,"^3","+",x,"^3","=",i)
                    Ta.append(i)
                    print(i,"は2通りの立法数の和で表せる数です")
                    print("")
print(t-1,"以下の2通りの立法数の和で表せる数一覧")
print(Ta)