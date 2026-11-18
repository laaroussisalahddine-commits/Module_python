def recursive(n : int) -> None:
    if (n <= 0):
        return 
    else:
        recursive(n - 1)
        print(f"Day {n}")

def ft_count_harvest_recursive():
    number = int(input("Days until harvest: "))
    recursive(number)
    print("Harvest time!")

ft_count_harvest_recursive()
