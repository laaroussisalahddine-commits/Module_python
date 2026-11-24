class Plant:
    def __init__(self, Name, Age, Height, growth_rate) -> None :
        self.Name = Name
        self.Age = Age
        self.Height = Height
        self.growth_rate = growth_rate

    def grow(self) ->None :
        self.Height += self.growth_rate
        self.Height = round(self.Height, 1)

    def age(self) -> None :
        self.Age += 1
    
    def show(self):
        print (f"{self.Name}: {self.Height}cm, {self.Age} days old")

def ft_garden_growth() -> None :
    print("=== garden Plant Growth ===")
    p1 = Plant("Rose", 30, 25, 0.8)
    initial_height = round(p1.Height, 1)
    p1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.age()
        p1.grow()
        p1.show()
    growth = round(p1.Height - initial_height, 1)
    print(f"Growth this week: {growth}cm")

if __name__ == "__main__":
    ft_garden_growth()
