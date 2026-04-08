username = input("Enter your name:")
print(username)

usernameInBank = "Abu Hurairah"
pinInBank = "0123"

if usernameInBank == username:
    print("Welcome", username.upper())
    pin = input("Enter your pin:")
    print(pin)
    if pinInBank == pin:
        print("Login successful")
    else:
        print("Invalid pin")
else:
    print("Invalid username")

#  Built in functions for string in python


# age = int(input("Enter your age: "))
# print(age + 1)

# print(username.upper(),username)
# print(username.lower(),username)
# print(username.swapcase(),username)
# print(username.title(),username)
# print(username.strip(),username)
# print(username.lstrip(),username)
# print(username.rstrip(),username)
# print(username.replace("a","Z"),username)
# print(len(username))
# print(username.find("a"))
# print(username.count("a"))
# print(username.startswith("A"))
# print(username.endswith("a"))

