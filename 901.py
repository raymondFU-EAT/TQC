# 901. 成績資料
# 題目設計要求:
# 輸入五筆資料寫入到write.txt（若不存在，則讓程式建立它），
# 每一筆資料為一行，包含學生名字和期末總分，以空白隔開。檔案寫入完成後要關閉。
def d901():
	with open('write.txt', 'w') as f:
		for i in range(5):
			f.write(input()+'\n')


# 902. 資料加總
# 題目設計要求:
# 讀取read.txt的內容（內容為數字，以空白分隔）並將這些數字加總後輸出。
# 檔案讀取完成後要關閉。
def d902():
	with open('read.txt', 'r', encoding='utf-8') as f:
		f = f.read().split()
		d = list(map(eval, f))
		print(sum(d))


# 903. 成績資料
# 題目設計要求:
# 輸入五個人的名字並加入到data.txt的尾端。之後再顯示此檔案的內容。
def d903():
	with open('data.txt', 'a')as f:
		for i in range(5):
			f.write('\n'+input())
	print('Append completed!')
	print('Content of "data.txt":')
	with open('data.txt', 'r')as f:
		print(f.read())
	

# 904. 資料計算
# 題目設計要求:
# 讀取read.txt（每一列的格式為名字和身高、體重，以空白分隔）並顯示檔案內容、
# 所有人的平均身高、平均體重以及最高者、最重者。
# Tips. 輸出浮點數到小數點後第二位
def d904():
	n, h, w = [], [], []
	with open('read.txt', 'r', encoding='utf-8') as f:
		for i in f:
			print(i)
			f = i.replace('\n', '').split(' ')
			n.append(f[0])
			h.append(eval(f[1]))
			w.append(eval(f[2]))
	print(f'Average height: {(sum(h)/len(h)):.2f}')
	print(f'Average weight: {(sum(w)/len(w)):.2f}')
	print(f'The tallest is {n[h.index(max(h))]} with {max(h):.2f}cm')
	print(f'The heaviest is {n[w.index(max(w))]} with {max(w):.2f}kg')


# 905. 字串資料刪除
# 題目設計要求:
# 輸入檔案名稱data.txt和一字串s，顯示該檔案的內容。接著刪除檔案中的字串s，
# 顯示刪除後的檔案內容並存檔。
def d905():
	d, s, n = input(), input(), []
	with open(d, 'r', encoding='utf-8') as f:
		n = f.read()

	print('=== Before the deletion')
	print(n)
	print('')
	n = n.replace(s, '')
	print('=== After the deletion')
	print(n)
	with open(d, 'w', encoding='utf-8') as f:
		f.write(n)


# 906. 字串資料取代
# 題目設計要求:
# 輸入檔名data.txt、字串s1和字串s2。程式將檔案中的字串s1以s2取代之。
def d906():
	d, s1, s2 = input(), input(), input()
	with open(d, 'r', encoding='utf-8') as f:
		f = f.read()
	print('=== Before the replacement')
	print(f)	
	print('=== After the replacement')
	print(f.replace(s1,s2))
	

# 907. 詳細資料顯示
# 題目設計要求:
# 輸入檔名read.txt，顯示該檔案的行數、單字數（簡單起見，單字以空白隔開即可，
# 忽略其它標點符號）以及字元數（不含空白）。
def d907():
	t = input()
	l, w, c =0, 0, 0
	with open(t, 'r', encoding='utf-8') as f:
		for i in f:
			l += 1
			ws = i.split(' ')
			w += len(ws)
			for i in range(len(ws)):
				c += len(ws[i])
	print(l, ' line(s)')
	print(w, ' word(s)')
	print(c, ' character(s)')


# 908. 單字次數計算
# 題目設計要求:
# 輸入檔名read.txt，以及檔案中某單字出現的次數。輸出符合次數的單字，
# 並依單字的第一個字母大小排序。（單字的判斷以空白隔開即可）
def d908():
	t, c = input(), eval(input())
	d, s = {}, []
	with open(t, 'r', encoding='utf-8') as f:
		f = f.read().replace('\n', '').split(' ')
	for i in f:
		d.update({i:f.count(i)})
	for i in d.keys():
		if d.get(i) == c:
			s.append(i)
	for i in sorted(i):
		print(i)


# 909. 聯絡人資料
# 題目設計要求:
# 輸入的五個人的資料寫入data.dat檔，每一個人的資料為姓名和電話號碼，以空白分隔。
# 再將檔案加以讀取並顯示檔案內容。
def d909():
	with open('data.dat', 'w', encoding='utf-8') as f:
		for i in range(5):
			f.write(input()+'\n')
	with open('data.dat', 'r', encoding='utf-8') as f:
		print('The content of "data.dat":')
		for i in f:
			print(i)


# 910. 學生基本資料
# 題目設計要求:
# 讀入read.dat（以UTF-8編碼格式讀取），第一列為欄位名稱，第二列之後是個人記錄。
# 請輸出檔案內容並顯示男生人數和女生人數（根據"性別"欄位，0為女性、1為男性）。
def d910():
	m, w = 0, 0
	with open('read.dat', 'r', encoding='utf-8') as f:
		for i in f:
			f =i.split(' ')
			if f[2] == '1':
				m+=1
			if f[2] == '0':
				w+=1
			print(i)
	print(f"Number of males: {m}")
	print(f"Number of females: {w}")   

	
# def main():
# 	d901()
# 	d902()
# 	d903()
# 	d904()
# 	d905()
# 	d906()
# 	d907()
# 	d908()
# 	d909()
# 	d910()
# main()
