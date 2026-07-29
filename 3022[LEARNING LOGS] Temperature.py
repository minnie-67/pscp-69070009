"""Temperature"""
temp = float(input())
unit1 = input()
unit2 = input()

if unit1 == "C":
    celsius = temp
elif unit1 == "F":
    celsius = (temp - 32) * 5 / 9
elif unit1 == "K":
    celsius = temp - 273.15
else:
    celsius = (temp - 491.67) * 5 / 9

if unit2 == "C":
    result = celsius
elif unit2 == "F":
    result = celsius * 9 / 5 + 32
elif unit2 == "K":
    result = celsius + 273.15
else:
    result = (celsius + 273.15) * 9 / 5

print(f"{result:.2f}")