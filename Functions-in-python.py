def myfunction():
	s = 'Hello World from function'
	print(s)

print('Before function call')
myfunction()
print('After function call')

# defining a function
def plus(a,b):
	return a + b

# Create a sum class

class Summation(object):
	def sum(self,a,b):
		self.contents = a + b
		return self.contents
	

sumInstance = Summation()
sumInstance.sum(1,2)
print(sumInstance.contents)


def square(x):
	return x * x

square(5)

#lambda expression
add1 = lambda x,y: x + y
num = add1(5,6)
print(num)

# lambda expression
# to convert celsius to fahrenheit
c= [30,23,44,55,66,77,88,99]
f = list(map(lambda x: (float(9)/5)*(x + 32), c))
print(f)

# a funtion that returns a int and string.
def printInfo(nameandsurname, age):
	print("Name and Surname: ", nameandsurname)
	print("Age: ", age)
	return
printInfo("John Doe", 30)
