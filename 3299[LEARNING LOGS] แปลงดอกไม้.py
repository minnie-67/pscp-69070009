"""แปลงดอกไม้"""

L, N = map(int, input().split())

band = 1

while band * L * (band * L + 1) // 2 < N:
    band += 1

print(band)
