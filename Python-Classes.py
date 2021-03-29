class Employee:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
john = Employee('John')
print(john) # John

# Dog class
class Dog:
  # Method of the class
  def bark(self):
    print("Ham-Ham")
 
# Create a new instance
charlie = Dog()
 
# Call the method
charlie.bark()
# This will output "Ham-Ham"

class Car:
  "This is an empty class"
  pass
 
# Class Instantiation
ferrari = Car()

class my_class:
  class_variable = "I am a Class Variable!"
  
x = my_class()
y = my_class()
 
print(x.class_variable) #I am a Class Variable!
print(y.class_variable) #I am a Class Variable!

class Animal:
  def __init__(self, voice):
    self.voice = voice
 
# When a class instance is created, the instance variable
# 'voice' is created and set to the input value.
cat = Animal('Meow')
print(cat.voice) # Output: Meow
 
dog = Animal('Woof') 
print(dog.voice) # Output: Woof

a = 1
print(type(a)) # <class 'int'>
 
a = 1.1
print(type(a)) # <class 'float'>
 
a = 'b'
print(type(a)) # <class 'str'>
 
a = None
print(type(a)) # <class 'NoneType'>

# Defining a class
class Animal:
  def __init__(self, name, number_of_legs):
    self.name = name
    self.number_of_legs = number_of_legs

class Employee:
  def __init__(self, name):
    self.name = name
 
  def print_name(self):
    print("Hi, I'm " + self.name)
 
 
print(dir())
# ['Employee', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'new_employee']
 
print(dir(Employee))
# ['__doc__', '__init__', '__module__', 'print_name']

class ParentClass:
  def print_test(self):
    print("Parent Method")
 
class ChildClass(ParentClass):
  def print_test(self):
    print("Child Method")
    # Calls the parent's version of print_test()
    super().print_test() 
          
child_instance = ChildClass()
child_instance.print_test()
# Output:
# Child Method
# Parent Method

class CustomError(Exception):
  pass

class ParentClass:
  def print_self(self):
    print('A')
 
class ChildClass(ParentClass):
  def print_self(self):
    print('B')
 
obj_A = ParentClass()
obj_B = ChildClass()
 
obj_A.print_self() # A
obj_B.print_self() # B

class String:
  # Dunder method to initialize object
  def __init__(self, string): 
    self.string = string
          
string1 = String("Hello World!") 
print(string1.string) # Hello World!

class ParentClass:
  def print_self(self):
    print("Parent")
 
class ChildClass(ParentClass):
  def print_self(self):
    print("Child")
 
child_instance = ChildClass()
child_instance.print_self() # Child

class Family:
  def type(self):
    print("Parent class")
    
class Member(Family):
  def type(self):
    print("Child class")
     
print(issubclass(Member, Family)) # True

class Animal: 
  def __init__(self, name, legs):
    self.name = name
    self.legs = legs
        
class Dog(Animal):
  def sound(self):
    print("Woof!")
 
Yoki = Dog("Yoki", 4)
print(Yoki.name) # YOKI
print(Yoki.legs) # 4
Yoki.sound() # Woof!

class A:
  def __init__(self, a):
    self.a = a 
  def __add__(self, other):
    return self.a + other.a 
    
obj1 = A(5)
obj2 = A(10)
print(obj1 + obj2) # 15