emails = ['me@gmail.com', 'you@hotmail.com', 'they@gmail.com']
print(dir(emails))
print((emails.__len__()))
print((emails.__iter__()))
for item in emails:
    if 'gmail' in item:
        print(item)

password = ''

while password != 'python123':
    password = input("Enter password: ")
    if password == 'python123':
        print("You are logged in!")
    else:
        print("Sorry, try again!")


names = ['james', 'john', 'jack']
email_domains = ['gmail', 'hotmail', 'yahoo']

#use zip to iterate over two list

for i, j in zip(names, email_domains):
    print (i, j)