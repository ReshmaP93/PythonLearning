#Example 1
#To create a function we use def word
def myfun():  #declaring the function
    print('hello')
myfun()  #call the function

#Example 2 Passing a parameter
def myfun(name):
    print("Hello",name)

myfun("Smith")

#Example 3
def cal(a,b):
    print(a+b)
#First method
sum=cal(100,20) #120
print(sum)

#Second Method
print(cal(100,20))

#Example 4
def fun():
     return
#Another way
def fun():
    i=10
print(fun()) #None - By default this function will return none

#Example 5
def cal(a,b):
    print(a+b)
cal(10,20) #30

#####
def cal(a,b):
    return(a+b)
print(cal(10,20)) #30

