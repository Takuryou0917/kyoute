a=3
print(a==3) #aは３と等しい
print(a==2) #aは２と等しい
print(a!=3) #aは３と等しくない
print(a>=3) #aは３以上
print(a>3) #aは３より大きい
print(a<3) #aは３より小さい
print(a<=3) #aは３以下
print("="*20)
print("M" in "Minecraft")
print("O" in "Minecraft")
print("O" not in "Minecraft")
print("="*20)
print(a>2 and a<=10)
print(2<a<=10)
six = 6
pi=3.14
text="テキスト"
is_ok = True
print(type(six)) #int 整数
print(type(pi)) #float 実数
print(type(text)) #str 文字列
print(type(is_ok))#bool True or False
print("="*20)
three=3
print(three,type(three))
three_str=str(three) #int,strなどに認識を変える
print(three_str,type(three_str))
print(three==three_str)
print("="*10,"問題","="*10)
s="1,980円"
print(s)
s=s.replace(",","" ).replace("円","")
print(s)
s_int=int(s)
print(s_int,type(s_int))