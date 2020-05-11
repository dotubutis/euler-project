# Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#1) Generate prime numbers up to the number 10000
import math 

prime_list = [2]
for num in range(3, 10000, 2):
	prime = True
	for i in range(2, int(math.sqrt(num))+1):
		if num%i==0:
			prime = False
	if prime:
		prime_list.append(num)

print(prime_list)

#2) Find  which of those numbers are prime factors of the number 600851475143
prime_factors = []
for i in prime_list:
	if 600851475143%i==0:
		prime_factors.append(i)

# Return largest prime factor
print(max(prime_factors))
