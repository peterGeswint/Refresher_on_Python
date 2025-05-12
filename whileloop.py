number = int(input("Please enter a number to compare: "))
while number < 5:
	if (number % 2 == 0):
		print("The number "+ str(number) + " is even.")
	else:
		print("The number "+ str(number) + " is odd")

	number = number + 1
print("The loop is done.")


count = 0
while(count < 3):
	if count < 1:
		print("You are doing python.")
	elif count == 1:
		print("Welcome to regenesys.")
	elif count == 2:
		print("You are done !!")
	count = count + 1

print("Done")