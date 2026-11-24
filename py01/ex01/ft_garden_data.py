class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print (f"{self.name}: {self.height}cm, {self.age} days old")
def ft_garden_data()->None:
    p1 = Plant("Rose", 30, 25)
    p2 = Plant("Sunflower", 45, 80)
    p3 = Plant("Cactus", 120, 15)
    print("=== garden Plant Registry ===")
    p1.show()
    p2.show()
    p3.show()

if __name__ == "__main__":
    ft_garden_data()
