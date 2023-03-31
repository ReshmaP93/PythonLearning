#Example 1

class MyClass: #class
      def fun(self):
         pass #empty
      def display(self):
            print("Smith")

mc1=MyClass() #Objects
mc1.fun() #Accessing methods through objects
mc1.display() #Smith

#Example 2 - Passing parameters

class MyClass:
      def fun(self):
          pass #empty
      def display(self,name):
          print(name)
mc1=MyClass()
mc1.fun()
mc1.display("lally")

#Example 3
class Task:
     def fun(self):
         pass
     def display(self,designation):
         print("Test Analyst")
t1=Task()
t1.display("Test Analyst")

#Example 4 - Instance method
class MyClass:
     def m1(self):
         print("This is instance method")
     @staticmethod
     def m2(self,num):
        print(self,num)

mc=MyClass()
mc.m1()
mc.m2(100,200)

MyClass.m2(10,20) #10,20 - here calling the static method directly using class, not through object

#Example 5 Class Variables

class MyClass:
    a,b=10,20 #class variables declaration
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=MyClass()
mc.add()
mc.mul()

#Example 6 - Local Variables, Global Variables and Class Variables
i,j=14,23  #global variables

class MyClass:
     a,b = 10,20 #class variables
     def add(self,x,y): #x,y are local variables
         print(x+y) #x,y are local variables
         print(self.a+self.b) #here a.b are class variables
         print(i+j) #here i,j are global variables

mc=MyClass() #Accessing the method add
mc.add(100,400)

#Example 7
a,b=14,23  #if global,local and class variables are same

class MyClass:
     a,b = 10,20 #class variables
     def add(self,a,b):
         print(a+b) #a,b are local variables
         print(self.a+self.b) #here a.b are class variables
         print(globals()['a']+globals()['b']) #here a,b are global variables

mc=MyClass() #Accessing the method add
mc.add(100,400)

#Example 8 - One Class having multiple objects

class MyClass:
     def display(self,name):
         print("This is display method")
         print(name)

obj1=MyClass()
obj1.display("john")

obj2=MyClass()
obj2.display("scott")

#Example 9 #Method and Constructor
class MyClass:
     def __int__(self):
         print("this is constructor")
     def test(self):
         print("hello..")
     def work(self,x,y):
         return(x+y)
mc=MyClass() # created an object #invoke constructor automatically
mc.test() #methods we have to call explicitly through object
print(mc.work(10,20))

#Example 10
class MyClass:
    name="John"
    def __init__(self,name): #constructor expecting one parameter or argument
         print(name)
         print(self,name)

mc=MyClass("David") #passing parameter to the constructor

#Example 11
#Req Employee
   #constructor - eid,ename,sal
   #display() -  print eid,ename,sal
class Emp:
    def __init__(self,eid,ename,sal):
     #   a=10 #local variable
      #  self.a #class variable
         self.eid=eid #eid - local variable and self.eid is class variable
         self.ename=ename
         self.sal=sal #we can also create class variables inside the constructor or methods and accessible to constructors and methods
    def display(self):
         print(self.eid,self.ename,self.sal)

e1=Emp(1034,"John",50000)
e1.display()

e2=Emp(12345,"Shivs",70000)
e2.display()


#Example 12
#Req Employee
   #constructor - eid,ename,sal
   #constructor -  print eid,ename,sal
class Emp:
    def __init__(self,eid,ename,sal):
     #   a=10 #local variable
      #  self.a #class variable
         self.eid=eid #eid - local variable and self.eid is class variable
         self.ename=ename
         self.sal=sal #we can also create class variables inside the constructor or methods and accessible to constructors and methods
    def __str__(self):
        # return(self.ename,self.sal) #Invalid because __str__() will only returns string data
         return(self.ename)

e1=Emp(1034,"John",50000)
print(e1)







