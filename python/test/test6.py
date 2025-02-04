add=lambda a,b:a+b
try:
    r=add(1,"2")
    print(r)
except TypeError as e:
    print("エラー")
    print(e)
print("処理終了")
print("="*20)
add=lambda a,b:a+b #こっちのほうはエラーが起きないプログラムはelse以下に入れている
try:
    r=add(1,2)
except TypeError as e:
    print("エラー")
    print(e)
else:
    print(r)
finally:
    print("処理終了")

class Student(object):
    def say_hello(self,times):
        print("Hello"*times)
s=Student()
print(s.say_hello(3))