"""ไพ่ 44 ใบ"""
card = input().upper()

tam = card[:-1] #เอาทุกตัวยกเว้นตัวสุดท้าย
dok = card[-1] #เอาแคตัวสุดท้าย

doks = ["diamonds", "hearts", "spades", "clubs"]
yor = ["D", "H", "S", "C"] #ตัวย่อ

if tam == "A":
    tam = "ace"
elif tam == "J":
    tam = "jack"
elif tam == "Q":
    tam = "queen"
elif tam == "K":
    tam = "king"

name = doks[yor.index(dok)]
#หาว่าdokที่inputมาอยู่ตัวที่เท่าไหร่ในlistของyor
#ถ้าสมมุติได้เป็นตัวที่สอง ก็เอามาดูตัวที่สองในlistของdoksต่อ ก็จะได้ตัวนั้น

print(tam + " of " + name)
