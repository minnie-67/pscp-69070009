"""หารลงตัว"""
x = int(input())
y = int(input())
0 <= x < 1000 and 0 <= y < 1000

if x % y == 0:
    print("yes")
else:
    print("no")
