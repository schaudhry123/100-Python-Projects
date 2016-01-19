meal_price = raw_input("Enter the price of your meal: ")

tip_percent = raw_input("Enter percent tip: ")

price = float(meal_price) * float(tip_percent) / 100

print("Your tip is $%.2f" % price)