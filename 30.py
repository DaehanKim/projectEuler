import math
from tqdm import tqdm
from collections import Counter

def get_power_sum(num):
	return sum([int(i)**5 for i in str(num)])

numbers = []
for num in tqdm(range(10,354295)):
	if num == get_power_sum(num) : 
		numbers.append(num)

# print(get_power_sum(132))
# print(get_power_sum(99999))

print(sum(numbers))
