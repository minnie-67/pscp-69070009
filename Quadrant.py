"""Quadrant."""
x = int(input())
y = int(input())

if not x and not y:
    print("o")
elif not x:
    print("y")
elif not y:
    print("x")
elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
else:
    print("Q4")
