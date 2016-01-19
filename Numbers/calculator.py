def get_operation():
	while (True):
		op = raw_input("Enter the operation: ")
		if (op != '+' and op != '-' and op != '*' and op != '/' and op != 'q' and op != '^'):
			print "Invalid operation"
		else:
			return op

# Any checks needed for numberi nput
# Whether the input is a number -- what does int() return
def get_num(n):
	if (n == 1):
		num = float(raw_input("Enter the 1st number: "))
	else:
		num = float(raw_input("Enter the 2nd number: "))
	return num

# Do the actual calculation and return the result
def calculate(op, num1, num2):
	if (op == '+'):
		return num1 + num2
	elif (op == '-'):
		return num1 - num2
	elif (op == '*'):
		return num1 * num2
	elif (op == '/'):
		return num1 / num2
	elif (op == '^'):
		return num1 ** num2
	else:
		print "Invalid operation"
		return

def main():
	print "Welcome to my calculator!"
	print "This calculator currently supports basic arithmetic operations."
	print "Enter what operation first, then each number. One line at a time"
	print "+ add, - subtract, * multiply, / divide, ^ raise to power, q quit"

	# Get the inputs
	flag = False
	while (not flag):
		op = get_operation()
		if (op == 'q'):
			flag = True
		else:
			num1 = get_num(1)
			num2 = get_num(2)

			print "==> %.2f" % calculate(op, num1, num2)

	print "Thank you for using my calculator!"
	return


if __name__ == '__main__':
	main()