"""season"""

def main():
    """main"""
    month = int(input())
    day = int(input())

    if month in [1,2,3]:
        Season = "winter"
    elif month in [4,5,6]:
        Season = "spring"
    elif month in [7,8,9]:
        Season = "summer"
    elif month in [10,11,12]:
        Season = "fall"

    if not month % 3 and day >=21:
        if Season == "winter":
            Season = "spring"
        elif Season == "spring":
            Season = "summer"
        elif Season == "summer":
            Season = "fall"
        elif Season == "fall":
            Season = "winter"

    print(Season)

main()
