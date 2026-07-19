"""ปราสาท."""
x = int(input())

floor = 1
while floor  ** 2 < x:
    floor += 1
far = (floor**2) - x
room = 2*(floor) - 1
if not far % 2:
    print(room - 1)
else :
    print(room - 2)
