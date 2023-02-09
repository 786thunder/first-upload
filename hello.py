#x = 10
#print(x)
#x = "sitting"
#print(x)
#print(x)

#fruits = ["apple", "garpes", "mango"]

#for _ in range(5):
#	fruits.append("apple")
    
#print(fruits)


#while loops ###
# infinit loop

#shayan = "sitting"
#shayan == "sitting"
#while shayan != "standing":
 #   print("get your fat up")

#counter = 0
#while counter < 150:
 #   print(counter)
  #  counter = counter + 1

#def counter = 0
 #while counter < 10:
#	 print(counter)
# 	counter = counter + 1

#def double(numbers: list ): 
 #   result = []
  #  for  number in numbers:
   #   result.append(number * 2)
    #return result

#print(double([1, 2, 3, 4, 5, 6]))
 
 #creeat an
#def count_words(phrase):
#    print(len(phrase.split()))

#count_words("hi my name is thunder")


#def sum_list(numbers):
#    count = 0
 #   for number in numbers:
 #       count += number
 #   return count   

#print(sum_list([1, 2, 3,]))
#print(sum_list([1, 2, 3, 4, 5]))

# max() find_max

#def find_max(numbers):
 #   current_max = numbers[0]
  #  for number in numbers:
   #     if number > current_max:
    #      current_max = number

   #return current_max

#print(find_max([1, 5, 10, 3,1, 5, 10, 3,1, 5, 10, 3,1, 5, 10, 3,1, 5, 10, 3,1, 5, 10, 3,1, 5,
 # 10, 3,1, 5, 10, 3,1, 5, 10, 3,1, 577, 10, 3,1, 5,
  # 10, 3,1, 5, 10, 3,1, 5, 10, 3,1, 5, 10, 3,]))



#def word_frequency(phrase):
 #   result = {}
  #  words = phrase.split()
   # for word in words:
    #  if word not in result:
     #   result[word] = 1
      #else:
       # result[word] += 1
##
#    return result

#print(word_frequency(input("plese inter your phrase:")))

#print(word_frequency("i love batman because i am batman"))
 
 #result = {}
 #is "i" in the result

 ### higher order function
 ## map
 ## filter
  
#def double_number(number):
#   return number * 2

#print(list(map(double_number,[10, 9, 8])))


#print(list(map(lambda num: num * 3 , [10, 9, 8])))

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#print(list(filter(lambda number: number % 2 == 0, numbers)))

## list comprehension

#print([number for number in numbers if number ÷ 3 == 0])
 
 #import counter_app
#from counter_app importhome_page, app, show, db

#@app.route("/")
#def home():
#    return show(home_page)

#app.run(host="0.0.0.0", port=81)

#def increment():
#  returns " increment"

### day 6 

''' 
  <div style="background-colour: red;">
    <h2>hello</h2>
    <div style="background-colour: red;">
      <h2>welcome back</h2
    </div>
    <h6>qazi</h6>
    <input type= 'text' placeholder='username'/>
    <input type= 'submit'/>
    <p>hi, my name is qazi</p>
  </div>    
'''

#@app.route('/')
#def home():
 # return render_template_string(my_home_page)

#@app.route('/increment')
#import matplotlib

#print(matplotlib.__version__)

#import mysql.connector

#name = input("en78
# 67ter your name ")
#print("hello ", name)

#num1 = int(input("enter num1: "))
#num2 = int(input("enter num2: "))

#num3 = num1 * num2
#print("product is: ", num3)

# geeksforgeeks

#num1 = 576
#if(num1>12):
 # print("num1 is good ")
#elif(num1>35):
 #  print("num2 is goooo ")
#else:
 # print("num2 is great ")

#def hello():
  #  print("hello ")
 #   print("hello again ")
#hello()

#hello()

#def get_integer():   
#  result = int(input("enter integer"))
  #  return result

#def main():
 #   print("started")
  #  output = get_integer
   # print(output)

#if __name__=="__main__":
 #   main()

#for step in range(5):
 #    print(step)

#import math

#def main():
 #   num = 5

  #  num = math.fabs(num)
   # print(num)


#if __name__=="__main__":
   # main()

#import keyword

#print("the list of key words is: ")
#print(keyword.kwlist)

#for i in range(10):

#  print(i, end = " ")

 # if i == 6:
  #    break

#print()

#i = 0
#while i <10:
#  if i == 6:
 #   i+= 1
  #  continue
  #else:
   #  print(i, end = " ")

 # i += 1

 # if i == 6:
  #    break

#print()

#i = 0
#while i <10:  print(i, end = " ")

#if i == 6:

#print()

#i = 0
#while i <10:
 # if i == 6:
  #  i+= 1
   # continue
  #else:
   #  print(i, end = " ")

  #i += 1
  #if i == 6:
   # i+= 1
   # continue
  #else:
   #  print(i, end = " ")

#  i += 

# Using for loop

#for i in range(10):

#	print(i, end = " ")
	
#	if i == 6:
#		break
	
#print()
	

#i = 0
#while i <10:
	

#	if i == 6:
#		i+= 1
#		continue
#	else:
		
#		print(i, end = " ")
		
#	i += 1

#def fun():
 #    s = 0

#     for i in range(10):
 #         s += i
  #   return s
#
#print(fun())

#def fun():
  #  s = 0

   # for i in range(10):
    #    s += i
     #   yield s
 
#for i in fun():
 #    print(i)

#g = lambda x: x*x*x

#print(g(2))

#a = 4 
#b = 9

#try:
 #   k = a//b
  #  print(k)
#
#except ZeroDivisionError:
 #   print("can not divided by zero ")

#finally:
 #     print("this is always executed ")

#print("the value of a / b is :")
#assert b != 0, "divided by 0 error"
#print(a / b)

#x, y, z = input("enter three valuse: ").split()
#print("number of boys: ", x)
#print("number of girls: ", y)
#print("number of techers: ", z)
#print()

#import time

#count_seconds = 3
#for i in reversed(range(count_seconds + 1)):
 #   if i > 0:
  #      print(i, end=">>>")
   #     time.sleep(1)
    #else:
     #   print("start")

#a = 12
#b = 2
#c = 2023
#print(a,b,c,sep=".")

#import sys

#sys.stdout.write("www.thunder.com")
#ys.stdout.write("innovative company!")
# Here all the iterables are True so all
# will return True and the same will be printed
#print (all([True, True, True, True]))

# Here the method will short-circuit at the
# first item (False) and will return False.
#print (all([False, True, True, False]))

# This statement will return False, as no
# True is found in the iterables
#print (all([False, False, False]))
#a = 3
#b = 4

#print("addition of number is :",end=" ")
#print(operators.add(a, b))

#print("subtraction of number is :",end=" ")
#print(operators.sub(a, b))

#print("product of the number is :",end=" ")
#print(operators.mul(a, b))

# Python code to demonstrate working of
# add(), sub(), mul()

# importing operator module
#import operator

# Initializing variables
#a = 4

#b = 3

# using add() to add two numbers
#print ("The addition of numbers is :",end="");
#print (operator.add(a, b))

# using sub() to subtract two numbers
#print ("The difference of numbers is :",end="");
#print (operator.sub(a, b))

# using mul() to multiply two numbers
#print ("The product of numbers is :",end="");
#print (operator.mul(a, b))

#file = open("file.txt","r")
#print(file.read())

#a = "welcome to thunder"
#print(a.isspace())
#a = int(input("enter your age"))
#print("your age is:", a)
#if(a>18):
 ## print("you can drive")
  #print("yes")

#else:
 # print("you can not drrive")
  #print("no!")
#60print("thunder")

#import time
#timestamp = time.strftime("%H:%M:%S")
#print(timestamp)
#timestamp = int(time.strftime("%H"))
#print(timestamp)
#timestamp = int(time.strftime("%M"))
#print(timestamp)
#timestamp = int(time.starftime("%S"))
#print(timestamp)

#name = "thunder"
#for x in name:
#  print(x)
#  if(x =="h"):
#    print("hitlerr")

#colours =  ["red", "green", "blue"]
#for colour in colours:
#  print(colour)
 # for x in colour:
  #  print(x)
#for k in range(9, 20):
 # print(k)
#i = 0
#while(i<3):
 # print(i)
  #i = i + 1

#print("done with the loop")

#OOPs b Object Oriented Programming





"""class Aeroplane:

  def startEngine(self, name):
    print(name, "Aeroplane Starting engine")

  def engageGear(self, gear):
    print("Engine started, engaging gear no", gear)


  def fly(self, lift):
    print("Lift off : ", lift)

plane1 = Aeroplane()


plane1.startEngine("Naveeds")
plane1.engageGear(3)
plane1.fly(False)



plane2 = Aeroplane()

plane2.startEngine("Shayans")
plane2.engageGear(9)
plane2.fly(True)

plane3 = Aeroplane()

plane3.startEngine("thunders")
plane3.engageGear(5)
plane3.fly(True)"""

#OPPs in python

"""class Employee:
  pass
harry = Employee()
rohan = Employee()

harry.name ="harry"
harry.salary = 455
harry.result = "pass"

rohan.name = "rohan"
rohan.salary = 633
rohan.result = "fail"
print(rohan.__dict__)
print(harry.__dict__)"""
"""class names:
  def __init__(self, name, age):
    self.name = name
    self.age = age

    print(names.name(shayan))

  def __init__(self, height, weight):
    self.height = height
    self.weight = weight"""

# class employee:
  # no_of_leaves = 8

  # def __init__(self, aname, asalary, arole):
      # self.name = aname
      # self.asalary = asalary
      # self.arole = arokle

  # def printdetails(self):
    # return f"the name 

# @classmethod
# def change_leaves(cls, newleaves):
#  cls.no_of_leaves = newleaves

#harry = employee("harry", 334, "instructer,")
#import time
#import os

#work_duration = 3600  # 1 hour in seconds

#print("System will shut down in 1 hour. Please save your work.")
#time.sleep(work_duration)
#os.system("shutdown -s -t 0")

"""class Employee:

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "_" + last + "@company.com"

def fullname(self):
  return "{} {}".format(emp_1.first, emp_1.last)
emp_1 = Employee("corey", "schafer", 543333)
emp_2 = Employee("name", "nop", 6777)
 

print(emp_1)
print(emp_2)
#print("{} {}".format(emp_1.first, emp_1.last))"""

"""emp_1.first = "corey"
emp_1.last = "schafer"
emp_1.email = "corey.sfsdgd@gmail.com"
emp_1.pay = 543333

emp_2.last = "name"
emp_2.email = "corey.sfsdgd@gmail.com"
emp_2.pay = 6777"""

## OOP
"""class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print("Woof!")"""

#a = 4
#b = 5
#c = a, b

#for x in range(9999999):
 #print(x)

""" from numpy import random

z = random.randint(100)

print(z) """

"""from numpy import random

x = random.rand(5)

print(x)"""

"""class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 10
	
	# A member method that changes
	# __hiddenVariable
	def add(self, increment):
		self.__hiddenVariable += increment
		print (self.__hiddenVariable)

# Driver code
myObject = MyClass()	
myObject.add(2)
myObject.add(5)

# This line causes error
print (myObject.__hiddenVariable)
"""
"""class A:
      def displayA(self):
        print("thunder.gb")

class B:
      def displayB(self):
        print("thunder.pk")

class C(A, B):
      def displayC(self):
        print("thunder.AUS")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC() """

"""class student:
  def __init__(self):
    self.name=""
  def getname(self): 
    return self.__name
  def setname(self,name):
    self.__name=name

obj=student()
obj.setname("thunder")
name=obj.getname()
print(name)"""

#encapsulation  an objects variable shuld not always be directly accessible.

"""class student:
    __name="zeeshan"
    def __init__(self):
      print(self.__name)
      self.__displayinfo()
    def __displayinfo(self):
       print("welcome to thunder")

obj=student()"""

##polymorphism  means same function name but different  signatuer
"""l=[10,20,30]
print(len(l))
s=("welcome")
print(len(s))
"""

## funtion overloading ,, function over riding

"""class W:
  def displaying(self):
    print("welcome to thunder ")"""

"""obj=W()
obj.displaying() 
obj.displaying("python")"""

"""class E:
  def displayinfo(self):
    super().displaying()
    print("welcome to my company")

#obj=E()
#obj.displayinfo()
#obj.displayinfo("babe")


class IIP(E, W):
  def displayinginfo(self):
    super().displayinfo()
    print("welcome to IIP")#

obj=IIP()
obj.displayinginfo( )
class area:
  def find_area(self,x=None,y=None):

    if x!=None and y!=None:
      print(x*y)
    elif x!=None:
      print(x*x)
    else:
      print("nothing")

obj1=area()
obj1.find_area()
obj1.find_area(10)
obj1.find_area(10,20)

class A:
  def showData(self):
    print("i am in A  fefwefclass")

class A:
  def showData(self):
    print("i am in Bmsdlf class")

obj=A()
obj.showData()
def square(n):"""
  
'''tales in a number n, returns the square of n
  print(n**2)
  square(5)
  print(square.__doc__ )'''
  # Python program to demonstrate
# hybrid inheritance


'''class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
#object.func3()'''
'''class Mobile:
  def __init__(self):
    print("iphone is owsome")

iphone = Mobile()

class ElectronicDevices:
  chargingjug = 1
  earphonejack = 2

class PocketGaget(ElectronicDevices):
  simcard = "yes"
  memorycard = "no"

class Phone(PocketGaget):
  name = "thunder"
  type = "pro max"

phone = Phone()
print(Phone.s)

a = 44
b = 89
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a>b else 0
print(c)

##multilevel inheritance

class Person:
  def assignbasi(self, name, age):
    self.name = name
    self.age = age

class Employee(Person):
  def assignemp(self, idno):
    self.idno = idno

class Programmer(Employee):
  def assignprog(self, lang):
    self.lang = lang

def main():
  obj1 = Programmer()
  obj1.assignbasic("aswin", 32)
  obj1.assignemp(1003)
  obj1.assignprog("python 3")
  print(obj1.name, obj1.age, obj1.idno, obj1.lang)

if __name__ == "__main__":
    main()

### school teacher 1, 2 student
## hybrid inheritance>>>

class School:
  def Fun1(self):
    print("im principal")

class Teacher1(School):
  def Fun2(self):
    print("im teacher1")

class Teacher2(School):
  def Fun3(self):
    print("i am teacher 2")

class Student(Teacher1, Teacher2):
  def fun4(self):
    print("i am new student")

obj = Student()
obj.Fun1()
obj.Fun2()
obj.Fun3()
obj.fun4()

## encapsulation 

class school:

  def __init__(self):
    self.__fun2()

  def fun1(self):
    print("im fun1")

  def __fun2(self):
    print("im fun2")


obj= school()
obj.fun1

class Add:
  def sum(self, a, b):
    r = a + b 

  def sum(self, a, b, c):
    r = a + b + c
    print(r)

obj = Add()
#obj.sum(1, 2)
obj.sum(1, 2, 3)

class Add:

  def sum(self, a=None,b= None,c= None):

    if a!=None and b!=None and c!=None:
      r = a + b + c

    elif a!=None and b!=None:
      r = a + b

    else:
      r=a

      return r

obj=Add()
print(obj.sum(1,2,3))
print(obj.sum(9,2))
print(obj.sum(9))

# Python program to
# demonstrate private members

# Creating a Base class


class Base:
  def __init__(self):
    self.__c()


def __init__(self):
		self.a = "GeeksforGeeks2"
		self.__c = "GeeksforGeeks34"

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.__c)


# Driver code
obj1 = Base()
print(obj1.__c)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class




class parent:

  def fun(self):
    print("im in the parent class")

class child(parent):
  def fun(self):
    print("i am in the child class")

obj=child()
obj.fun()
obj=parent()
obj.fun()

#print("First Module Name: {}" .format(__name__))

## __name__ will print __mani__

##abstract class


from abc import ABC, abstractmethod

class parent(ABC):

      @abstractmethod
      def fun1(self):
        pass

      def fun2(self):
        print("this is parent class")

class child(parent):

      def fun1(self):
        print("this is child class")


obj=child()
obj.fun1()
obj.fun2()

class Pakistan():
  def capital(self):
    print("islamabad")

  def language(self):
    print("urdu")

  def type(self):
    print("not developed")

class Canada():

  def capital(self):
    print("toronto")

  def language(self):
    print("english")

  def type(self):
    print("developed")

obj_Pakistan = Pakistan()
obj_canad  = Canada()
for country in (obj_Pakistan, obj_canad):
  country.capital()
  country.language()
  country.type()

#def Welcome():
 # print()
 
class MyClass:
    @classmethod
    def my_method(cls):
        print("This is my class method")

obj = MyClass()
obj.my_method()

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance()) # 1000
account.deposit(500)
print(account.get_balance()) # 1500
account.withdraw(2000) # Insufficient funds.
print(account.get_balance()) # 1500

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

def pet_speak(pet):
    print(pet.speak())

dog = Dog("Fido")
cat = Cat("Whiskers")

pet_speak(dog) # Output: "Woof!"
pet_speak(cat) # Output: "Meow!"

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
p = Person("John", 3)
print(p.name) # Output: John
p.name = "Jane", 4
print(p.name) # Output: Jane



class Dog:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    def age(self):
        return self._age

    def age(self, value):
        self._age = value

ob=Dog('ali')
ob.age = 77
print(ob.name)
print(ob.age)


def add_numbers(x, y):
  return x + y

def multiply_numbers(y, z):
  return y * z

result = add_numbers(4, 8)
esult = multiply_numbers(5 ,6) 
print(esult)
print(result)

y = 10

def my_function():
  global x
  x = 10
  print(5)

my_function()

print(y)
print(x)

with open('file.txt','w') as f:
  f.write('hello world!')
  f.truncate(5)
#with open('file.txt', 'r') as4



## date 1.25.2023
class myfunc():
  f = 30
  print(f)

myfunc()

class myfunc:
  def __init__(self, name):
    self._ername = name

  def MyClass1(self, _name):
    return _name

  def MyClass1(self, age):
    self._name = age

  def age(self):
    return self._age

  def age(self):
    self

def cube(x):
  return x*x*x

print(cube(2))

l = [1, 2, 3, 4, 5]
#newl = []
#for item in l:
 # newl.append(cube(item))
newl = list(map(cube, l))
print(newl)

a = [1, 2, 3, 4, 56]
b = [1, 2, 3, 4, 56]
print(a is b)
print(a == b)

class person:
  name = 'thunder'
  age = 9
  height = '6'
  def info(self):
    print(f'{self.name} hight is {7}')

A = person()
b = person()
c =person()
A.name = 'shayan'
A.age = 5
#print(A.age, A.height, A.name)

b.name = 'zeesshan'
b.age = 67
b.height = 55445
c.name = 'zoya'
c.age = 444
A.info() 
b.info()
c.info()
class person():

    def __init__(self, n, o):
      print('hay im thunder')

      self.name = n
      self.occ = o

    def info(self):
      print(f'{self.name} is a {self.occ}')



a = person('shayan', 'developer')
b  = person('thunder', 'company')
a.info()
b.info()

def greet(fx):
  def mxf(*args, **kwwargs):
    print('good morning')
    fx(*args, **kwwargs)
    print('thanks for using this service')
  return mxf

@greet
def hello():
  print('hello world!')

# @greet
def add(a, b):
  print(a + b)

# greet(hello)()
hello()
greet(add)(1, 2)

from abc import ABC,abstractmethod
 
class car(ABC):
  def Show(self):
    print('every car has 4 wheels')
  @abstractmethod
  def Speed(self):
    pass

class Maruti(car):
  def Speed(self):
    print('speed is 100km\h')

class Suzuki(car):
  def Speed(self):
    print('speed is 70km\h')

obj=Maruti()
obj.Show()
obj.Speed()
obj=Suzuki()
obj.Speed()
from abc import ABC,abstractmethod

class shape(ABC):
  @abstractmethod
  def show(self):
    pass

class square(shape):
  def show(self):
    print('square has 4 equal sides...')

class circle(square):
  def show(self):
    print('circle is 2 dimensional...')


c=circle()
c.show()
c.show() 

###polymorphism
#function having differet behaviour

class A:
  def show(self):
    print('welcome')

  def show(self,fname=''):
    print('welcome',fname)

  def show(self,fname='',lname=''):
    print('welcome', fname, lname)

obj=A()
obj.show()
obj.show('shayan')
obj.show('shayan','ali')


class A:
  def Disp(self):
    print('this is parent class method')

class B(A):
  def Disp(self):
    super().Disp()
    print('this is child class method...')

obj=B()
obj.Disp()
### multithreading...
from abc import ABC,abstractmethod

class Father(ABC):
  @abstractmethod
  def disp(self): ## this is abstract class
    pass

  def show(self):
    print('concreat meathod')  ## this is concreat class

class Child(Father):
  def disp(self):
    print('child class')
    print('this is abstract class')

c=Child()
c.disp()
c.show()

from abc import ABC,abstractmethod

class DefenceForce(ABC):
  @abstractmethod
  def area(self):
    pass

  def gun(self):
    print('gun = AK47')

class Army(DefenceForce):
  def area(self):
    print('army area = land')

class AirForce(DefenceForce):
  def area(self):
    print('airforce area = sky')

class Navy(DefenceForce):
  def area(self):
    print('navy area = see')

a = Army()
af = AirForce()
n = Navy()

a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()
print()

def has_duplicate_letters(sentence):
    words = sentence.split()
    for word in words:
        if len(word) != len(set(word)):
            return True
    else:
        return False
sentence = "Hello World, how are you today?"
print(has_duplicate_letters(sentence))

sentence = "Hello World, hhow are you today?"
print(has_duplicate_letters(sentence)) 

import socket

def get_domain_name(ip_address):
    return socket.gethostbyaddr(ip_address)[2]

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"
print(calculate(5, "*", 4)) #output: 24

def apply_discount(price, discount):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price

item_price = 100
discount_percent = 20
final_price = apply_discount(item_price, discount_percent)
print(final_price)
class MyClass:
  def __init__(self, value):
    self._value = value

  def show(self):
    print(f'the value is{self._value}')

@property
def ten_value(self):
  return 10* self._value

@ten_value.setter
def ten_value(self, new_value):
  self._value = new_value/10

obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

class A:
  name2='mr shayan'
  def __init__(self, name, age, address):
     address='hunza'
     print(age, name, address,self.name2)

  def show(self):
    print(self.name2)


obj = A(32, 'thunder',None)
obj.show()

def greet(firstname, lastname):
  print('good evening', firstname , lastname)

greet('shayan', 'thunder')

a =int(input('enter a number:'))
b = int(input('enter the scound number:'))

try:
 c = a/b
 print('result', c)
except:
  print('can not divided by zero') 

class A:
  def __init__(self,name,age,adderess):
    print(age,'',name,'',adderess)

obj=A(10,'thunder','gilgit')
obj=A(10,'shayan','sultanabad')
class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

  def show(self):
    print(f"the name of employee {self.id} is {self.name}") 

e1 = Employee("fwef", 77)
e1.show()
class A:
  a = 89
  _j = 98
  __i= None
  print(a, _j, __i)
 # def add(self):
  #  self.__i= self.a+self._j
   # print("addition:", self.__i)

class B(A):
  def Show(self):
    print(self.a)
    print(self._j)
    #fprint(self.__i)

obj=B()
obj.Show()
#print(obj.a) 
#print(obj._j)
#print(obj.__i)

class Father:
  def Land(self):
    print("i have 59 accars of land in gb")

class Son(Father):
  def Money(self):
    print("i have 59 corrore in my bank account")

class GrandSon(Son):
  def Property(self):
    print("i have 35% shers in gilgit app")

S=GrandSon()
S.Land()
S.Money()
S.Property( )

class A:
  num1=int(input("enter the first number "))
  num2=int(input("enter the second number "))

  def add(self):
    print("addition", self.num1+self.num2)
  def subtraction(self):
    print("subtraction", self.num1-self.num2)

class B(A):
  def multi(self):
    print("multipilication:", self.num1*self.num2)
  try:
    def division(self):
      print("division", self.num1/self.num2)
  except:
    print("caan  not divideed by zero")
  def reminder(self):
    print("reminder:", self.num1%self.num2)

obj=B()
obj.add()
obj.subtraction()
obj.multi()
obj.division()
obj.reminder()

class Gfather:
  surname="barcha"

class Father():
  def show1(self):
    print("shahkhan", self.surname)

class Son():
  def Show(self):
    print("shayan", self.surname)

class GrandSon(Gfather,Son,Father):
  def Disp(self):
    print("bijon", self.surname)

t=GrandSon()
t.Disp()
t.Show()
t.show1

class Naveed:
   back = "node js and dewups"
   def BackEnd(self):
    print("backend is done using: ", self.back)

class Little:
  front = "javascript and html"
  def FrontEnd(self):
    print("front end is done using:", self.front)

class TeamLeadKamran(Naveed,Little):
  def Show(self):
    print("the electric taxi app created")

obj=TeamLeadKamran()
obj.BackEnd()
obj.FrontEnd()
obj.Show() 

class Father:
  surname="barcha"
  def Show(self):
    print("my surname is:", self.surname)

class Mother(Father):
  def love(self):
    print("my name is sartaj", self.surname)

class Son(Father):
  def Show2(self):
    print("my name is tayab ", self.surname)

class Daughter(Father):
  def Show3(self):
    print("my name is zoya ", self.surname)

class son2(Father):
  def big(self):
    print("my name is zeeshan")

obj=son2()
obj.big()
obj.Show()


class A:
  def show(self):
    print("welcome")

  def show(self,firstname=" "):
    print("welcome" , firstname)

  def show(self, firstname=" ", secondname=" "):
    print("welcome", firstname, secondname)

obj=A()
obj.show()
obj.show(" thunder")
obj.show("thunder ",".com ")

def Calculator(a,b):
    print("add two numbers:",a+b)
    print("subtract two numbers:",a-b)
    print("multiply two numbers:",a*b)
    print("divide two numbers:",a/b)

Calculator(45,6)
Calculator(53,3)
Calculator(45,0)'''
'''user_input = int(input("enter your number: "))

if user_input % 2 == 0:
    print("the number is even")

else:
    print("the number is odd ")

age = int(input('enter your age: '))

if age > 60:
    print('you are too old to get marry!')
elif age < 18:
    print('you are too young to get marry!')
else:
    print('we will find a perfect match for you!')

for i in range(90, 99):
    print(i)

input = int(input("enter the number: "))

for number in range(1, 11):
    print(input * number)

password = "thunder786"

input_password = input("enter your password")

while password != input_password:
    input_password = input("enter password")

else:
    print("unlocked")

if "a" in "learning code":
    pass

for number in range(1, 11):
    if number % 2 == 0:
        break
    else:
       print(number)

import calendar
print(calendar.month(2023,))

def calculator(a,b):
    print("addition :", a+b)
    print("subtraction:", a-b)
    print("division", a/b)
    print('multiplication:',a*b)

calculator(2,4)

calculator(6,8)

calculator(67,9)
calculator(76,8)


###multithrading
class A:
  def run(self):
    for i in range(5):
      print("shayan")

class B:

class Father:
  age = 56
  def show(self, name):
    print("i have a clint his name is:", name,"and his age is", self.age)

class Son(Father):
  def show2(self, idno):
    print("his id no is", idno)

obj=Son()
obj.show("ali")
obj.show2(54)




class A:
  _a = 78
  def __init__(self):
    print("hight of our home is", self._a)

obj=A()
print(obj._a)


# public: a
##     _a
##privet: __a
class Father:
  a=8
  _a=8
  __=8
  def show(self):


class son(Father):
  def show(self):
    return super().show()
obj=son()
obj.show()
obj.show()
r

def simple_intrest(p,t,r):
  print("the principal amount is:", p)
  print("the time required is:", t)
  print("the rate of per item is", r )

  si = (p*t*r)/100

  print("the simple intrest is:" , si)

simple_intrest(12,34,45)
def pattern(n):

  for i in n:

    print("|", end="")

    print("*" * int(i))

n = "564738291"
pattern(n)

# Python3 program to find compound
# interest for given values.



def compound_interest(principal, rate, time):

  amount = principal * (pow((1 + rate / 100), time))
  CI = amount - principal
  print('compound intrest is', CI)

compound_interest(10000, 10.5, 5)'''

def compound_interest(p,t,r):
    print()