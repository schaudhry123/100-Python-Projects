def reduce_by_num(n):
	

def main():
	cost = float(raw_input("Enter the cost: "))
	money_given = float(raw_input("Enter the amount of money given: "))

	while (money_given < cost):
		money_given = float(raw_input("Not enough money. Reenter amount of money given: "))

	price = 0
	tip = raw_input("Include tip? (y/n): ")
	if (tip == 'y'):
		tip_percent = raw_input("Enter percent tip: ")

		price = float(cost) * float(tip_percent) / 100

		print("Your tip is $%.2f" % price)

	diff = money_given - cost - price

	# Number of dollars
	# To-do: break up into $1, $5, $20
	dollars = 0
	while (diff >= 1):
		dollars += 1
		diff -= 1

	# Number of quarters
	quarters = 0
	while (diff >= 0.25):
		quarters += 1
		diff -= 0.25

	# Number of dimes
	dimes = 0
	while (diff >= 0.1):
		dimes += 1
		diff -= 0.1

	# Number of nickels
	nickels = 0
	while (diff >= 0.05):
		nickels += 1
		diff -= 0.05

	# Number of pennies
	pennies = 0
	while (diff >= 0.01):
		pennies += 1
		diff -= 0.01

	if (dollars != 0):
		print "Dollars: %d" % dollars
	if (quarters != 0):
		print "Quarters: %d" % quarters
	if (dimes != 0):
		print "Dimes: %d" % dimes
	if (nickels != 0):
		print "Nickels: %d" % nickels
	if (pennies != 0):
		print "Pennies: %d" % pennies

	return

if __name__ == '__main__':
	main()