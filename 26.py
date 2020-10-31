import math
from tqdm import tqdm

def is_divisible(a, b):
	# a, b : string
	# returns True if a is divisible by b else false
    if len(a) <= len(b) + 1:
    	# exit condition
    	if int(a) % int(b) == 0 : return True
    	return False
    res = int(a[:len(b)+1]) % int(b)
    new_a = str(res)+a[len(b)+1:]
    return is_divisible(new_a,b)

def remove_10(inp):
	ret = inp
	while(ret % 2 == 0):
		ret //= 2
	while(ret % 5 == 0):
		ret //= 5
	return ret

def num_recurring_cycle(inp):
	inp = remove_10(inp)
	if inp == 1 : return 0
	cnt = 1
	while(True):
		if is_divisible("9"*cnt,str(inp)) : break
		cnt += 1
	return cnt

rec_list = [num_recurring_cycle(num) for num in tqdm(range(1,1001))]
print(rec_list)
print(max(rec_list))
print(rec_list.index(max(rec_list))+1)