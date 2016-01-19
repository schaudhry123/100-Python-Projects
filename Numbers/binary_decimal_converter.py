def binary_to_decimal(n):
	return int(n, 2)

def decimal_to_binary(n):
	return bin(n)[2:]

def main():
	print "Binary-Decimal Converter"
	flag = False
	while (not flag):
		converter = raw_input("Enter b for binary input or d for decimal input (q to quit): ")
		if (converter == 'b'):
			num = raw_input("Enter the binary number: ")
			print "==> %d" % binary_to_decimal(num)
		elif (converter == 'd'):
			num = int(raw_input("Enter the decimal number: "))
			print "==> %s" % decimal_to_binary(num)
		elif (converter == 'q'):
			flag = True
		else:
			print "Invalid input"
	return

if __name__ == '__main__':
	main()