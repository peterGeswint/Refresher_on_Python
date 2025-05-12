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