"""BigFrame"""
p = []

for i in range(5):
    p.append(input().rstrip())

max_len = 0

for i in p:
    if len(i) > max_len:
        max_len = len(i)

print("*" * (max_len + 4))

for i in p:
    print("*", i.ljust(max_len), "*")

print("*" * (max_len + 4))
