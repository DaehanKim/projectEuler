import math
from tqdm import tqdm

exp = lambda x: 16*x**2 -28*x + 16

ans = 1
for n in range(2,502):
	ans += exp(n)
print(ans)