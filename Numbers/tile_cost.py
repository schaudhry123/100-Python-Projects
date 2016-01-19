def main():
	cost = float(raw_input("Enter the price of a tile: "))

	# Keep checking input intil valid
	flag = False
	while (not flag):
		if (cost <= 0):
			cost = float(raw_input("Invalid input. Please enter a new number: "))
		else:
			flag = True

	width = int(raw_input("Enter the width of the floor: "))
	length = int(raw_input("Enter the length of the floor: "))

	newcost = cost * width * length
	print "A %dx%d floor costs $%.2f" % (width, length, newcost)
	return

if __name__ == '__main__':
	main()