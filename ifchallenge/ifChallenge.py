name = input("Enter your name: ")
age = int(input("Enter your age, {}: ".format(name)))

if 18 < age < 31:
    print("Welcome to the holiday {0}".format(name))
else:
    print("I am sorry {0}, you cannot come to this holiday.".format(name))