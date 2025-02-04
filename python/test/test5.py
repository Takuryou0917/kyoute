n=[2,5,7,3,1]
print(sum(n))#合計
print(min(n))
print(max(n))
l=[2,5,7,3,1]
avg=sum(l)/len(l)
print(avg)
def say_hello():
    print("Hello")
say_hello()
def average(numbers):
    avg=sum(numbers)/len(numbers)
    return avg
n1=[5,4,3,5,67,4,67,]
n2=[5,7,4,2,4,7,8]
print(average(n))
print(average(n1))
print(average(n2))
a=average(n)
print(a)
print("="*40)
def hantei(x):
    if x%15==0:
        h="FizzBuzz"
    elif x%3==0:
        h="Fizz"
    elif x%5==0:
        h="Buzz"
    else:
        h=x
    return h
h1=hantei(3)
h2=hantei(5)
h3=hantei(30)
h4=hantei(49)
print(h1)
print(h2)
print(h3)
print(h4)
print("="*40)
def add (a,b):
    return a+b
add1=add(3,5)
print(add1)
def greet(name,message="Hello"):
    print(message,name,"!")
greet("Alice","Bye")
def waru(n):
    if n%2==0:
        return "偶数"
    else:
        return "奇数"
r1=waru(4)
r2=waru(5)
print(r1)
print(r2)
print("="*40)
my=lambda x: x if x%2==0 else "割り切れません"
m1=my(4)
m2=my(5)
print(m1)
print(m2)