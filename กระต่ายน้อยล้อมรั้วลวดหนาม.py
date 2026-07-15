"""กระต่ายน้อยล้อมลวดหนาม"""
Width, length, layer = map(int, input().split())
price_per_meter = int(input())

total = 2 * (Width + length) * layer
print(total)
print(total * price_per_meter)
