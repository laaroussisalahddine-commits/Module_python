def ft_water_reminder() -> None:
    Water = int(input("Days since last watering: "))
    if (Water > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
