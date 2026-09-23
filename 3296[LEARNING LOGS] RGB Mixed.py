"""RGB Mixed"""
colour1 = list(map(int, input().split()))
colour2 = list(map(int, input().split()))

op = []

for i in range(3):
    op.append((colour1[i] + colour2[i]) // 2)

print(*op)
