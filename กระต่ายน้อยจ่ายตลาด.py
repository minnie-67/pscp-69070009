"""กระต่ายน้อยจ่ายตลาด"""
carrot, cabbage, tomato = map(int, input().split())

CARROT_PRICE = 10
CABBAGE_PRICE = 25
TOMATO_PRICE = 3

total_price = (carrot * CARROT_PRICE) + (cabbage * CABBAGE_PRICE) + (tomato * TOMATO_PRICE)
print(total_price)
