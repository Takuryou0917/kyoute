import mpmath as mp
mp.mp.dps=50

f=(1 + mp.sqrt(5)) / 2
a=1
b=1
fi=int(input("黄金比の近似フィボナッチ数列で(無限に飛ばすと黄金比になる)"))

for i in range(1,fi+1):
    c=a+b
    a=b
    b=c
    print(f"\r{int((i/fi)*100)} %",end="")

o=mp.mpf(1)+mp.mpf(a)/mp.mpf(b)
print("フィボナッチ数列を用いた黄金比の計算 小数点以下50桁")
print(" ")
print("計算結果",o)
print("黄 金 比",f)
print(" 誤  差 ",abs(f-o))