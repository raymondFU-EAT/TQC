# 701. 串列數組轉換
# 題目設計要求:
# 輸入數個整數並儲存至串列中，以輸入-9999為結束點（串列中不包含-9999），
# 再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。
def d701():	
	n = []
	while True:
		x = eval(input())
		if x == -9999:
			break
		n.append(x)
	n = tuple(n)
	print(n)
	print('Length: %d' % len(n))
	print('Max: %d' % max(n))
	print('Min: %d' % min(n))
	print('Sum: %d' % sum(n))


# 702. 數組合併排序
# 題目設計要求:
# 輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。
# 將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。
def d702():
	n1, n2 = (), ()
	print('Create tuple1: ')
	while True:
		s = eval(input())
		if s == -9999:
			break
		n1 += (s,)

	print('Create tuple2: ')
	while True:
		s = eval(input())
		if s == -9999:
			break
		n2 += (s,)

	print('Combined tuple before sorting: ', n1+n2)
	print('Combined list after sorting: ', sorted(n1+n2))


# 703. 數組條件判斷
# 題目設計要求:
# 輸入一些字串至數組（至少輸入五個字串），以字串"end"為結束點（數組中不包含字串"end"）。
# 接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。
def d703():
	n = ()
	while True:
		s = input()
		if s == 'end':
			break
		n += (s,)
	print(n)
	print(n[:3])
	print(n[-3:])
	

# 704. 集合條件判斷
# 題目設計要求:
# 輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），
# 最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。
def d704():
	n = set()
	while True:
		tmp = eval(input())
		if tmp == -9999:
			break
			n.add(tmp)
	print('Length: ', len(n))
	print('Max: ', max(n))
	print('Min: ', min(n))
	print('Sum: ', sum(n))
	

# 705. 子集合與超集合
# 題目設計要求:
# 依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。
# 接著回答：set2是否為set1的子集合（subset）？ set3是否為set1的超集合（superset）？
# Tips. 依序分別輸入五個、三個、九個整數
def d705():
	s1, s2, s3 = set(), set(), set()
	print('Input to set1: ')
	for i in range(5):
		s1.add(eval(input()))

	print('Input to set2: ')
	for i in range(3):
		s2.add(eval(input()))

	print('Input to set3: ')
	for i in range(9):
		s3.add(eval(input()))

	print('set2 is subset of set1: ', s2<=s1)
	print('set3 is superset of set1: ', s3>=s1)


# 706. 全字母句
# 題目設計要求:
# 全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子。
# 輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，程式判斷該句子是否為Pangram，
# 並印出對應結果True（若是）或False（若不是）。
# Tips. 不區分大小寫字母
def d706():
	k = eval(input())
	for i in range(k):
		word = set(input().lower().replace(' ',''))
		print(len(word) == 26)


# 707. 共同科目
# 題目設計要求:
# 輸入X組和Y組各自的科目至集合中，以字串"end"作為結束點（集合中不包含字串"end"）。
# 請依序分行顯示:
# X組和Y組的所有科目
# X組和Y組的共同科目
# Y組有但X組沒有的科目
# X組和Y組彼此沒有的科目（不包含相同科目）
# Tips. 輸出科目依字母由小至大進行排序
def d707():
	x, y = set(), set()
	print("Enter group X's subjects:")	
	while True:
		tmp = input()
		if tmp == 'end':
			break
		x.add(tmp)

	print("Enter group Y's subjects:")	
	while True:
		tmp = input()
		if tmp == 'end':
			break
		y.add(tmp)

	print(sorted(x|y))
	print(sorted(x&y))
	print(sorted(y-x))
	print(sorted(x^y))


# 708. 詞典合併
# 題目設計要求:
# 自行輸入兩個詞典（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），將此兩詞典合併，
# 並根據key值字母由小到大排序輸出，如有重複key值，後輸入的key值將覆蓋前一key值。
# Tips. 重複輸入到key值為'end'時才跳出迴圈
def d708():
	d1, d2 = {}, {}
	print('Create dict1: ')
	while True:
		tmp = input('Key: ')
		if tmp == 'end':
			break
		d1[tmp] = input('Value: ')

	print('Create dict2: ')
	while True:
		tmp = input('Key: ')
		if tmp == 'end':
			break
		d2[tmp] = input('Value: ')

	d1.update(d2)
	for i in sorted(d1.keys()):
		print(f'{i}: {d1[i]}')
		

# 709. 詞典排序
# 題目設計要求:
# 輸入一顏色詞典color_dict（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），
# 再根據key值的字母由小到大排序並輸出。
def d709():
	d = {}
	while True:
		k = input('Key: ')
		if k == 'end':
			break
		d[k] = input('Value: ')
	for i in sorted(d.keys()):
		print(f'{i}: {d[i]}')
		


# 710. 詞典搜尋
# 題目設計要求:
# 為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），
# 再輸入一鍵值並檢視此鍵值是否存在於該詞典中。
def d710():
	d = {}
	while True:
		k = input('Key: ')
		if k == 'end':
			break
		d[k] = input('Value: ')
	print(input('Search key: ') in d)


def main():
	# d701() 
	# d702()
	# d703()
	# d704()
	# d705()
	# d706()
	# d707()
	# d708()
	# d709()
	# d710()
# main()
