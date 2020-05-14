#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import time

start_time = time.time()
for n in range(10, 300000000, 10):
	for m in range(1, 21):
		even_div = True
		if n%m!=0:
			even_div = False
			break
	if even_div:
		print(n)
		print("--- %s seconds ---" % (time.time() - start_time))
		break


