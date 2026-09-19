"""สลากกินแบ่ง"""
win = input().split()
buy = input().split()

if win == buy:
    print(1000000)
elif win[1] == buy[1] and win[0] != buy[0]:
    print(100000)
elif win[0] == buy[0] and win[1][-3:] == buy[1][-3:]:
    print(2000)
elif win[0] == buy[0] and win[1][-2:] == buy[1][-2:]:
    print(1000)
elif win[0] != buy[0] and win[1][-3:] == buy[1][-3:]:
    print(200)
elif win[0] != buy[0] and win[1][-2:] == buy[1][-2:]:
    print(100)
elif win[0] == buy[0] and win[1] != buy[1]:
    print(20)
elif win[0] != buy[0] and win[1] != buy[1]:
    print(0)
