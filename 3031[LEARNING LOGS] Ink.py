"""Ink"""
import math
def main():
    """Find flooding time"""
    speed,people = map(int, input().split())
    for _ in range(people):
        x, y = map(int, input().split())
        area = 3.1416 * (x ** 2 + y ** 2)
        time = math.ceil(area / speed)
        print(time)
main()
