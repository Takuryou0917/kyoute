import random
r={1: "R",2: "R'",3: "R2",4: "L",5: "L'",6: "L2",7: "U",8: "U'",9: "U2",10: "F",11: "F'",12: "F2",13: "D",14: "D'",15: "D2",16: "B",17: "B'",18: "B2"}
s=[]
for i in range(0,20):
    if i==0:
        s.append(r.get(random.randint(1,18)))
    elif i==1:
        while True:
            p=random.randint(1,18)
            if p%3==0:
                if s[i-1]==r.get(p) or s[i-1]==r.get(p-1) or s[i-1]==r.get(p-2):
                    continue
                else:
                    s.append(r.get(p))
                    break
            elif p%3==1:
                if s[i-1]==r.get(p) or s[i-1]==r.get(p+1) or s[i-1]==r.get(p+2):
                    continue
                else:
                    s.append(r.get(p))
                    break
            elif p%3==2:
                if s[i-1]==r.get(p) or s[i-1]==r.get(p+1) or s[i-1]==r.get(p-1):
                    continue
                else:
                    s.append(r.get(p))
                    break
    else:
        while True:
            p=random.randint(1,18)
            if p%3==0:
                if s[i-1]==r.get(p) or s[i-1]==r.get(p-1) or s[i-1]==r.get(p-2) or s[i-2]==r.get(p) or s[i-2]==r.get(p-1) or s[i-2]==r.get(p-2):
                    continue
                else:
                    s.append(r.get(p))
                    break
            elif p%3==1:
                if s[i-1]==r.get(p) or s[i-1]==r.get(p+1) or s[i-1]==r.get(p+2) or s[i-2]==r.get(p) or s[i-2]==r.get(p+1) or s[i-2]==r.get(p+2):
                    continue
                else:
                    s.append(r.get(p))
                    break
            elif p%3==2:
                if s[i-1]==r.get(p) or s[i-1]==r.get(p+1) or s[i-1]==r.get(p-1) or s[i-2]==r.get(p) or s[i-2]==r.get(p+1) or s[i-2]==r.get(p-1):
                    continue
                else:
                    s.append(r.get(p))
                    break
print("="*55)
print("")
print(' '.join(s))
print("")
print("="*55)