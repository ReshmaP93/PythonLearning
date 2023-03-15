#conditional statements

#if if else elif

#Example 1 - Print a person is eligible for vote or not
#age=20

age=20
if age>=18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")

#Example 2 -

if True:
    print("true condition")
else:
    print("false condition")

#Example 3
if 1:
    print("1")
else:
    print("not 1")

#Example 4 - Find a number is even or odd num%2 remainder 0

num=10

if num%2==0:
    print("Even")
else:
    print("Odd")

#Example 5 -if else in single line -(ternary operator)

mum=10
print("even") if num%2==0 else print("odd")

#Example 6 - multiple if else statements in a single line

a=30
{print("hello"), print("python")} if a>=20 else {print("hi"), print("java")}


#Example 7 - Multiple conditions using elif

weekno=7

if weekno==1:

   print("sunday")

elif (weekno==2):
    print("monday")

elif (weekno==3):
     print("tuesday")

elif (weekno == 4):
     print("wednesday")

elif (weekno==5):
     print("thursday")

elif (weekno==6):
     print("friday")

elif (weekno==7):
     print("saturday")

else:
    print("invalid weekno")

#Example 8 - check whether the number is positive or negative
num=float(input("Enter a number:"))
if num>=0:
    print("num is positive")
elif num==0:
    print("zero")
else:
    print("num is negative")

#Example 9 - check whether the num is largest or not

num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))
if num1>num2 and num1>num3:
    print("num1 is greater")
if num2>num3 and num2>num1:
    print("num2 is greater")
if num3>num1 and num3>num2:
    print("num3 is greater")

#Example 10 - Print week number if you provide weekname as input

weekname = monday
if weekname==sunday:
    print("1")
elif(weekname==monday):
    print("2")
elif (weekname == tuesday):
    print("3")
elif (weekname == wednesday):
    print("3")
elif (weekname == thursday):
    print("4")
elif (weekname == friday):
    print("5")
elif (weekname == saturday):
    print("6")
else:
    print("invalid weekname")


