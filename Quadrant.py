"""Quadrant."""
x = int(input())
y = int(input())

if not x and y:
    print("O")
elif not x:
    print("X")
elif not y:
    print("Y")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")
