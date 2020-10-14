class fiboGenerator:
	def __init__(self):
		self.idx = 0
		self.x1 = 1
		self.x2 = 2 

	def next(self):
		if self.idx == 0: 
			self.idx += 1
			return 1
		if self.idx == 1 : 
			self.idx += 1
			return 2
		ret = self.x1 + self.x2
		self.x1, self.x2 = self.x2, ret
		self.idx += 1
		return ret

g = fiboGenerator()

sum_ = 0
while(True):
	num = g.next()
	print(f"{g.idx} : {num}")
	if num % 2 != 0 : continue
	if num > 4000000: break
	print("added!")
	sum_ += num

print(sum_)