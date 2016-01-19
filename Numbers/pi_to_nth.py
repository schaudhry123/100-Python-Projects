import math

num_string = raw_input("How many decimals of pi? ")

num = int(num_string)

flag = False
# Keep checking input intil valid
while (not flag):
	if (num > 100):
		num_string = raw_input("Max is 100. Please enter a new number: ")
		num = int(num_string)
	elif (num <= 0):
		num_string = raw_input("Invalid input. Please enter a new number: ")
		num = int(num_string)
	else:
		flag = True

print "%.9f" % (math.pi)