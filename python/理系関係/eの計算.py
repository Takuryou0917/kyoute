import decimal as de
import mpmath as mp

de.getcontext().prec = 50

ei = de.Decimal(1).exp()
e=int(input("ネイピア数eの極限値の定義(無限に飛ばすとeになる)"))
e=(de.Decimal(1)+de.Decimal(1)/de.Decimal(e))**de.Decimal(e)
print("ネイピア数の極限での定義 有効数字50桁")
print(" ")
print("計 算 結 果",e)
print("ネイピア数 ",ei)
print(" 誤 差  ",abs(ei-e))