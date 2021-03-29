# 601. 偶數索引值加總
# 題目設計要求:
# 利用一維串列存放使用者輸入的12個正整數（範圍1~99）。
# 顯示這些數字，接著將串列索引為偶數的數字相加並輸出結果。
# Tips. 輸出每一個數字欄寬設定為3，每3個一列，靠右對齊
def numm():	
	x, num = [], 0
	for i in range(12):
		x.append(eval(input()))
		if i % 2 == 0: # 如果輸入到2倍數的次數時進行加總
			num += x[i] # 列表中抓出的偶數位加總 
	for i in range(12):
		print(f'{x[i]:3d}',end=' ')
		if(i+1) % 3 == 0: # 因為i不包含起始值,所以要要分3列時需要+1
			print()		
	print(num)


# 602. 撲克牌總和
# 題目設計要求:
# 輸入52張牌中的5張，計算並輸出其總和。
# Tips. J、Q、K以及A分別代表11、12、13以及1
def poker():
	p, num ={'J':'11','Q':'12','K':'13','A':'1'}, 0
	for i in range(5):
		x = input()
		if x in p:
			num += eval(p[x])
		else:
			num += eval(x)
	print(num)


# 603. 數字排序
# 題目設計要求:
# 輸入十個數字並存放在串列中。接著由大到小的順序顯示最大的3個數字。
def line1():
	line = []
	for i in range(10):
		line.append(eval(input()))
	line=sort(line)
	print(line[9], line[8], line[7])


# 604. 眾數
# 題目設計要求:
# 輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。
# Tips. 假設樣本中只有一個眾數
def many():
	line, nums = [], []
	for i in range(10):
		line.append(eval(input()))
		nums.append(line.count(line[i])) #紀錄輸入字元的出現次數至nums內
	print(line[nums.index(max(nums))])#將line套用索引nums當中出現次數最高的數字	
	print(max(nums))


# 605. 成績計算
# 題目設計要求:
# 輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。
# Tips. 平均值輸出到小數點後第二位
def score():
	g = []
	for i in range(10):
		g.append(eval(input()))
	g.remove(max(g))
	g.remove(min(g))
	print(sum(g))
	print(f'{(sum(g)/8:.2f}')


# 606. 二維串列行列數
# 題目設計要求:
# 輸入兩個正整數rows、cols，分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。
# 串列元素[row][col]所儲存的數字，
# 其規則為：row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。 
# 接著以該串列作為參數呼叫函式compute()輸出串列。
# Tips. 欄寬為4
# Example Input:4,7
def compute(rows, cols):
	for r in range(rows):
		for c in range(cols):
			print(f'{(c-r):4d}', end=' ')
		print()	


# 607. 成績計算
# 題目設計要求:
# 輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
# Tips. 平均分數輸出到小數點後第二位
# Tips. 先顯示學生順序後輸入(輸出:The 1st student: 然後輸入資料,依序進行)
def scores():
	info = ['The 1st student: ', 'The 2nd student: ', 'The 3rd student: ']
	scores = [[], [], []]
	for i in range(3):
		print(info[i])
		for j in range(5):
			scores[i].append(eval(input()))
	for i in range(3):
		print('Student %d' %(i+1))
		print('#Sum %d' % sum(scores[i]))
		print('#Average %.2f' % (sum(scores[i])/5))


# 608. 最大最小值索引
# 題目設計要求:
# 建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。
def N():
	N = []
	for i in range(9):
		N.append(eval(input()))
	largest = N.index(max(N))
	smallest = N.index(min(N))
	print("Index of the largest number %d is: (%d, %d)" % (max(N), largest//3, largest % 3))
	print("Index of the smallest number %d is: (%d, %d)" % (min(N), smallest//3, smallest % 3))


# 609. 矩陣相加
# 題目設計要求:
# 建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。
# Tips. 注意輸出格式
# Tips. 先顯示當前矩陣後輸入(輸出:[1, 2]: 然後輸入資料,依序進行)
def mix():
	s1=[0,0],[0,0]
	s2=[0,0],[0,0]
	print('Enter matrix 1:')
	for i in range(2):
		for j in range(2):
			s1[i][j] = eval(input('[%d, %d]:'%(i+1, j+1)))
	print('Enter matrix 2:')
	for i in range(2):
		for j in range(2):
			s2[i][j] = eval(input('[%d, %d]:'%(i+1, j+1)))
	print('Matrix 1:')
	for i in range(2):
		for j in range(2):
			print(s1[i][j], end = ' ')
		print()
	print('Matrix 2:')
	for i in range(2):
		for j in range(2):
			print(s2[i][j], end = ' ')
		print()
	print('Sum of 2 matrices:')
	for i in range(2):
		for j in range(2):
			print(s1[i][j]+s2[i][j], end = ' ')
		print()


# 610. 平均溫度
# 題目設計要求:
# 輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。
# Tips. 平均溫度輸出到小數點後第二位
# Tips. 最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1
# Tips. 先顯示當前天數後輸入(輸出:Day 1: 然後輸入資料,依序進行)
def tmp():
	t = []
	for i in range(4):
		print('Week %d:' % (i+1))
		for j in range(3):
			t.append(eval(input('Day %d:' % (j+1))))
	print('Average: %.2f' % (sum(t)/12))
	print('Highest: %.1f' % max(t))
	print('Lowest: %.1f' % min(t))



def main():
	# numm() # 601
	# poker() # 602
	# line1() # 603
	# many() # 604
	# score() # 605
	# compute(eval(input()), eval(input())) # 606
	# scores() # 607
	# N() # 608
	# mix() #609
	# tmp() # 610
main()
