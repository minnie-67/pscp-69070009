"""[LEARNING LOGS] Giraffe"""
n = int(input())
count = 0
x = []

for i in range(n):
    x.append(int(input()))

if n == 1:
    count += 1
else:
    if x[0] > x[1]: #ตัวแรกมันไม่มีตัวซ้ายเลยต้องเขียนแยก
        count += 1

    if x[n - 1] > x[n - 2]: #ตัวสุดท้ายมันไม่มีตัวขวาเลยต้องเขียนแยก
        count += 1

    for i in range(1, n - 1): #ไม่นับตัวแรกกับไม่กับตัวสุดท้ายเพราะเขียนแยกไว้แล้ว
        if x[i] > x[i + 1] and x[i] > x[i - 1]:
            count += 1

print(count)
