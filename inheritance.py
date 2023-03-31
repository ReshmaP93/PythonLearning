#Example 1 - Single Inheritance

class A():
      def m1(self):
          print("this is m1 method of class A")
class B(A):
      def m2(self):
          print("this is m2 method of class B")

bobj=B()
bobj.m1() # this is m1 method of class A
bobj.m2() # this is m2 method of class B

#Example 2
class A:
    a,b=10,20 #class variables
    def m1(self):
        print(self.a+self.b)
class B(A):
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

bobj=B()
bobj.m1()
bobj.m2()

#Example 3 - Multilevel Inheritance
class A:
    a,b=10,20 #class variables
    def m1(self):
        print(self.a+self.b)
class B(A):
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

class C(B):
      i,j=50,30
      def m3(self):
          print(self.i*self.j)

cobj=C()
cobj.m1() #30
cobj.m2() #100
cobj.m3() #1500

#Example 4 - Hierarchy Inheritance -
class A:
    a,b=10,20 #class variables
    def m1(self):
        print(self.a+self.b)
class B(A):
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

class C(A):
      i,j=50,30
      def m3(self):
          print(self.i*self.j)

bobj=B()
bobj.m1() #30
bobj.m2() #100

cobj=C()
cobj.m1() #30
cobj.m3() #1500

#Example 5 - Multiple Inheritance - Multiple parent - single child
class A:
    a,b=10,20 #class variables
    def m1(self):
        print(self.a+self.b)
class B:
    x,y=200,100
    def m2(self):
        print(self.x-self.y)

class C(A,B):
      i,j=50,30
      def m3(self):
          print(self.i*self.j)


cobj=C()
cobj.m1()
cobj.m2()
cobj.m3()

#Example 6 calling parent class method using child class by using super() method
class A:
     def m1(self):
         print("This is m1 method in class A")
class B(A):
     def m1(self):
         print("This is m1 method in class B")
         super().m1() # to invoke the parent class method through child class methd
bobj=B()
bobj.m1() #calling the method using object #latest method will be called
          #This is m1 method in class B
          #This is m1 method in class A

#Example 7
class A:
      a,b=10,20

class B(A):
      i,j=80,90
      def m(self,x,y):
          print(x+y) #local variables #300
          print(self.i+self.j) #class variables #170
          print(self.a+self.b) #class variables #30
bobj=B()
bobj.m(100,200)

#Example 8 - Overriding variables
class Parent:
     name="Scott"
class Child(Parent):
      name="John" #overriding the variable
      def test(self):
          super().name
cobj=Child()
print(cobj.name)#John #here we have to use print bcoz we are overriding variables
cobj.test() #John

#Example 9 - Overriding methods - Hierarchy Inheritance
class Bank:
     def rateofInterest(self):
         return 0
class XBank(Bank):
      def rateofInterest(self):
         return 10
class YBank(Bank):
      def rateofInterest(self):
        return 12

objx=XBank()
print(objx.rateofInterest()) #10

objy=YBank()
print(objy.rateofInterest()) #12

#Example 10 Overloading - Polymorphism

class Human:
    def hello(self,name=None):
      if name is not None:
          print("Hello" +name)
      else:
           print("hello")

h=Human()
h.hello("Scott")
h.hello()

#Example 11 - Overloading 2
class Calculation:
      def add(self,a=0,b=0,c=0):
          print(a+b+c)

calobj=Calculation()
calobj.add() #0
calobj.add(10,20) #30
calobj.add(100,200,300) #600







