# asks user for their name
name = input("Please enter your name: ")

# prints user's name
print("Welcome " + name + ".")

# asks user for age
age = input("How old are you? ")

# converts age str into an int
age = int(age)

# adds 10 to age
age = age + 10

# prints all
print("Guess what, " + name + "? You will be " + (str(age)) + " in 10 years!")