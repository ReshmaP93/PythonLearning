#Example 1 - Creating a Dictionary
#dic={key:"value"}
mydic={101:"x",102:"y",103:"z"}
print(mydic) #{101: 'x', 102: 'y', 103: 'z'}

#Example 2 - Access items in Dictionary
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
print(mydic["brand"]) #hyundai
print(mydic["model"]) #i1o
print(mydic["year"]) #2021

#Example 3 - using get() function
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
x=mydic.get("brand")
print(x)

#Example 4 - Change values in Dictionary
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
print(mydic)
mydic["year"]=2022
print(mydic)

#Example 5 - reading items from dictionary using loop
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
for i in mydic:
       print(i) #prints only keys from dictionary

for i in mydic:
       print(mydic[i]) #prints only values from dictionary

#Another way

for i in mydic.values():
       print(i) #hyundai
                #i1o
                #2021
#Another way - print keys along with values
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
for x,y in mydic.items():
       print(x,y)

#Example 6 - Check whether key exists in dictionary or not
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
if"model" in mydic:
       print("exist") #true
else:
       print("not exist") #false

#print("model" in mydic) #True

#Example 7 - Find total no. of items in Dictionary
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
print(len(mydic))

#Example 8 - Adding items to Dictionary
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
mydic["color"]="red"
print(mydic)

#Example 9 - Removve item from dictionary
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
mydic.pop("year")
print(mydic)

#Another way
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
del mydic["model"]
print(mydic)

#Delete the dictionary along with items
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
del mydic
#print(mydic) #NameError: name 'mydic' is not defined
#Clear
mydic={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
mydic.clear()
print(mydic) #{}

#Example 10 - Copying Dictionary
mydic1={
       "brand":"hyundai",
       "model":"i1o",
       "year":2021
       }
#with using copy()
mydic2=mydic1.copy()
print(mydic2) #{'brand': 'hyundai', 'model': 'i1o', 'year': 2021}
#without using copy()
mydic2=mydic1
print(mydic2) #{'brand': 'hyundai', 'model': 'i1o', 'year': 2021}