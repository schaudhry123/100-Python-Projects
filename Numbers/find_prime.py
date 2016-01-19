def is_prime(num):
    return all(num % i for i in xrange(2, num))

def find_factors(num):
	factors = []
	for i in range(2, num):
		#print "%d" % i
		if (num % i == 0 and is_prime(i)):
			factors.append(i)
	return factors

def main():
	num = int(raw_input("Enter a number to find all of its prime factorizations: "))
	factors = find_factors(num)
	if factors:
		print str(factors).strip('[]')
	return 

if __name__ == '__main__':
	main()