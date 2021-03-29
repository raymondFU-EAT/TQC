# 301迴圈整數連加
# 題目設計要求:
# 輸入兩個正整數a、b（a < b），利用迴圈計算從a開始連加到b的總和。
# 例如：輸入a=1、b=100，則輸出結果為5050（1 + 2 + … + 100 = 5050）。
def sum():
	a, b = (eval(input()), eval(input()))
	sum = 0
	for i in range(a, b+1):
		sum += i
		
	print(sum)	


# 302迴圈偶數連加
# 題目設計要求:
# 輸入兩個正整數a、b（a < b），利用迴圈計算從a開始的偶數連加到b的總和。
# 例如：輸入a=1、b=100，則輸出結果為2550（2 + 4 + … + 100 = 2550）。
def even():
	a, b = (eval(input()), eval(input()))
	sum = 0
	for i in range(a, b+1):
		if i % 2 == 0:
			sum += i
	print(sum)		


# 303. 迴圈數值相乘
# 題目設計要求:
# 輸入一個正整數（<100），然後以三角形的方式依序輸出此數的相乘結果。
# Tips. 輸出欄寬為4，且需靠右對齊
def mix():
	N = eval(input())
	for i in range(1, N+1): #輸出要求從1開始輸出 所以我們初值設1,故N也必須+1 迴圈次數才會正確
		for j in range(1, i+1):
			print('%4d' % (i*j), end='')
		print('') #分行用 不然會全部擠一行


# 304. 迴圈倍數總和
# 題目設計要求:
# 輸入一個正整數a，利用迴圈計算從1到a之間，所有5之倍數數字總和。
def sum5():
	add = 0
	a = eval(input())
	for a in range(1, a+1):
		if a % 5 == 0:
			add += a
	print(add)


# 305. 數字反轉
# 題目設計要求:
# 輸入一個正整數，將此數值以反轉的順序輸出。	
def convert():
	n = input()  #因為是字串所以不用運算
	print(n[::-1])
	

# 306. 迴圈階乘計算
# 題目設計要求:
# 輸入一個正整數n，利用迴圈計算並輸出n!的值。
def i():
	num = 1
	n = eval(input())
	for i in range(1, n+1):
		num *= i
	print(num)


# 307. 乘法表
# 題目設計要求:
# 輸入一個正整數n（n<10），顯示n*n乘法表。
# 每項運算式需進行格式化排列整齊，
# 每個運算子及運算元輸出的欄寬為2，
# 而每項乘積輸出的欄寬為4，皆靠左對齊不跳行。
def mul():
	n = eval(input())
	for i in range(1, n+1):
		for j in range(1, n+1):
			print('%-2d%-2s%-2d%-2s%-4d' % (j, '*', i, '=', i*j), end = '')
		print('')


# 308. 迴圈位數加總
# 題目設計要求:
# 輸入一個數字，此數字代表後面測試資料的數量。
# 每一筆測試資料是一個正整數（由使用者輸入），將此正整數的每位數全部加總起來。
# Tips. 需每輸入一次資料就輸出一次結果
def sumall():
	n=[]
	for i in range(eval(input())):
		n=input()
		s=list(map(eval,n))
		print(n,sum(s))
	
		
	
	
# 309. 存款總額
# 題目設計要求:
# 輸入金額、年收益率，以及經過的月份數，接著顯示每個月的存款總額。
# Tips. 計算公式為: 存款+(存款*年收益率/12個月)=存款總額
# Tips. 請注意年收益率的輸入單位為"百分比",計算時需注意
# Tips. 下一個月的存款為上一個月之存款總額
def dep():
	money, rate, month = (eval(input()), eval(input()), eval(input()))	
	print('Month \t Amount')
	for i in range(month):
		print(f'{(i+1):3d} \t {(money+money*rate/1200):.2f}')
		money+=money*rate/1200
		


# 310. 迴圈公式計算
# 題目設計要求:
# 輸入正整數n (1 < n)，計算以下公式的總和並顯示結果：
# Tips. 輸出結果至小數點後四位
def n():
	n = eval(input())
	num = 0
	for i in range(2, n+1): # 從第二個數字開始
		num += 1/(((i-1)**0.5)+(i**0.5))
	print('%.4f' % num)

def main():
	sum()#301
	even()# 302
	mix()# 303
	sum5()# 304
	convert()# 305
	i()# 306
	mul()# 307
	sumall()# 308
	dep()# 309
	n()# 310
# main()
