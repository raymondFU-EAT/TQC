# 201偶數判斷
def N():
	N = eval(input())
	if N % 2 == 0:
		print(N, 'is an even number.')
	else:
		print(N, 'is not an even number.')


# 202倍數判斷(先嚴3.5.後簡3.or5.)
def x():
	x = eval(input())
	if x % 3 == 0 and x % 5 == 0:
		print(x, 'is a multiple of 3 and 5.')
	elif x % 3 == 0:
		print(x, 'is a multiple of 3.')
	elif x % 5 == 0:
		print(x, 'is a multiple of 5.')

	else:
		print(x, 'is not a multiple of 3 or 5.')


# 203閏年判斷 
# 輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏。
def leap():
	leap = eval(input())
	if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0):
		print(leap, 'is a leap year.')

	else:
		print(leap, 'is not a leap year.')


# 204算術運算
# 輸入兩個整數a、b，然後再輸入一算術運算子【+、-、*、/、//、%】 ，輸出經過運算後的結果。
def fm():
	a ,b = (eval(input()), eval(input()))
	fm = input()
	if fm == '+':
		print(a+b)
	elif fm == '-':
		print(a-b)
	elif fm == '*':
		print(a*b)
	elif fm == '/':
		print(a/b)
	elif fm == '//':
		print(a//b)
	elif fm == '%':
		print(a%b)


# 205字元判斷
# 題目設計要求:
# 輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。
# Tips. 例如：a為英文字母、9為數字、$為其它字元。
def word():
	word = input()
	if word.isdigit(): # digit(數字)
		print(word,'is a number.')
	elif word.isalpha(): # alpha(字母)
		print(word,'is an alphabet.')
	else:
		print(word,'is a symbol.')


# 206等級判斷
# 題目設計要求:
# 根據輸入的分數顯示對應的等級。標準如下表所示：

# 分數	等級
# 80 ~ 100 A
# 70 ~ 79	B
# 60 ~ 69	C
# <= 59	F
def grade():
	grade = eval(input())
	if grade >= 80 and grade <= 100:
		print('A')
	elif grade >= 70 and grade <= 79:
		print('B')
	elif grade >= 60 and grade <= 69:
		print('C')
	else:
		print('F')


# 207折扣方案
# 題目設計要求:
# 輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。
# 購物金額折扣方案如下表所示：Tips. 輸出不需指定小數點位數

# 金額	折扣
# 8,000(含)以上	9.5折
# 18,000(含)以上	9折
# 28,000(含)以上	8折
# 38,000(含)以上	7折
def money():
	money = eval(input())
	if money >= 38000:
		print(money*0.7)
	elif money >= 28000:
		print(money*0.8)
	elif money >= 18000:
		print(money*0.9)
	elif money >= 8000:
		print(money*0.95)


# 208十進位換算
# 題目設計要求:
# 輸入一個十進位整數num （0 ≤ num ≤ 15），將num轉換成十六進位值。
# Tips. 轉換規則: 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F
def num():
	num = eval(input())
	if num < 10:
		print(num)
	elif num == 10:
		print('A')
	elif num == 11:
		print('B')
	elif num == 12:
		print('C')
	elif num == 13:
		print('D')
	elif num == 14:
		print('E')
	elif num == 15:
		print('F')


# 209距離判斷
# 題目設計要求:
# 輸入一個點的平面座標x和y值，判斷此點是否與點（5, 6）的距離小於或等於15，
# 如距離小於或等於15顯示【Inside】，反之顯示【Outside】。
def dis():
	x1, y1 = (5, 6)
	x2, y2 = (eval(input()), eval(input()))
	dis = ((5-x2)**2+(6-y2)**2)**0.5
	if dis <= 15:
		print('Inside')
	else:
		print('Outside')


# 210 三角形判斷
# 題目設計要求:
# 輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。
# 若可以，則輸出該三角形之周長；否則顯示【Invalid】。
# Tips. 檢查方法: 任意兩個邊長之總和大於第三邊長。
def line():
	x , y, z = (eval(input()), eval(input()),eval(input()))
	if x+y<z or y+z<x or x+z<y:
		print('Invalid')
	else:
		print(x+y+z)

def main():
	N()#201
	x()# 202
	leap()# 203
	fm()# 204
	word()# 205
	grade()# 206
	money()# 207
	num()# 208
	dis()# 209
	line()# 210
main()