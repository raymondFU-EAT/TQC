# 401. 最小值
# 題目設計要求:
# 輸入十個數字，然後找出其最小值，最後輸出最小值。
def minf():
	n = []
	for num in range(10):
		n.append(eval(input()))		
	print(min(n))


# 402. 不定數迴圈-最小值
# 題目設計要求:
# 持續輸入數字，輸入的動作直到輸入值為9999才結束，然後找出其最小值，並輸出最小值。		
def minf1():
	n = []
	while True:
		num = eval(input())		
		if num == 9999:
			break
		n.append(num)
	print(min(n))


# 403. 倍數總和計算
# 題目設計要求:
# 輸入兩個正整數a、b（a<=b），
# 輸出從a到b（包含a和b）之間4或9的倍數（一列輸出十個數字、欄寬為4、靠左對齊）以及倍數之個數、總和。
def sum1():
	a, b = (eval(input()), eval(input()))
	count, add = 0, 0
	for num in range(a, b+1):
		if num % 4 == 0 or num % 9 == 0:
			print('%-4d' % num, end='')
			count += 1
			add += num
			if count % 10 == 0:
				print()
	print()
	print(count)
	print(add)		


# 404. 數字反轉判斷
# 題目設計要求:
# 輸入一個正整數，將此正整數以反轉的順序輸出，並判斷如輸入0，則輸出為0
def turn():	
	n = input()
	print(n[::-1])


# 405. 不定數迴圈-分數等級
# 題目設計要求:
# 以不定數迴圈的方式輸入一個正整數（代表分數），之後根據以下分數與GPA的對照表，
# 印出其所對應的GPA。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：
# Tips. 每輸入一次就輸出一次
def gpa():
	while True:
		n = eval(input())
		if 100>=n>=90:
			print('A')
		elif 89>=n>=80:
			print('B')
		elif 79>=n>=70:
			print('C')
		elif 69>=n>=60:
			print('D')
		elif 59>=n>=0:
			print('E')	
		elif n == -9999:
			break


# 406. 不定數迴圈-BMI計算
# 題目設計要求:
# 以不定數迴圈的方式輸入身高與體重，計算出BMI之後再根據以下對照表，
# 印出BMI及相對應的BMI代表意義（State）。假設此不定數迴圈輸入-9999則會結束此迴圈。標準如下表所示：
# Tips. BMI公式 = 體重公斤/(身高公尺*身高公尺)
# Tips. 輸出浮點數到小數點後第二位。 不需考慮男性或女性標準。
# Tips. 每輸入一次就輸出一次
def bmi1():
	while True:
		h, w = (eval(input()), eval(input()))
		if h == -9999 or w == -9999:
			break
		bmi = w/((h/100)*(h/100))
		print('BMI:%.2f ' % bmi)
		if bmi < 18.5:
			print('State: under weight')
		elif 18.5 <= bmi < 25:
			print('State: normal')	
		elif 25 <= bmi < 30:
			print('State: over weight')
		elif bmi >= 30:
			print('State: fat')


# 407. 不定數迴圈-閏年判斷
# 題目設計要求:
# 以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年（leap year）或平年。
# 其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。假設此不定數迴圈輸入-9999則會結束此迴圈。
# Tips. 每輸入一次就輸出一次
def leap():
	while True:
		year = eval(input())
		if year == -9999:
			break
		elif (year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
			print(year ,'is a leap year.')
		else:
			print(year ,'is not a leap year')


# 408. 奇偶數個數計算
# 題目設計要求:
# 輸入十個整數，計算並輸出偶數和奇數的個數。
def even():
	even, odd = 0, 0
	for num in range(10):
		num = eval(input())
		if num % 2 == 0:
			even += 1		
		else:
			odd += 1			
	print('Even numbers: ', even)
	print('Odd numbers: ', odd)


# 409. 得票數計算
# 題目設計要求:
# 某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，
# 輸入值如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號候選人投票，如輸入其他值則視為廢票。
# 每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；
# 如最終計算有相同的最高票數者或無法選出最高票者，顯示【=> No one won the election.】。
# Tips. 每次投完後需印出目前每位候選人的得票數
def vote():
	v1, v2, v3 = 0, 0, 0
	for i in range(5):
		num = eval(input())		
		if num == 1:
			v1 += 1			
		elif num == 2:
			v2 += 1
		else:
			v3 += 1
		print('Total votes of No.1: Nami = ', v1)
		print('Total votes of No.2: Chopper = ', v2)
		print('Total null votes = ', v3)
	if v1 == v2:
		print('=> No one won the election.')
	elif v1 > v2:
		print('No.1: Nami won the election.')
	else:
		print('No.2: Chopper won the election.')


# 410. 繪製等腰三角形
# 題目設計要求:
# 依照輸入的n，畫出對應層數的等腰三角形。
def tri():
	N = eval(input())
	star, space = 1, N-1
	for i in range(N):
		print(' '*space+'*'*star) #字串*次數
		star += 2 #星星每輪+2
		space -= 1 #空白每輪-1

def main():
	minf()# 401
	minf1()# 402
	sum1()# 403
	turn()# 404
	gpa()# 405
	bmi1()# 406
	leap()# 407
	even()# 408
	vote()# 409
	tri()# 410
main()
