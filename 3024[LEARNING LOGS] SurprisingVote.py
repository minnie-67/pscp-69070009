"""SurprisingVote"""
total = float(input())
max = float(input())

min = total - (max * 2)
if max - min > 2:
    print("Surprising")
else:
    print("Not surprising")
