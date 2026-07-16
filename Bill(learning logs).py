"""Bill."""
price = float(input())
sevice = 0

if price < 500:
    service = 50
elif  price > 10000:
    service = 1000
elif price <= 0:
    service = 0
else:
    service = price / 10

vat = (service + price) * 0.07
total = service + vat + price
print(f"{total:.2f}")
