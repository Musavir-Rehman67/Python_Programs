# reading a file
f  = open("test.txt","r")
print(f.read())
print(f.read(5))
print(f.readlines())
for x in f:
    print(x)
f.close()

# writing and appending a file
f = open("test1.txt","a")
f.write("Haroon is a scrum master for our team for first weak")
f.close()
f = open("test1.txt","r")
print(f.readline())

f = open("test_writing.txt","w")
f.write("I have deleted the content")
f.close()

f = open("test_writing.txt","r")
print(f.read())


# create a new file

f = open("myfile.txt","x")


import os
if os.path.exists("E:test_writing.txt"):
    os.remove("test_writing.txt")
else:
    print("The file does not exists")
# os.remove("test_writing.txt")


# Delete a folder
os.mkdir("E:myfolder")
# os.rmdir("myfolder")

