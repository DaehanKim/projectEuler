import math
# from itertools import combinations
from tqdm import tqdm


def is_prime(num):
	if num == 2 : return True
	for i in range(2, math.ceil(math.sqrt(num))+1):
		if num%i == 0 : return False
	return True

sum_ = 0 
for i in tqdm(range(2,2000000), total=2000000):
	if is_prime(i) : sum_ += i 
print(sum_)