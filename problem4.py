#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

word = '110011'
def palindrome(word):
	if word[0::] == word[::-1]:
		return True
	else: 
		return False

product_palindromes = []
for n in range(1, 1000):
	for m in range(1, 1000):
		product = n*m 
		if palindrome(str(product)) == True:
			product_palindromes.append(product)

print(max(product_palindromes))