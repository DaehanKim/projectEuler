import math
from tqdm import tqdm
from functools import reduce


def level_digits(num_list):
	def is_flat(num_list):
		for item in num_list:
			if item // 10 != 0 : return False
		return True
	def add_space(num_list):
		amount = math.floor(math.log10(num_list[0]))
		return [0 for _ in range(amount)] + num_list

	ret = add_space(num_list)
	while(not is_flat(ret)):
		for i in range(1,len(ret)):
			try:
				ret[-i-1] += ret[-i]//10
				ret[-i] %= 10
			except IndexError:
				pass
		ret = add_space(ret)
	return ret


def str_mult(a,b):
	# a, b : string
	a_list = list(map(lambda x:int(x), a))
	b = int(b)

	a_times_b = [a_digit*b for a_digit in a_list]
	a_times_b = level_digits(a_times_b)
	return "".join([str(digit) for digit in a_times_b])



inp = "1"
for i in tqdm(range(2,101)):
	inp = str_mult(inp, str(i))
	# print(inp)

print(
	reduce(
		lambda x,y:x+y,
		map(lambda x:int(x),inp)
		)
	)