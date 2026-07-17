"""คะแนนสอบ"""
rabbit = int(input())
max_score = 0
top = 0

for i in range(rabbit):
    score = int(input())
    if score > max_score:
        max_score = score
        top = 1
    elif score == max_score:
        top += 1

print(max_score)
print(top)
