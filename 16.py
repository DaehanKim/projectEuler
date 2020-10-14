import math
from tqdm import tqdm
from functools import reduce
from collections import Counter

num_dict = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
			6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten",
			11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
			15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 
			20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",
			80:"eighty", 90:"ninety", 100:"hundred"}

def read_num(num):
	if num == 1000 : return "one thousand"
	if num <= 20 : return num_dict[num]
	elif num // 100 == 0 : # 2-digit number
		return f"{num_dict[num // 10 * 10]} {num_dict[num%10]}"
	else:
		ret = "{} hundred and {}".format(num_dict[num // 100], read_num(num%100))
		if num % 100 == 0 : ret = ret.replace("and", "")
		return ret

# for i in range(1,1001):
# 	print("{:-4} --> {}".format(i, read_num(i)))
	# sum()

res = sum([len(read_num(i).replace(" ", "")) for i in range(1,1001)])
print(res)