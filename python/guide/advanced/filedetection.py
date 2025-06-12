# Python file detection

# To detect files in Python, we will import the os module:
import os

# Let's make a video of file_path:
file_path = "/home/swanb/Documents/my-projects/python/guide/advanced/filedetection.txt" #It can be an absolute path
# Or a relative path

# We will need an if-else statement for this:
if os.path.exists(file_path):
    print(f"the file exists")
    if os.path.isfile(file_path): #you can detect file property
        print("that is a file")
    elif os. # TODO: finish ts
else:
    print(f"the file does not exist")
