# A class is a  blue print for objects - one class for many objects of that type.
# To define a class in python we use the class keyword. This is like we use def to define a function.
# To access the members of a Python class we use the dot operator.

class Test:
	def fun(self):
		print("Hello World from class method")
	
	def addition(self, a, b):
		return a + b

obj = Test()
obj.fun()
obj.addition(5, 10)

# Instance variables are variables whose value is assigned inside a constructor or method with self keyword.
# Class variables are variables whose value is assigned in class.

class Teacher:
	# Class variable
	subject = "Life Sciences"

	# The init method or constructor 
	def __init__(self,fullname, YearOfBirth):
		# Instance variables
		self.fullname = fullname
		self.YearOfBirth = YearOfBirth

x = Teacher("John Doe", 1985)
print(x.fullname)
print(x.YearOfBirth)
print(x.subject)  # Accessing class variable

# we can also crearte instance variables inside methods.
class Lecturer:
	# class variable
	module = "Cyber Security"

	# The init method or constructor
	def __init__(self, NumberOfStudents):
		# Instance variable
		self.NumberOfStudents = NumberOfStudents

		# adds an instance variable 
	def setlectureHall(self, hall):
		self.hall = hall

		# Retieve lecture hall
	def getLectureHall(self):
		return self.hall
		
# DriverCode 
s = Lecturer(50)
s.setlectureHall("Room 101")
print(s.getLectureHall())
# Accessing class variable
print(s.module)  
# Accessing instance variable
print(s.NumberOfStudents)

#Hidden variables and their access

# In python we use double underscore (__) to hide a variable.
# I will try to access a hiiden variable and see what happens.

class MyClass:
	# Hidden member of my class
	__hiddenVariable = 0

	# A member method that changes __hiddenVariable
	def add(self, increment):
		self.__hiddenVariable += increment
		print(self.__hiddenVariable)

# Driver code
myObject = MyClass()
myObject.add(5)  # This will work
myObject.add(10)  # This will work

# Trying to access the hidden variable directly
print(myObject.__hiddenVariable)

# How to print Object information in a Python class
#Printing objects gives us information about the objects we are workinh with.

class Test:
	def __init__(self, a,b):
		self.a = a
		self.b = b
	
	def __repr__(self):
		return f"Test a: %s b: %s" % (self.a, self.b)
	
	def __str__(self):
		return f"From str method of test: a: is %s b: is %s,"\
			"b is %s " % (self.a, self.b)

# driver code
t = Test(123, 246)
print(t)
print([t])