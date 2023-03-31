#Example 1
global_var=20 #global variable

def func():
    local_var=10
    print(local_var) #local variable
    print(global_var)

func()

#print(local_var) #invalid because local_var is local variable of func()
print(global_var) #valid because global_var is global variable of func()

#Example 2
xy=100 #global variables

def cool():
    xy=200 #local variable
    print(xy)
cool() #200

#Example 3 Using global variable as a local variable and update a value
xy=100 #global variables

def cool():
    global xy #specifying xy as a global variable
    xy=200 #global variable
    print(xy)
cool() #200

print(xy)

#Example 4

xy=100 #global variables

def cool():
    global xy #specifying xy as a global variable
    xy=500 #global variable
    print(xy)
#cool() #500

print(xy)

#Example 5 #Global variables can also be used inside function by using global keyword

def cool():
    global xy
    xy=1000
    print(xy)
cool()
print(xy)