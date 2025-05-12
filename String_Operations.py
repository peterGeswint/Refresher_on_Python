var1 = 'Hello lala !'
var2 = 'welcome to coding in python'

print("var[0]: " + var1[0])
print("var2[4:13]: "+ var2[4:13])

var1 = 'hello regenesys students !'
print("Updating String : - ",var1[:6] + "welcome")

count = 0
for letter in 'Regenesys':
	if(letter == 'e'):
		count += 1
print(count, 'Letters found.')

astring = "Peter Geswint!"
afewords = astring.split()
print(afewords[1])

input = "Regensys_for_learning_is_best"

#split initialization
split_string = input.split('_')
#output list initialise
output = []
#Iteration
for a in range(len(split_string)):
	temp = split_string[:a + 1]
	temp = "_".join(temp)
	output.append(temp)

#print output
print(output)



#input initialization
input_list = [1,3,4,5,6,7,8,9,10]
#output lists initialization
evenlist = []
oddlist = []
#list iteration
for num in input_list:
	#performing modulo operation
	if num % 2 == 0:
		#appending lists
		evenlist.append(num)
	else:
		#appending lists
		oddlist.append(num)
#displaying two lists
print("evenlist: ",evenlist)
print("oodlist: ", oddlist)
