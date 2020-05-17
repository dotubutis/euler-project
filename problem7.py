# What is the 10 001st prime number?
import math 

def find_prime():
	prime_list = [2]
	for num in range(3, 110000, 2):
		prime = True
		for i in range(2, int(math.sqrt(num))+1):
			if num%i==0:
				prime = False
		if prime:
			prime_list.append(num)
	return prime_list

found_primes = find_prime()
print(len(found_primes))
print(found_primes)
print(found_primes[10000])