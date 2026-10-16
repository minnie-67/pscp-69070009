"""[LEARNING LOGS] Duplicate I"""
m = int(input())
n = int(input())

x = []
y = []

for _ in range(m):
    num = int(input())
    x.append(num)

for _ in range(n):
    num = int(input())
    y.append(num)

shown = []

for num in x:
    if num in y and num not in shown:
        shown.append(num)

shown.sort(reverse=True) #sortคือเรียงจากน้อยไปมาก แล้วrevverseคือย้อนกลับจากมากไปน้อย

if shown:
    for num in shown:
        print(num)
else:
    print("Nope")
