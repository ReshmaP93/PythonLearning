#Example 1 - Creating a set
myset={"apple","banana","cherry"}
print(myset)

#Example2 - Accessing items/values from set
myset={"apple","banana","cherry"}
for i in myset:
     print(myset)

#Example 3 - Value exists in set or not
myset={"apple","banana","cherry"}

print("banana"  in myset) #true
print("banana1"  in myset) #false

#Example 4 - Adding items to set
#add() - add only single item to the set
#update() - add multiple items to the set
myset={"apple","banana","cherry"}
myset.add("orange")
myset.update(["mango","kiwi"])
print(myset) #{'apple', 'orange', 'banana', 'cherry'}

#Example 5 - Find number of items in the set
myset={"apple","banana","cherry"}
print(len(myset)) #3

#Example 6 - To remove item from the set - remove() and discard()
myset={"apple","banana","cherry"}
myset.remove("banana")
print(myset) #{'cherry', 'apple'}
#myset.remove("xyz") #KeyError: 'xyz
##########################################
myset.discard("banana")
print(myset)
#myset.discard("xyz") # this will not throw any error
print(myset)

#Example 7 - To clear all the items from the set
#myset={"apple","banana","cherry"}
myset.clear()
print(myset) # set()

del myset
#print(myset) #NameError: name 'myset' is not defined

#Example 8 - To join two sets - union()
set1 = {"a,b,c"}
set2 = {"1,2,3"}
set3 = set1.union(set2)
print(set3)

#update()
set1 = {"a,b,c"}
set2 = {"1,2,3"}
set1.update(set2)
print(set1)
