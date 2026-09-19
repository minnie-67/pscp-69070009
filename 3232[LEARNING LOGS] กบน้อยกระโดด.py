"""กบน้อยกระโดด"""
x, y = map(int, input().split())
distance = 0 #กระโดดไปแล้วกี่เมตร
jump = x #กระโดครั้งนี้ได้กี่เมตร
count = 0 #กระโดดกี่ครั้งแล้ว

while distance < y and jump > 0: #ถ้าระยะรวมยังน้อยกว่าyให้ทำต่อและไม่อยากให้ระยะโดดเป็นลบ
    distance += jump
    count += 1
    jump -= 2

if distance >= y:
    print(count)
else:
    print(-1)
