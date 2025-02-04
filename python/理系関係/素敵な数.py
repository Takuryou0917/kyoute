for i in range(100,1000):
    count=0
    count1=0
    p=str(i+2024)
    for j in range(len(p)):
        if p[j] in ("2","3","5","7"):
            count+=1
            decount=1
    if count==len(p):
        p=str(i-34)
        for y in range(len(p)):
            if p[y] in ("2","3","5","7"):
                count1+=1
    if count1==len(p):
        print(i)