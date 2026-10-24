"""[LEARNING LOGS] B - Fully pair?"""

text = input()
count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

result = ""

for char in text:
    if count[char] % 2 == 1:
        result += char
        count[char] = 0

if not result:
    print("fully paired")
else:
    print(result)
