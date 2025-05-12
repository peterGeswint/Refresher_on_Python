count = 0
while True:
	print(count)
	count += 1
	if(count >= 5):
		break

for x in range(10):
	if x % 2 == 0:
		continue
	print(x)

for letter in 'Durban':
	if letter == 'b':
		pass
		print ("this is a pass block")
	print('Current letter : '+ letter)

print("Goodbye !")
