"""A-E-I-O-U"""
text = input().lower()
vowel = ["a", "e", "i", "o", "u"]
count = [0, 0, 0, 0, 0]

for you in text:
    for i in range(len(vowel)):
        if you == vowel[i]:
            count[i] += 1

for i in range(len(vowel)):
    if count[i] > 0:
        print(f"{vowel[i]} : {count[i]}")
