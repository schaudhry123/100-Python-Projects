def fib_iteratively(n):
	num1 = 0
	num2 = 1
	for i in range(0, n):
		temp = num1 + num2
		num1 = num2
		num2 = temp
	return num2

def fib_recursively(n):
	if (n == 0 or n == 1):
		return 1
	return fib_recursively(n-1) + fib_recursively(n-2)

def main():
	num = int(raw_input("Enter a number to calculate its fibonacci: "))
	print "Iteratively: %d" % fib_iteratively(num)
	print "Recursively: %d" % fib_recursively(num)
	return

if __name__ == '__main__':
	main()