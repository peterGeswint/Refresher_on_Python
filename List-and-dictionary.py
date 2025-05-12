# Lists are mutable,and hence. they can be altered even after their creation.
# A single list may contain Datatypes like intergers, strings aswell as objects
# Dictionary in python on the other hand is an unordered colection of data values
# like a map, which unlike other data types that hold only single values as an element
# holds key value pairs. 
# A dictionary is mutable, but the keys in a dictionary must be immutable.

# Creating Lists
prices = [7, 8, 9, 10, 11, 12]
print(prices)
prices.append(2)
prices.insert(2,49)
print(prices)
prices.sort()
print(prices)
prices.reverse()
print(prices)

# Creating Dictionary
Dict = {101: "Reggi", 102: "Ravi", 103: "Ravi", 104: "Ravi"}
print("Dictionary: ", Dict)

player = {"FirstName": "Ravi", "LastName": "Kumar", "Age": 25, "Country": "India"}
print(player["FirstName"])

letters = ['a', 'b', 'c', 'd', 'e']
print(letters[0])
slice = letters[1:4]
print(slice)