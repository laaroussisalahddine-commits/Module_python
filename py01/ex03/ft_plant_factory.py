class Plant:
    def __init__(self, name : str, height : float, age : int) -> None :
        self.name = name
        self.age_days = age
        self.height = height

    def grow(self) ->None :
        self.height += 0.0
        self.height = round(self.height, 1)

    def age(self) -> None :
        self.age_days += 0

    def show(self) -> None :
        print (f"Created: {self.name}: {self.height:.1f}cm, {self.age_days} days old")

def ft_plant_factory()->None:
    plants1: Plant = Plant("Rose", 25, 30)
    plants2: Plant = Plant("Oak", 200, 365)
    plants3: Plant = Plant("Cactus", 5, 90)
    plants4: Plant = Plant("Sunflower", 80, 45)
    plants5: Plant = Plant("Fern", 15, 120)
    
    print("=== Plant Factory Output ===")
    string : list[plant] = [plants1, plants2, plants3, plants4, plants5]
    for p in string :
        p.show()

if __name__ == "__main__":
    ft_plant_factory()
