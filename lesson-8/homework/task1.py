class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age)
        self.milk_production = milk_production

    def produce_milk(self):
        print(f"{self.name} produced {self.milk_production} liters of milk today.")


class Chicken(Animal):
    def __init__(self, name, age, egg_count):
        super().__init__(name, age)
        self.egg_count = egg_count

    def lay_eggs(self):
        print(f"{self.name} laid {self.egg_count} eggs today.")


class Sheep(Animal):
    def __init__(self, name, age, wool_quality):
        super().__init__(name, age)
        self.wool_quality = wool_quality

    def shear(self):
        print(f"{self.name} was sheared for {self.wool_quality} quality wool.")