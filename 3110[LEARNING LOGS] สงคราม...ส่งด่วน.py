"""สงคราม...ส่งด่วน"""
def main():
    """ojoiso"""
    start, end = input().upper().split()
    weight = float(input())
    fee = 0
    fee_w = 0
    found = ""

    if start == "BKK" and end == "CNX":
        fee = 10
        fee_w = 30
        found = True
    elif start == "CNX" and end == "UBP":
        fee = 15
        fee_w = 40
        found = True
    elif start == "UBP" and end == "BKK":
        fee = 20
        fee_w = 40
        found = True
    elif start == "BKK" and end == "PKT":
        fee = 25
        fee_w = 50
        found = True
    elif start == "PKT" and end == "CNX":
        fee = 30
        fee_w = 60
        found = True
    elif start == "UBP" and end == "PKT":
        fee = 40
        fee_w = 70
        found = True

    if found:
        price = fee + (fee_w * weight)
        print(f"{price:.2f}")
    else:
        print("Error")
main()
