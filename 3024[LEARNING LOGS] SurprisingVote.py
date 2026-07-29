"""SurprisingVote"""
total = float(input())
maximum = float(input())

minimum = total - (maximum * 2)
if maximum - minimum > 2:
    print("Surprising")
else:
    print("Not surprising")
