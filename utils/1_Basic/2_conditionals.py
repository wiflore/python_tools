def age_foo(age):
    new_age = float(age) + 50
    return new_age


def less_than(age):
    if age < 125:
        print("ok")
    elif age == 5:
        print("Perfect")
    else:
        print ("LoL Si como no")

age = input("enter the number: ")
less_than(age_foo(age))
