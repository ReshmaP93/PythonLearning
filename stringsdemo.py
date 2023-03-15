#create string variable

#Example1
#ways of creating string variables
s="welcome"
s='welcome'
s=str("welcome")
s=str('welcome')
name=str()

#creating empty string variables
name=""
name=''

print("name")

#mutable and immutable

#mutable - cannot change the value of variable anytime

#immutable - can change the value of variable anytime

#Strings are immutable
#Example 2
str1="welcome"
print(id("str1")) #3270322024560

str1=str1,"to python"
print(id("str1"))

#if the value is changed after updation, then it is immutable

#Example 3 - + and * with strings

str="welcome"
print(str+"programming")  #concatenation/joining
print(str*3)  #- output - #welcomewelcomewelcome

#Slicing - Cut the strings based on the strings we had provided
#starting index counts from 0
#ending index counts from 1
# -1 means removes the last character in a string
# -2 means removes the last 2 characters in a string
str="welcome"
print(str[1:3]) #el

print(str[:6]) #welcom

print(str[2:]) #lcome

print(str[1:-2]) #elco

print(str[1:-1]) #elcom

#Example5 - ord() and chr()
print(ord('A')) #65 returns ASCII code of the character
print(chr(65)) #A returns character represented by ASCII number

#Example 6 max() min() len() - maximum, minimum and length of characters

print(max("abc"))
print(min("abc"))
print(len("abc"))

#Example 7 - in, not in operators - returns true/false

s="welcome"
print("come" not in s)
print("lome"  not in s)

s="welcome"
print("come" in s)
print("lome"  in s)

#Example 8 - String comparison

print("tim"=="tie")
print("free"!="dom")
print("arrow">"aron")

#Example 9 - Testing Strings  - True/False
s="hi java 123"
print(s.isalnum()) #false
print("hi".isalpha()) #true
print("12".isdigit()) #true
print("first number". isidentifier())#false
print("hi". islower()) #true
print("JAVA".isupper()) #true
print(" ".isspace()) #true

#Example 10 - Searching for substrings

s="welcome to python"
print(s.endswith("thon")) #True
print(s.startswith("py")) #true
print(s.find("come")) #3
print(s.find("wel")) #true
print(s.count("t"))

#Example 11 - Converting Strings

s="string in python"
s1=s.capitalize() #String in python
print(s1)

s2=s.title() #String In Python
print(s2)

s3=s.upper() #STRING IN PYTHON
print(s3)

s4=s.lower() #string in python
print(s4)

s5=s.swapcase()  #It means upper to lower and lower to upper #STRING IN PYTHON
print(s5)

s6=s.replace("in", "on")
print(s6)

#Example 12 - how to reverse a string
#Method 1
s="welcome"
rev_str= ""

for i in s:
    rev_str=i+rev_str
    print("reversed string is:",rev_str)

#Method 2
s="welcome"
rev_str=s[::-1] #s[0:end:-1]
print(rev_str)


