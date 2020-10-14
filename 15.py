import math
from tqdm import tqdm
from functools import reduce
from collections import Counter

def get_sum_of_digit(inp):
	return reduce(lambda x,y :x+y,list(map(lambda x:int(x), inp)))

def times_two(num_str):
	orig = list(map(lambda x:int(x),num_str))
	# done = [item*2 for item in orig]
	ret = [0 for _ in range(len(orig))]
	if orig[0] >=5 : ret += [0]
	for i in range(1,len(orig)+1):
		ret[-i] += (2*orig[-i] % 10)
		if orig[-i] >= 5 : ret[-i-1] += 1
	return "".join(list(map(lambda x:str(x), ret)))

# print(times_two('124335421364235623642334'))  
inp = "1"
for _ in range(1000):
	inp = times_two(inp)

# print(inp)
print(get_sum_of_digit(inp))