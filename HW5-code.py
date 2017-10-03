import re
import operator

fh = open('actual-data.txt')
sum_list = []
for line in fh:
	line = line.strip()
	nums_in_line = re.findall('[0-9]+',line)
	for num in nums_in_line:
		sum_list.append(int(num))
print(sum(sum_list))