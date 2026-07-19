"""ปราสาท."""
x = int(input())

floor = 1
while floor  ** 2 < x:
    floor += 1
far = (floor**2) - x
ROOM = 2*(floor) - 1
if not far % 2:
    print(ROOM - 1)
else :
    print(ROOM - 2)
