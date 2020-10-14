def get_i_mult(i, limit):
	ret = []
	for j in range(1,limit): 
		if j%i ==0 : ret.append(j) 
	return ret

mult_3 = get_i_mult(3,1000)
mult_5 = get_i_mult(5,1000)

sum_ = sum(set(mult_3).union(mult_5))
print(sum_)