import os

print("Get the Current Directory")
print(os.getcwd())

print("Make a New Folder")
os.mkdir("newdir")

directory = os.getcwd() + "/newdir"

print("New Folder Made, Let's Go to It")
print(os.chdir(directory))

print("Now see our current working directory")
print(os.getcwd())
