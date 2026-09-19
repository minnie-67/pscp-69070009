"""Arcade of Time : Store Check"""


def main():
    """Count open stores at each check time."""
    num, check = map(int, input().split())

    diff = [0] * 1442

    for _ in range(num):
        start, stop = map(int, input().split())
        diff[start] += 1
        diff[stop] -= 1

    count = [0] * 1441
    current = 0

    for minute in range(1441):
        current += diff[minute]
        count[minute] = current

    times = list(map(int, input().split()))

    result = []
    for i in range(check):
        result.append(str(count[times[i]]))

    print(" ".join(result))


main()
