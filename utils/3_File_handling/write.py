file = open("example2.txt", 'w')
file.write("Line 1")
file.close()

#it overwrite
file = open("example2.txt", 'w')
file.write("Line 2\n")
file.close()

#it \n

file = open("example2.txt", 'w')
file.write("Line 1\n")
file.write("Line 2\n")
file.close()

file = open("example3.txt", 'w')
l = ["line1", "line2", "line2"]
for item in l:
    file.write(item+"\n")
file.close()