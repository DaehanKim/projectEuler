import math
from tqdm import tqdm

res = []

def perm(inp, cur = []):
	if not inp :
		res.append(cur)
		return cur
	if len(inp) == 1 :
		return perm([], cur=cur + inp )
	for this in inp:
		# print("current : ",[item for item in inp if item != this])
		perm([item for item in inp if item != this] , cur=cur + [this])

perm(list("0123456789"))
print("".join(res[1000000-1]))

# from itertools import permutations

# for i permutations("0123456789",10)
