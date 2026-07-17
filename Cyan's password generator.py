"""Program to generate a password based on user input."""

name = input()
surname = input()
age = input()

if len(name) >= 5 and len(surname) >= 5:
    password = name[:2] + surname[-1] + age[-1]
else:
    password = name[0] + age + surname[-1]
print(password)
