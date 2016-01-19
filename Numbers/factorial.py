def fact_iteratively(n):
	num = 1
	for i in range(1, n+1):
		num *= i
	return num

def fact_recursively(n):
	if (n == 0):
		return 1
	return n * fact_recursively(n-1)

def main():
	# Read in number to calculate factorial of
	num = int(raw_input("Enter a number to calculate the factorial of: "))
	print "Iteratively: %d" % fact_iteratively(num)
	print "Recursively: %d" % fact_recursively(num)
	return

if __name__ == '__main__':
	main()