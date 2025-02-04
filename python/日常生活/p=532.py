print("="*20)
print("テストの教科(スペースあけて入力)")
s=["国語","英語リーディング","英語リスニング","数学1A","数学2BC","物理","化学","地理","情報"]
n=len(s)
t=[]
d={}
print("="*20)
for i in range(n):
    print(s[i],"の点数は？")
    tensu=input("→")
    t.append(int(tensu))
    print("="*20)
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