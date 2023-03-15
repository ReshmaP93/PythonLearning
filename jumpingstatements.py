#break continue

#for i in range(1,10):
    #if i==5:
       #break
    #print(i)
#print("Exited from the loop")

for i in range(1,10):
     if i==5:
        continue
     print(i)
print("Exited")

#skip some random values
for i in range(1,10):
     if i==3 or i==5 or i==7:
        continue
     print(i)
print("Exited")

