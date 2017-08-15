file = open("example.txt", 'r')
print(type(file))
content = file.read()
print(content)
print(type(content))

content = file.readlines()
print(content)
print(type(content))

# File seek to work with the content of the file
file.seek(0)

print(dir(file))
content = file.readlines()
print(content)
print(type(content))

# strip content rstrip \n
content = [line.rstrip("\n") for line in content]
print (content)

file.close()

print (content)
