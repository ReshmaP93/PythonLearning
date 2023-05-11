#Example 1 writing data into text file
file=open("D:\DemoFiles\mytext",'w')
file.write("this is my first statement..\n")
file.write("this is my second statement..\n")
file.write("this is my third statement..\n")
file.write("this is my fourth statement..\n")
file.write("this is my fifth statement..\n")
file.close()
print("program completed")

#Example 2 reading data from text file
file=open("D:\DemoFiles\mytext",'r')
print(file.read())
file.close()

#Example 3  Appending data into text file
file=open("D:\DemoFiles\mytext",'a')
file.write("\n This is my sixth line\n")
file.write("This is my seventh line\n")
file.close()
print("program is completed")