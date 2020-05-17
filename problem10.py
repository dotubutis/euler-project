# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math 
import time

def is_prime(n):
    # return True if a num is prime number
    # otherwise return False
    # num type : int

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n%2==0:
    	raise ValueError('this function only checks odd numbers (except 2)')

    i = 3
    while (i * i <= n):
        if n % i == 0:
            return False
        i += 2
    return True

start_time = time.time()

prime_list = [2]
result = 0
for num in range(3, 2000001, 2):
	if is_prime(num):
		result += num

print("--- %s seconds ---" % (time.time() - start_time))
print(result)
