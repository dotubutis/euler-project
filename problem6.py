# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def problem6(n_range):
	result1 = 0
	for n in range(1, n_range):
		result1 += n**2
	print(result1)
	result2 = 0
	for n in range(1, n_range):
		result2 += n
	result2 = result2**2
	print(result2)

	result = result2 - result1
	return result

print(problem6(101))

