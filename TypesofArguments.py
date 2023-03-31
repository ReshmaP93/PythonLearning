#Example 1

def fun(i,j):
    print(i,j)

fun(10,20) #positional arguments
fun(j=20,i=10) #keyword arguments

#Example 2 Default values assigned to positional arguments
def fun(i,j=10):
    print(i,j)
fun(100,200) #100 200
fun(100) #100 10

#Example 3 keyword arguments
def greetings(name,greetings):
    print(greetings+" "+name)

greetings(name='John', greetings='Hello') #Hello John
greetings(greetings="Hello",name='John') #Hello John

#Example 4 Positional and Keyword parameters

def my_fun(a,b,c):
    print(a,b,c)

my_fun(10,20,30) #positional parameters
my_fun(a=10,b=20,c=30) #keyword parameters
my_fun(b=20,a=10,c=30) #keyword arguments - we can change the order of arguments also

my_fun(10,20,c=30) #positional and keyword #10,20,30
my_fun(10,b=20,c=30) #positional and keyword #10,20,30
#my_fun(10,b=20,30) #Incorrect statement - Positional parameters must appear before any keyword parameter
#my_fun(10,30,b=20) #this is having logical error

#Example 5
def largest(a,b):
     if a>b:
         return a,b
     else:
         return b,a
print(largest(100,200)) #200 100
print(largest(20,10)) #20 10

res=largest(10,20)
print(res)
print(type(res)) #tuple

