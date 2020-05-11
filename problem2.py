#Problem 2

fib_list = [1,2]
while fib_list[-1] < 4000000:
	fib_new = fib_list[-1] + fib_list[-2]
	fib_list.append(fib_new)

fib_list_even = []
for i in fib_list:
	if i%2==0:
		fib_list_even.append(i)

print(sum(fib_list_even))

