x=7
if x%15==0:
    print("FizzBuzz")
elif x%3==0:
    print("Fizz")
elif x%5==0:
    print("Buzz")
else:
    print(x)

x="Pyt"
if (n:=len(x))>3:
    print(n)
else:
    print("short")
print("="*2)
for i in range(5):
    print(i)
print("="*2)
for i in range(1,5):
    print(i)
print("="*2)
for i in range(1,5,2):
    print(i)
s="Python"
for i in range(len(s)):
    print(s[i])
print("="*2)
for a in s:
    print(a)
print("="*2)
i=0
while i<10:
    if i==5:
        break
    i=i+1
    print(i)
print("="*2)
for i in range(11): #５抜かしで文字列作成
    if i==5:
        continue
    print(i)
print("="*2)
for i in range(11): #５抜かしで文字列作成
    if i%3==0:
        continue
    print(i)
print("="*2)
c=3
match c:
    case 1:
        print("It is 1")
    case 2:
        print("iIT is 2")
    case _:
        print("Another")