c = "Hi there!"
print(c[0], c[3], c[-1], c[0:2], c[3:6], c[:4])
print(c[-3:3])
print(c[2:])
print(c[-3:-1])
print(c[-3:])

c = ["H", 2, "Hello"]
print(c)
print(type(c[1]))
print(type(c[2]))
print(type(c[:2]))

print(dir(list))
c.append(3)
print(c)

help(c.remove)
c.remove(2)
print(c)
