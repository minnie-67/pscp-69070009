"""[LEARNING LOGS] ของขวัญและขโมย"""
n, k, t = map(int, input().split())

if t == 1:
    print(1)
else:
    person = 1
    count = 1

    while True:
        person = (person + k - 1) % n + 1

        if person == t:
            count += 1
            break

        if person == 1:
            break

        count += 1

    print(count)
