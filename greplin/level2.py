from math import sqrt

def fib_larger(n):
	a, b = 0, 1
	while a <= n:
		a, b = b, a + b
	return a

def is_prime(n):
	if (n < 2):
		return False

	for x in range(2, int(sqrt(n))+1):
		if (n % x == 0):
			return False

	return True
	
def partA():
	str = input("Enter a number.")

	try:
		number = int(str)
	except ValueError:
		exit("Input must be a number.")

	found = False
	while (not found):
		number = fib_larger(number)
		found = is_prime(number)

	print(number)

def sum_prime_divisors(n):
	sum = 0
	for x in range(2, int(n/2)+1):
		if (n % x == 0 and is_prime(x)):
			sum += x
	return sum

def partB():
	x = 514229
	print(sum_prime_divisors(x + 1))

# partA()
partB()