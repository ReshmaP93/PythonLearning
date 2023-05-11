#Example 1

print("This is the starting point of the program...")
print("This is the starting point of the program...")
print("This is the starting point of the program...")
try:
    print(x)
except:
    print("Exception occured")
print("This is the ending point of the program..")
print("This is the ending point of the program..")
print("This is the ending point of the program..")

#Example 2
print("This is the starting point of the program...")
print("Program is in progress")
try:
    print(10/0) #ZeroDivisionError: division by zero
except ZeroDivisionError:
    print("Exception occured.. handled")
print("Program is completed..")

#Example 3
print("This is the starting point of the program...")
print("Program is in progress")
try:
    print(10/5)
except ZeroDivisionError:
    print("Exception occured.. handled")
print("Program is completed..")

#Example 4 - Multiple except blocks - try, except else, finally
try:
    num1, num2 = 10, 0
    result = num1 / num2
    print("result is :", result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError Exception")
except SyntaxError:
    print("Thrown SyntaxError exception")
except:
    print("Exception Handled")
else:
    print("no exceptions occurred")
finally:
    print("always executed")

#Example 4 - Raising our own exceptions
def age(num):
    if num<0:
       raise ValueError("Only Integers are allowed:")
    if num%2==0:
        print("even")
    else:
        print("odd")
print("checking whether the number is even or odd")

num=4
try:
   age(num)
except ValueError:
    print("ValueError exception occurred and handled..")
print("program is completed")