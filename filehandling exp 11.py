file=open("demo_file.txt","w")
file.write("hello! This is the first line.\n")
file.write("python file handling demonstration. \n")
file.close()


print("Data written successfully, \n")

file=open("demo_file.txt", "r")
print("reading file contents:")
content=file.read()
print(content)
file.close()


file=open("demo_file.txt", "a")
file.write("this line is added later using append mode. \n")
file.close()

print("data appemded succesfully. \n")

file=open("demo_file.txt", "r")
print("Updated file contents:")
updated_content=file.read()
print(updated_content)
file.close()

