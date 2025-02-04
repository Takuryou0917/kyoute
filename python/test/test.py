a=3
b=-6
plus = a + b #足し算
minus=a-b #引き算
multiply=a*b #掛け算
divide=a/b #割り算
print(plus, minus, multiply, divide) #printで表示
print("あってますか？") #文字は""に入れる
s="Minecraft" #変数の時も
print(s)
print(s[3]) #文字指定 0 1 2 3 前から[]で囲う
print(s[0:3]) #前の０はなくても最初からの意味。後ろは終わり+１
print(s[-1])  #後ろから数えたかったら-?を使う
c="kjgbklhKGLjbsldkjbgjaa"
print(len(c))
print("="*10,"足し算","="*10)
print(a+b)
print("="*10,"掛け算","="*10)
print(a*b)
print(c.index("gb"))
print(c.find("gb"))
print(s.replace("Mine","Your"))