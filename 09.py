import math
from itertools import combinations
from tqdm import tqdm
# import time

# startT = time.time()

# for i in range(166167000):
# 	continue
# print(f"finished in {time.time() - startT}!")

for a,b,c in tqdm(combinations(range(1,1001), 3)):
	if (a+b+c) != 1000 : continue
	if a**2 + b**2 - c**2 == 0 : print(a*b*c)