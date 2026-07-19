"""หาร10"""
num = int(input())

ten = (num // 10) * 10
for i in range(ten, -1, -10):
    print(i, end = " ")
