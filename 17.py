import math
from tqdm import tqdm
from functools import reduce
from collections import Counter

TRIANGLE = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

num_row = len(TRIANGLE.split('\n'))
triangle_lst = [[int(item) for item in row.split()] for row in TRIANGLE.split('\n')]
cache = [[-1 for _ in range(num_col)] for num_col in range(1,num_row+1)]


def get_max_sum(row, col):
	if cache[row][col] != -1 : return cache[row][col] # if cached
	if row == 0: # initial condition 
		cache[row][0] = triangle_lst[row][0]
		return get_max_sum(row,col)
	if col == row :
		cache[row][col] = get_max_sum(row-1, col-1) + triangle_lst[row][col] 
	elif col == 0 : 
		cache[row][col] = get_max_sum(row-1, col) + triangle_lst[row][col]
	else:
		cand_list = [get_max_sum(row-1,col)+triangle_lst[row][col], get_max_sum(row-1,col-1)+triangle_lst[row][col]]
		cache[row][col] = max(cand_list)
	return get_max_sum(row, col)

# for row in range(num_row):
# 	for col in range(row+1):
# 		# print(f"{row}, {col}")
# 		# if cache[row][col] == -1:
# 		get_max_sum(row,col) 

for i in range(15):
	get_max_sum(14,i)

print(cache)
for row in cache:
	print(" ".join([str(item) for item in row]))
# get_max_sum(row,col)

# for row in triangle_lst:
# 	print(" ".join([str(item) for item in row]))

