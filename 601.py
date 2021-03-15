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
		print('%3d' % x[i],end=' ')
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
	line.sort(reverse=True)
	print(line[0], line[1], line[2])


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
	print('%.2f' %(sum(g)/8))



def main():
	numm() # 601
	poker() # 602
	line1() # 603
	many() # 604
	score() # 605