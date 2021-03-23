#Comments
#user = "JDoe" #does not run in code

#Arithmetic operations
result = 10 + 10 #addition
result = 10 - 10 #subtraction
result = 10 * 10 #multiplication
result = 10 / 10 #division
result = 10 % 10 #modulo
result = 10 ** 2 #power

#Plus-Equals Operator +=
results = 0
results += 10 #returns 10
string = "string"
string += "string2" #returns "stringstring2"

#Variables
user_name = "username" #can be string
user_id = 102 #can be int
is_user_verfied = True #can be boolean

#Modulo Operator
result = 8 % 2 #returns 0, 8 divided by 2 is 4
result = 7 % 2 #returns 1, 7 divided by 2 is 3.5

#Integers
result = 1
results = -1
results = 0.0

#String Concatenation
string1 = "Hello"
string2 = "World"
new_string = string1 + string2 #returns "HelloWorld"

#Strings
string1 = "Hello"
string2 = "world \
    this is a longer string" #the \ allows your string to go down

#Floating Point Numbers
num = 1.34
num2 = 12.00
num3 = 0.30

#Print() function
print("Hello Worlds") #print strings
print(100) #print numbers
num = 10
print(num) #print variables

#Elif statement
var1 = "fish"

if var1 == 'fish':
    print('you have a fish')
elif var1 == 'cat':
    print('you have a cat')
else:
    print('error')

#Handling Exceptions
try:
    print('test')
except:
    print('error')

#OR Operator
True or True #true
True or False #true
False or False #false
1 < 2 or 3 < 1 #true

#Equal Operator
if 'yes' == 'yes': #True
    print('equal')

if (2 > 1) == (5 < 10): #True
    print('same')

#Not Equal Operator
if 'yes' != 'no': #true
    print('not equal')

#Comparison Operators
a = 1
b = 2
a < b  # evaluates to True
a > b  # evaluates to False
a >= b # evaluates to False
a <= b # evaluates to True
a <= a # evaluates to True

#If statement
test_value = 100
if test_value > 1:
  # Expression evaluates to True
  print("This code is executed!")
if test_value > 1000:
  # Expression evaluates to False
  print("This code is NOT executed!")
print("Program continues at this point.")

#Else statement
test_value = 50
if test_value < 1:
  print("Value is < 1")
else:
  print("Value is >= 1")
test_string = "VALID"
if test_string == "NOT_VALID":
  print("String equals NOT_VALID")
else:
  print("String equals something else!")

#AND operator
True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1   # Evaluates to False
"Yes" and 100     # Evaluates to True

#Booleans
is_true = True
is_false = False

#NOT operator
not True     # Evaluates to False
not False    # Evaluates to True
1 > 2        # Evaluates to False
not 1 > 2    # Evaluates to True
1 == 1       # Evaluates to True
not 1 == 1   # Evaluates to False

#Function Parameters
def function(vari1, vari2):
  return vari1,vari2 #indentation matters

#Calling functions
function(1,2)

#Default function Parameters
def function1(vari1 = 0, vari2 = 0): #setting default parameters
    return vari1,vari2

#Returning multiple values from a function
def square_point(x, y, z):
    x_squared = x * x
    y_squared = y * y
    z_squared = z * z
    return x_squared, y_squared, z_squared
a,b,c = square_point(1,2,3)

#Lists
numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]
empty_list = []

#Adding to a list
empty_list.append('example')
empty_list.append(1)

#List indices
empty_list[0] #prints 'example'
empty_list[1] #prints 1

#Negative list indices
empty_list[-1] #select from last element of the list
empty_list[-3:] #select the last three elements
empty_list[:-2] #select everything except the last two elements

#List count
empty_list.count('element') #returns how many times that element is present

#List length
len(empty_list) #returns list size

#List sort
#empty_list.sort() #sorts the elements

#List slicing
empty_list[0:2] #slices elements indices 0-2

#List sorted
#sorted(empty_list)

#Adding Lists together
empty_list + ['element1', 'element2']

#Loops
for i in empty_list:
  'action statement'
  'action statement'

#Loop Breaks
numbers = [0, 254, 2, -1, 3]
for num in numbers:
  if (num < 0):
    print("Negative number detected!")
    break # breaks at -1
  print(num)

#Loop Continue
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
  if i < 0:
    continue # Print only positive numbers:
  print(i)

#Loop Range
for i in range(3):
    print(i) # Print the numbers 0, 1, 2:

for i in range(3):
    print("WARNING") # Print "WARNING" 3 times:

for i in range(9):
    empty_list.append(i) # adds 0-8 

#While Loop
i = 1
while i < 6: # This loop will run 5 times
  print(i)
  i = i + 1

#Nested Loop
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]
for group in groups: # This outer loop will iterate over each list in the groups list
  for name in group: # This inner loop will go through each name in each list
    print(name)

#Strings Escaping Characters
txt = "You can use quotes \"inside a string \""

#Strings in
game = "Popular Nintendo Game: Mario Kart"
print("l" in game) # Prints: True
print("x" in game) # Prints: False

#Indexing and Slicing Strings
str = 'yellow'
str[1]     # => 'e'
str[-1]    # => 'w'
str[4:6]   # => 'ow'
str[:4]    # => 'yell'
str[-3:]   # => 'low'

#String length
length = len("Hello")
print(length) # Output: 5

#String .format()
msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10) # => 'Fred scored 3 out of 10 points.'
msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster') # => 'Fred tickled a fluffy hamster.'

#String methods
#.lower()
#.upper()
#.title()
#.strip()
#.split()
#.find()
#.replace()
#.join()

#Dictionaries
roaster = {"q1": "Ashley", "q2": "Dolly"}
roaster['q1'] = 'Ashley2' #updates a single key:value

#Dictionary updates
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}
#dict1.update({key:value, key:value}) #updates multiple key:value
#or
#dict1.update(dict2) # dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}

#Dictionary methods
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}
ex_dict.keys() # ["a","b","c"]
ex_dict.values() # ["anteater", "bumblebee", "cheetah"]
ex_dict.items() # [("a","anteater"),("b","bumblebee"),("c","cheetah")]
ex_dict.get("a", "default return") # "anteater" if not then returns default
ex_dict.pop("a") # removes key:value from the dictionary

#Dictionary from lists
#newDict = {key:value for key, value in zip(<lIST1>, <LIST2>)}

#Dictionary returning values from keys
#value = dict['color'] #returns and assigns the dictionary value

#dicionary getting a key
#dict.get(<VALUE>, <you set return>) #will return the Key from the dictionary

#Dictionary removes Key:value pair and returns value
#dict.pop(<KEY>, <you set return>) returns value

#Dictionary return all keys
#variable = dict.keys() #returns all keys in the dictionary

#Dictionary return all values
#dict.values() returns all values in the dictionary

#Dictionary get both the keys and the values
#for i, j in dict.getitem(): #loops throught dict and returns key and values
#  print(i, j)

#Modules
from datetime import datetime
time =  datetime.now()
print(time)

import random
randNum = random.randint(1, 101) #random number from a range
#random.choice(lst) #picks a random element from a list

#from <python_file.py> import <python_function()>

#Classes
class Class1:
  vari = 1

#Methods, aka functions in classes
class Class2:
  var1 = 1
  def method1(self):
    self.var1 = 2

#Class dunder __init__
# def __init__(self, arg):
    #self.arg = arg

#Class dunder __repr__
# def __repr__(self):
  #return string #can only return a string which represents

#vari = Class2()
# print(vari) #prints __repre__ returns  

#Classes using methods from other classes, proxy
#class SubClass(ParentClass):
  #def inherited_method(self, arg1, arg2):
    #super().inherited_method(arg1, arg2)