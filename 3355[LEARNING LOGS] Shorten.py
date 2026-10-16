
"""[LEARNING LOGS] Shorten"""
x = int(input())

start = x
last = x
ans = []

while x != -1:
    x = int(input())

    if x == -1:
        if start == last:
            ans.append(str(start))
        else:
            ans.append(f"{start}-{last}")
        break

    if x == last + 1:
        last = x
    else:
        if start == last:
            ans.append(str(start))
        else:
            ans.append(f"{start}-{last}")

        start = x
        last = x

print(", ".join(ans))
