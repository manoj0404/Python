# Lamda Function 
'''def double(x):
    return x*2
print(double(5))
double = lambda x: x*2
cube = lambda x: x*3
print(double(5))
print(cube(5))

#map
li = [1,2,3,4,5,6]
new =list(map(cube,li)) 
print(new


#filter
li = [1,2,3,4,5,6]
def filter_fun(a):
    return a>4

new =list(filter(filter_fun,li))
print(new)
from functools import reduce
li = [1,2,3,4,5,6]
sum = reduce(lambda x,y: x+y,li)
print(sum)

#54 is == 
a= 4
b="4"
print(a is b) #Exact location of boj in mem
print(a==b) #value
#intro object oriented programming Classes and Object
class person:
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def info(self):
        print(f"hey i am {self.name} and my age is {self.age}")       
a = person("manoj","50")
a.info()'''

'''b = person()
print(a.name)
print(a.occu)
b.name ="shubham"
b.occu = "teacher"
print(b.name)
print(b.occu)

# Getters and setters
class person:
    def __init__(self,value):
        self.value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,newvalue):
        self._value = newvalue
a = person()


class maneger():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def showdet(self):
        print(self.a+self.b)
class emp(maneger):
    def showide(self):
        print(self.a*self.b)
call = maneger(5,6)
call.showdet()
#a.showide()
print("By calling employee:")
cal1 = emp(5,6)
cal1.showdet()
cal1.showide()

## Librery manegement project in python
class librery:
    def __init__(self):
        self.nobooks=0
        self.books = []
    def addbook(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)
    def showinfo(self):
        print(f"the librery has {self.nobooks} books")
li = librery()
li.addbook("hary potter")
li.showinfo()
li.addbook("hary potter1")
li.addbook("hary potter")
li.addbook("hary potter")
li.addbook("hary potter")
li.showinfo()c

## 57 class and object
class person:
    name = "Harry"
    occu ="Software Developer"
    neetw = 20
    def info(self):
     print(f"{self.name} is a {self.occu}")

    
a =person()
a.name = "Shubham"
a.occu ="Accountant"
a.info()


class collage:
    def __init__(self,name,age,prn):
        self.name =name
        self.age= age
        self.prn= prn
    def student(self):
        print(f"The student name is {self.name} , age is {self.age} and prn is {self.prn}")
a = collage("manoj",21,2111)
a.student()
f =open('new.txt','a')
f.write('Hello world')
f.close()

## 59 python Decoretor
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx
@greet 
def hello():
    print("Hello World")
def add(a,b):
    print(a+b)
hello()
hello()
        
## inheritance in python
class employee:
 def __init__(self,name,id):
   self.name =name
   self.id = id

 def showdetials(self):
    print(f"The name of employee: {self.name} and id is {self.id}")

class Emp1(employee):
 def my(self):
  print("my name is manoj")
e1 = Emp1("Manoj",1)
e1.my()
e1.showdetials()
e2 = employee("sanny",3)
e2.showdetials()
e2.my
import random
a = int(input("enter the number:"))
b=int(random.randint(0,100))
if(a>b):
    print(a)
else:
    print(b)
##86##
#walrus operator
a = Trueh
print(a:=False)

foods = list()

while True:
    food =input("What food do you like:")
    if(food == "quit"):
       break
    foods.append(food)

print(foods)
## shutil module 87##
import shutil
shutil.copy("main.py","main2.py")
shutil.copy2("main.py","main2.py")
shutil.copytree()
shutil.move()
shutil.rmtree()'''


# request module 8









         
        
     



    

        











