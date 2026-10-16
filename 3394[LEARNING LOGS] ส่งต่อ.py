"""[LEARNING LOGS] ส่งต่อ"""
n, s = map(int, input().split())

friends = []

for _ in range(n):
    friends.append(int(input()))

visited = set()
current = s

while current and current not in visited:
    visited.add(current)
    current = friends[current - 1]

print(len(visited))
