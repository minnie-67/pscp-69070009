"""season."""
month = int(input())
day = int(input())

if month in [1, 2, 3]:
    season = "winter"
elif month in [4, 5, 6]:
    season = "spring"
elif month in [7, 8, 9]:
    season = "summer"
elif month in [10, 11, 12]:
    season = "fall"

if not month % 3 and day >= 21:
    if season == "winter":
       season = "spring"
    elif season == "spring":
        season = "summer"
    elif season == "summer":
        season = "fall"
    elif season == "fall":
        season = "winter"
print(season)
