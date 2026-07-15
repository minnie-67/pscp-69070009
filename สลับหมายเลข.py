"""สลับหมายเลข"""
number = int(input())
operator = input()

tens = number // 10
ones = number % 10

reverse = ones * 10 + tens

if operator == "+":
    resuit = number + reverse
    print(number , "+" , reverse , "=" , resuit)
elif operator == "*":
    resuit = number * reverse
    print(number , "*" , reverse , "=" , resuit)
