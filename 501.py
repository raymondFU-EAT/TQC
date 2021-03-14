# 501. 訊息顯示
# 題目設計要求:
# 呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、
# 學號（Student ID）和姓名（Name）並顯示這些訊息。
def compute():
	print('Department: %s' % input())
	print('Student ID: %s' % input())
	print('Name: %s' % input())


# 502. 乘積
# 題目設計要求:
# 輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。
def com():
	x, y =(eval(input()), eval(input()))	
	def compute(x, y):	
		f = x*y
		return f
	f = compute(x, y) 
	print(f)


# 503. 連加計算
# 題目設計要求:
# 輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和。
def add():
	def compute():
		num = 0
		a, b = eval(input()), eval(input())
		for c in range(a, b+1):
			num += c

		return num
	num = compute()
	print(num)


# 504. 次方計算
# 題目設計要求:
# 輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳的值。
def ab():
	def compute():
		a, b = eval(input()), eval(input())
		print(a**b)
	compute()


# 505. 依參數格式化輸出
# 題目設計要求:
# 輸入三個參數，變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），
# 作為參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，總共印出y列。
# Tips. 輸出的每一個字元後方有一空格
def init():
	def compute():
		a, x, y = input(), eval(input()), eval(input())
		for i in range(y):
			print((a+' ')*x)	
	compute()	


# 506. 一元二次方程式
# 題目設計要求:
# 輸入三個整數（代表一元二次方程式 的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，
# 該函式回傳方程式的解，如無解則輸出【Your equation has no root.】
# Tips. 輸出有順序性
def val():
	def compute():
		a, b, c = eval(input()), eval(input()), eval(input())
		y = b**2-4*a*c
		x1, x2 = (-b+(y)**0.5)/(2*a), (-b-(y)**0.5)/(2*a)
		if y >= 0:
			print('%.1f,%.2f' % (x1, x2))
		else:
			print('Your equation has no root.')
	compute()


# 507. 質數
# 題目設計要求:
# 輸入一個整數x，並將x傳遞給名為compute()的函式，此函式將回傳x是否為質數（Prime number）的布林值，
# 接著再將判斷結果輸出。如輸入值為質數顯示【Prime】，否則顯示【Not Prime】。
def g():
	def compute():
		x = eval(input())
		if (x==1 or x<=0):
			return('Not Prime')
		for i in range(2, x):
			if(x % i == 0):
				return('Not Prime')
		return('Prime')
	print(compute())


# 508. 最大公因數
# 題目設計要求:
# 輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。
# Tips. 輸入包含逗點「,」
def max():	
	def compute(x,y):	
		if (x % y != 0):
			return compute(y, (x%y))#遞迴應用 這邊用遞迴來寫程式碼會較精簡
		else:
			return y
	x, y = map(eval, input().split(','))#由於輸入有包含逗點,需要用.split來切開數值 再用map去分配儲存的變數
	print(compute(x,y))


# 509. 最簡分數
# 題目設計要求:
# 輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），計算這兩個分數的和為p/q，
# 接著將p和q傳遞給名為compute()函式，此函式回傳p和q的最大公因數（Greatest Common Divisor, GCD）。
# 再將p和q各除以其最大公因數，最後輸出的結果必須以最簡分數表示。
# Tips. 輸入包含逗點「,」 
def mux():
	def compute(n1, n2):
		if n1 % n2 != 0:
			return compute(n2, n1%n2)
		else:
			return n2
	x, y = map(eval, input().split(','))
	m, n = map(eval, input().split(','))
	p, q =(x*n)+(m*y), y*n
	tem = compute(p, q)
	print('%d/%d + %d/%d = %d/%d' % (x, y, m, n, p/tem, q/tem))



# 510. 費氏數列
# 題目設計要求:
# 計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，
# 並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。
# Tips. 每個輸出數值後面都帶有一個空格
# Tips. 費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
def count():
	def compute(n):
		if n == 0 or n == 1:
			return n
		else:
			return compute(n-1)+compute(n-2)
	for i in range(eval(input())):
		print(compute(i), end =' ')


def main():

	# compute() # 501
	# com() # 502
	# add() # 503
	# ab() # 504
	# init() # 505
	# val() # 506
	# g() # 507
	# max() # 508
	mux() # 509
	count() # 510
main()