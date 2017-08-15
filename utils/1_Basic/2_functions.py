def currency_converter(rate, euros):
    dollars = round(euros * rate, 4)
    return dollars

def currency_converter2(rate = 1, euros = 2):
    dollars = round(euros * rate, 4)
    print (dollars)

def age_foo(age):
    new_age = float(age) + 50
    return new_age


print(currency_converter(1.1, 3000))
print(type(currency_converter(1.1, 30403)))


currency_converter2(euros = 9)
currency_converter2(1.16, 2000)
print(type(currency_converter2(1.1, 30403)))

age = input("Enter you age: ")
print(age_foo(age))
