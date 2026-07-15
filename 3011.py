"""Colors."""
color1 = input().capitalize()
color2 = input().capitalize()

if color1 == "Red" and color2 == "Yellow":
    print("Orange")
elif color1 == "Red" and color2 == "Blue":
    print("Purple")
elif color1 == "Yellow" and color2 == "Blue":
    print("Green")
elif color1 == "Red" and color2 == "Red":
    print("Red")
elif color1 == "Yellow" and color2 == "Yellow":
    print("Yellow")
elif color1 == "Blue" and color2 == "Blue":
    print("Blue")
else:
    print("Error")
