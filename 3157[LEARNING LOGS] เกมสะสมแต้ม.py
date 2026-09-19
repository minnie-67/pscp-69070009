"""เกมสะสมแต้ม"""
n = int(input())
total = 0

for _ in range(n):
    d = input()

    if d == "+":
        total += 10
    elif d == "-":
        total -= 5

print(total)
