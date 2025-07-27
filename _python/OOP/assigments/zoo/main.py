

class Animal:
    def __init__(self, name, age=1, health_level=50, happiness_level=50):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health Level: {self.health_level}, Happiness Level: {self.happiness_level}")

class Lion(Animal):
    def __init__(self, name, age=1, health_level=50, happiness_level=50, roar_power=114):
        super().__init__(name, age, health_level, happiness_level)
        self.roar_power = roar_power

    def feed(self):
        self.health_level += 20
        self.happiness_level += 10
        print(f"Thank you for feeding the Lion {self.name}")

    def display_info(self):
        super().display_info()
        print(f"I'am a Lion and my Roar Power is: dB {self.roar_power}")

# **********************************************************
class Cheetah(Animal):
    def __init__(self, name, age=1, health_level=50, happiness_level=50, speed=112):
        super().__init__(name, age, health_level, happiness_level)
        self.speed = speed

    def feed(self):
        self.health_level += 12
        self.happiness_level += 18
        print(f"Thank you for feeding the Cheetahs {self.name}")

    def display_info(self):
        super().display_info()
        print(f"I'am a Cheetah and my Speed is: km/h {self.speed}")

# **********************************************************
class Elephant(Animal):
    def __init__(self, name, age=1, health_level=50, happiness_level=50, weight=5):
        super().__init__(name, age, health_level, happiness_level)
        self.weight = weight

    def feed(self):
        self.health_level += 13
        self.happiness_level += 66
        print(f"Thank you for feeding the Elephant {self.name}")

    def display_info(self):
        super().display_info()
        print(f"I'am an Elephant and my weight is: ton {self.weight}")

# **********************************************************
class Zebra(Animal):
    def __init__(self, name, age=1, health_level=50, happiness_level=50, stripes = 400):
        super().__init__(name, age, health_level, happiness_level)
        self.stripes = stripes

    def feed(self):
        self.health_level += 40
        self.happiness_level += 30
        print(f"Thank you for feeding the Zebra {self.name} ")

    def display_info(self):
        super().display_info()
        print(f"I'am a Zebra and my Stripes number is: Stripe {self.stripes}")


class Zoo:
    def __init__(self, Zoo_name):
        self.animals = []
        self.name = Zoo_name
    def add_lion(self, name, age=1, health_level=50, happiness_level=50, roar_power=114):
        self.animals.append(Lion(name, age, health_level, happiness_level, roar_power))
        return self

    def add_cheetah(self, name, age=1, health_level=50, happiness_level=50, speed=112):
        self.animals.append( Cheetah(name, age, health_level, happiness_level, speed))
        return self

    def add_elephant(self, name, age=1, health_level=50, happiness_level=50, height=5):
        self.animals.append( Elephant(name, age, health_level, happiness_level, height))
        return self
    
    def add_zebra(self, name, age=1, health_level=50, happiness_level=50, stripes = 400 ):
        self.animals.append( Zebra(name, age, health_level, happiness_level, stripes))
        return self


    def print_all_info(self):
        print("_"*30, self.name, "_"*30)
        for animal in self.animals:
            animal.display_info()
        return self
    
    def feed_all_animals(self):
        for animal in self.animals:
            animal.feed()
        return self
        

SpaceToon = Zoo("Space Toon's Zoo")
SpaceToon.add_lion("Scar",30, 60, 30, 90).add_cheetah("Bagheera", 20,).add_elephant("Babar", 40, 80, 100).print_all_info().feed_all_animals().print_all_info()

Qalqilya = Zoo("Qalqilya's Zoo")
Qalqilya.add_lion("asad t3ban", 60, 1, -50, 2).add_zebra("ne7", 10, 80, 90).print_all_info().feed_all_animals().print_all_info()
