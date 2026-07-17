"""Calculate the buffet cost."""
x = int(input())
y = int(input())
a = int(input())
z = int(input())

come = z // x
pay = z % x

total = (come * y + pay) * a
print(total)
