import math
from tqdm import tqdm
from functools import reduce
from collections import Counter

with open('p067_triangle.txt','rt',encoding='utf8') as f:
	TRIANGLE = f.read().strip()

# print(TRIANGLE)


num_row = len(TRIANGLE.split('\n'))
triangle_lst = [[int(item) for item in row.split()] for row in TRIANGLE.split('\n')]
cache = [[-1 for _ in range(num_col)] for num_col in range(1,num_row+1)]

print(triangle_lst)


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

# for row in range(num_row)
# 	for col in range(row+1):
# 		# print(f"{row}, {col}")
# 		# if cache[row][col] == -1:
# 		get_max_sum(row,col) 

for i in range(num_row):
	get_max_sum(num_row-1,i)

# print(cache)
for row in cache:
	print(" ".join([str(item) for item in row]))

print(max(cache[-1]))
