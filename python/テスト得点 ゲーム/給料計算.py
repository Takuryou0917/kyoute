while True:
    print("給料を入力してください")
    s=input("→").split()
    n=len(s)
    k=0
    try:
        for i in range(0,n):
            k=k+int(s[i])
        print("合計金額"," ",k,"円")
        break
    except ValueError:
        print("すべて数字を入力してください")
if k>=1030000:
    print("103万円を超えています")
else:
    print("103万円を超えていません")