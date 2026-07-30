"""A-E-I-O-U"""
text = input().lower()
vowel = ["a", "e", "i", "o", "u"]
count = [0, 0, 0, 0, 0]

for ch in text:
    if ch == "a":
        count[0] += 1
    elif ch == "e":
        count[1] += 1
    elif ch == "i":
        count[2] += 1
    elif ch == "o":
        count[3] += 1
    elif ch == "u":
        count[4] += 1

for i in range(5):
    if count[i] > 0:
        print(f"{vowel[i]} : {count[i]}")
