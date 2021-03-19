# 801. 字串索引
# 題目設計要求:
# 輸入一字串，顯示該字串每個字元的索引。
def d801():
	s = input()
	for i in range(len(s)):
		print(f"Index of '{len(s)}': {i}")


# 802. 字元對應
# 題目設計要求:
# 輸入一字串，顯示該字串每個字元的對應ASCII碼及其總和。
def d802():
	d, s = input(), 0
	for i in d:
		print(f"ASCII code for '{i}' is {ord(i)}")
		s += ord(i)
	print(s)
	
	
# 803. 倒數三個詞
# 題目設計要求:
# 輸入一個句子（至少有五個詞，以空白隔開），並輸出該句子倒數三個詞。
def d803():
	s = input().split(' ')
	print(f'{s[-3]} {s[-2]} {s[-1]}')


# 804. 大寫轉換
# 題目設計要求:
# 輸入一字串，分別將該字串轉換成全部大寫以及每個字的第一個字母大寫。
def d804():
	s = input()
	print(f'{s.upper()}')
	print(f'{s.title()}')


# 805. 字串輸出
# 題目設計要求:
# 輸入一個長度為6的字串，將此字串分別置於10個欄位的寬度的左邊、中間和右邊，
# 並顯示這三個結果，左右皆以直線「|」（Vertical bar）作為邊界。
def d805():
	s = input()
	print(f'|{s:<10s}|')
	print(f'|{s:^10s}|')
	print(f'|{s:>10s}|')


# 806. 字元次數計算
# 題目設計要求:
# 輸入一字串和一字元，並將此字串及字元作為參數傳遞給名為compute()的函式，
# 此函式將回傳該字串中指定字元出現的次數，接著再輸出結果。
def d806():
	def compute(word, w):
		print(f'{w} occurs {word.count(w)} time(s)')
	compute(input(), input())


# 807. 字串加總
# 題目設計要求:
# 輸入一字串，該字串為五個數字，以空白隔開。請將此五個數字加總（Total）並計算平均（Average）。
def d807():
	n = list(map(int, input().split(' ')))
	print(f'Total = {sum(n):1d}')
	print(f'Average = {(sum(n)/len(n)):.1f}')


# 808. 社會安全碼
# 題目設計要求:
# 輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。若格式完全符合（正確的SSN）
# 則顯示【Valid SSN】，否則顯示【Invalid SSN】。
def d808():
	n = input().replace('-', '')
	if n.isdigit():
		print('Valid SSN')
	else:
		print('Invalid SSN')


# 809. 密碼規則
# 題目設計要求:
# 輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
# 必須至少八個字元。
# 只包含英文字母和數字。
# 至少要有一個大寫英文字母。
# 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】。
def d809():
	n = input()
	if (len(n)>=8 and n.isalnum()==True and n.islower()==False):
		print('Valid password')
	else:
		print('Invalid password')


# 810. 最大值與最小值之差
# 題目設計要求:
# 首先輸入正整數k（1 <= k <= 100），代表有k筆測試資料。每一筆測試資料是一串數字，
# 每個數字之間以一空白區隔，請找出此串列數字中最大值和最小值之間的差。
# Tips. 差值輸出到小數點後第二位。
def d810():
	k = eval(input())
	for i in range(k):
		n = list(map(eval, input().split(' ')))
		print(f'{(max(n)-min(n)):.2f}')


def main():
	d801()
	d802()
	d803()
	d804()
	d805()
	d806()
	d807()
	d808()
	d809()
	d810()
# main()
