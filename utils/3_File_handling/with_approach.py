with open("example.txt", "a+") as doc:

    doc.seek(0)
    content = doc.read()
    doc.write("\nNEW LINE")

print (content)