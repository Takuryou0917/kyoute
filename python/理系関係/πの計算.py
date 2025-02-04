import mpmath as mp
mp.mp.dps = 20

p=mp.pi
pii=mp.mpf(0)
pi=int(input("πのテイラー展開の分数の数(無限に飛ばすとπになる)大きすぎると重い"))

for i in range(1,pi+1):
    pii=mp.mpf(pii)+((mp.mpf(1)/mp.mpf(2*i-1))*(mp.mpf(-1))**(mp.mpf(i+1)))
    print(f"\r{int((i/pi)*100)} %",end="")

print("テイラー展開を用いたπの計算 小数点以下20桁")
print(" ")
print("計算結果",4*pii)
print("π の 値 ",p)
print(" 誤 差  ",abs(p-4*pii))