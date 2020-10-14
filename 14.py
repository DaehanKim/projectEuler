import math
from tqdm import tqdm
from functools import reduce
from collections import Counter

def next_collatz_seq(num):
	if num%2==0 : return num//2
	return 3*num+1

def get_chain_length(num):
	cnt = 0
	res = num
	while(res!=1):
		res = next_collatz_seq(res)
		cnt += 1
	return cnt

# print(get_chain_length(13))

# LIM = 1000000
# chain_length_list = [0,0]
# for i in tqdm(range(2,LIM)):
# 	chain_length_list.append(get_chain_length(i))

# print(chain_length_list.index(max(chain_length_list)))
print(get_chain_length(837799))