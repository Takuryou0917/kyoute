#リストは[]　タプルは（）　リストは要素の変更ができるがタプルは要素の変更ができない
mix=[1,"こんにちは",True,33]
print(type(mix))
print(mix[2])
print(mix[0:3])
print(mix)
for i in range(len(mix)):
    print(mix[i])
print("="*2)
for v in mix:
    print(v)
print("="*2)
for i , v in enumerate(mix):
    print(i,v)
print(1 in mix)
print(15 in mix)
m=[0]
print(m*10)
n =[1,2,3,4,5]
print(n)
n.append(6)
print(n)
n=[]
for i in range(5):
    n.append(i*3)
print(n)
print("="*2)
n1=[1,2,3,4,5]
n2=[6,7,8,9,10]
n1.extend(n2)
print(n1)
print(n2)
s=[]
for i in range(5):
    s.append(i)
print(s)
s
p=[i for i in range(6)]
print(p)
print("="*20)
#練習問題 nunbersから１０以上３０未満の値を抽出したリストを内包表記で
numbers=[20,58,19,4,29,31,5,1,39,13,30]
numbers1=[n for n in numbers if 10<=n<30]
print(numbers1)

t=(1,2,3)
print(t)
print(type(t)) #tupleはリストと違って中身の変更ができない
print(t[1])
print("="*40)
f={"apple":100,"banana":120}
print(f)
print(type(f))
print(f["apple"])
print(f["banana"])
f["banana"]=150
print(f["banana"])
f["peach"]=500
print(f)
print(f.keys())
for key in f.keys():
    print(key)
print(f.values())
for v in f.values():
    print(v)
for k , v in f.items():
    print(k,v)
print(f.get("apple"))#getでkeyを指定するとないkeyでもエラーが発生しない
print(f.get("grape"))
f2={"banana":200,"grape":300}
f.update(f2) #updateはkeyがある場合は更新keyがない場合は追加
print(f)
v=f.pop("apple")
print(v)
print(f) #popは中身を取り出して消す