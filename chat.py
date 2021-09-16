def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:  # encoding =編碼 讀取寫入需相同
			for line in f:
				lines.append(line.strip()) #全部資料去除/n
					
	return lines

def convert(lines):
	new = []
	person = None  #以防第一個line不是人名
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue 
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person : #如果person有值才執行 
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)
main()