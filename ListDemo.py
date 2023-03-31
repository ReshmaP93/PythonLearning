#Example1 : how to create a list

mylist1 = [10,20,30,40,50]
mylist2 = ["welcome","banana","cherry"]
mylist3 = ["banana",10,"cherry"]
mylist = list()


print(mylist1)
print(mylist2)
print(mylist3)
print(mylist)

#Example 2 Accessing items from the list

mylist=["banana", "cherry", "apple"] #index starts from 0

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1]) #Negative value means that counts from the end of the list
print(mylist[-2])

#Example 3 - Range of indexes

mylist=["apple","banana","cherry","dragonfruit","kiwi","melon","mango"]
print(mylist[2:5]) #['cherry', 'dragonfruit', 'kiwi']
#Index starts from 0 and ends with n-1

mylist=["apple","banana","cherry","dragonfruit","kiwi","melon","mango"]
print(mylist[-4:-1]) #['dragonfruit', 'kiwi', 'melon']
#Index always starts from 0 either from end to beginning or beginning to end

#Example 4 - Change Item Values

mylist=["apple","banana","cherry"]

print(mylist) #['apple', 'banana', 'cherry']

mylist[0]='orange' #this will change the values based on index
print(mylist[0])

#Example 5 - read items using loop statement
mylist=["apple","banana","cherry"]

for i in mylist:
     print(i)

#Example 6 - check if the item exist in the list or not
mylist=["apple","banana","cherry"]

if "apple" in mylist:
    print("yes", "apple is present in mylist")
else:
    print("no","apple is not present in mylist")

#Example 7 - length(counting number of items in a list)
mylist=["apple","banana","cherry"]
len(mylist)
print(len(mylist))

#Example 8 - Add items - append() insert()
mylist=["apple","banana","cherry"]
mylist.append("orange") #adding new item at the end of the list - append()
print(mylist) #['apple', 'banana', 'cherry', 'orange']

mylist=["apple","banana","cherry"]
mylist.insert(1,"kiwi") #adding item somewhere in the middle of the list based on index
print(mylist) #['apple', 'kiwi', 'banana', 'cherry']

#Example 9 - Remove item from the list
#pop()
mylist=["apple","banana","cherry"]
mylist.pop(0)#here we should specify only the index not value
print(mylist)

#del
mylist=["apple","banana","cherry"]
del mylist[2] #del command removes the single item based on the index
print(mylist) #['apple', 'banana']

#clear
mylist=["apple","banana","cherry"]
mylist.clear()
print(mylist) #[]

#Example 10 - Copy List
#list()
mylist1=["apple","banana","cherry"]
mylist2=list(mylist1)

print(mylist1) #['apple', 'banana', 'cherry']
print(mylist2) #['apple', 'banana', 'cherry']

#copy()
mylist1=["apple","banana","cherry"]
mylist2=mylist1.copy()

print(mylist1) #['apple', 'banana', 'cherry']
print(mylist2) #['apple', 'banana', 'cherry']

#Example 11 - Combine/Join two lists

#using '+' operator
list1 = ['a','b','c']
list2 = ['1,2,3']
list3 = list1+list2
print(list3) #['a', 'b', 'c', '1', '2', '3']

#using looping statement
list1 = ['a','b','c']
list2 = [1,2,3]

for i in list2:
    list1.append(i)
    print(list1) #['a', 'b', 'c', 1]
                 #['a', 'b', 'c', 1, 2]
                #['a', 'b', 'c', 1, 2, 3]
#using extend()
list1 = ['a','b','c']
list2 = [1,2,3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]

# Example -lists comparison
list1=[10,20,30]
#tuple2=("a","b","c")
list2=[10,20,30]
if list1==list2:
    print("lists are equal")
else:
    print("lists are not equal")