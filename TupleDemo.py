#Example 1 - Create a Tuple

mytuple=("apple", "banana", "cherry")
print(mytuple)

mytuple=() #empty tuple

#Example 2 - Accessing items from the tuple
mytuple=("apple", "banana", "cherry")
print(mytuple[1]) #banana - here index starts from 0

print(mytuple[-1]) #cherry

#Example 3 - Range of indexes
mytuple=("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
print(mytuple[2:5]) #('cherry', 'orange', 'kiwi')
print(mytuple[-4:-1]) # Negative values always count from end with index 1 #('orange', 'kiwi', 'melon')

#Example 4 - Changing Tuple Items
#by default tuple does not allow us to change the values because it is immutable
#but there is workaround

#tuple - list(modify) --> tuple

mytuple= ("apple","banana","cherry")
mylist=list(mytuple)
mylist[0]="orange"
mytuple=tuple(mylist)
print(mytuple)

#Example 5: reading tuple items using loop

mytuple=("apple","banana","cherry")
for i in mytuple:
    print(i)

#Example 6 : check if item exists in the tuple or not(searching of item in a tuple)
mytuple=("apple","banana","cherry")
if "banana" in mytuple:
     print("banana is present")
else:
    print("banana is not present")

#Example 7: Tuple length - counting items in a tuple
mytuple=("apple","banana","cherry")
len(mytuple)
print(len(mytuple))

#Example 8 : - Add items to tuple
#We can't add new items to the tuple because it is immutable
#mytuple=("apple","banana","cherry")
#mytuple[0]="orange" #TypeError - Tuple object doe not support item assignment
#print(mytuple)

#Example 9 : - Copy Tuple
mytuple1=("apple","banana","cherry")
mytuple2=mytuple1
print(mytuple2)

#Example 10 : Removing items from tuple - not possible because tuple is immutable
mytuple=("apple","banana","cherry")
#mytuple.remove("apple") #invalid statement
del mytuple
#print(mytuple) #NameError : name 'mytuple' is not defined

#Example 11 - Join/combine tuple
tuple1=(10,20,30)
tuple2=("a","b","c")
tuple3 = tuple1 +tuple2
print(tuple3) #(10, 20, 30, 'a', 'b', 'c')

#Example 12 - Tuples comparison
tuple1=(10,20,30)
#tuple2=("a","b","c")
tuple2=(10,20,30)
if tuple1==tuple2:
    print("tuples are equal")
else:
    print("tuples are not equal")

