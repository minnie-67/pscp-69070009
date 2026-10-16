"""[LEARNING LOGS] หั่นขนมปัง"""
w, h, _, _ = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = [0] + x + [w]
y = [0] + y + [h]

widths = []
heights = []

for i in range(len(x) - 1):
    widths.append(x[i + 1] - x[i])

for i in range(len(y) - 1):
    heights.append(y[i + 1] - y[i])

widths.sort(reverse=True)
heights.sort(reverse=True)

first = widths[0] * heights[0]
second = max(widths[1] * heights[0],
             widths[0] * heights[1])

print(first, second)
