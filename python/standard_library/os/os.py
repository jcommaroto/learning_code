import os
#https://docs.python.org/3/library/os.html

print("Let's Get Some User Environment Information")
print(os.environ)
print(os.getenv("LOGNAME"))
system = os.uname()
print(system)
print(system[0])

print(os.name) 

print("Get the Current Directory")
print(os.getcwd()) #This funtion gets the current working directory

print("Make a New Folder")
directorycheck = os.path.exists("newdir") #This will check if a given directory exists
#Can also use os.path.isdir

if directorycheck != True:
    os.mkdir("newdir") #This will make a new directory
    print("Directory was not there so we are creating it")
else:
    print("Directory alread exists")

directory = os.getcwd() + "/newdir"

print("Changing to our directory")
print(os.chdir(directory)) #Changes into a directory

print("Now see our current working directory")
print(os.getcwd())

print("Let' Create a File")
fd = "GFG.txt"
fdcheck = os.path.exists(fd)

if fdcheck == True:
    print("The File Exists already")
    file = open(fd, 'r') 
    text = file.read() 
    print(text) 
    os.rename(fd, "new.txt")
else:
    file = open(fd, 'w') 
    file.write("Hello") 
    file.close() 
    file = open(fd, 'r') 
    text = file.read() 
    print(text)
    os.rename(fd, "new.txt")