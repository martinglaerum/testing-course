import random

class Aquarium:
    def __init__(self):
        self.fish = []
        self.plants = []

    def add_fish(self, fish):
        self.fish.append(fish)

    def add_plant(self, plant):
        self.plants.append(plant)

    def feeding_time(self, food_amount):
        amount_of_hungry = self.who_is_hungry()
        if (amount_of_hungry == 0):
            print("No fish are hungry")
            return 1
        tiny_food_amount = food_amount / amount_of_hungry
        print(f"Feeding {amount_of_hungry} creatures with a total of {food_amount}, meaning {tiny_food_amount} to each creature")
        for plant in self.plants:
            if plant.am_I_hungry() == True:
                plant.feed_me(tiny_food_amount)
                print(plant)
        for fishy in self.fish:
            if fishy.am_I_hungry() == True:
                fishy.feed_me(tiny_food_amount)
                print(fishy)


    def who_is_hungry(self):
        hungry_stuff_amount = 0 
        for plant in self.plants:
            if plant.am_I_hungry() == True:
                hungry_stuff_amount += 1
                print(plant)
        for fishy in self.fish:
            if fishy.am_I_hungry() == True:
                hungry_stuff_amount += 1
                print(fishy)
        return hungry_stuff_amount

    def go_to_bed(self):
        for fish in self.fish:
            eaten = random.randint(1, 5)
            fish.food -= eaten
            if fish.food < 0:
                fish.food = 0

            print(f"{fish.name} ate {eaten} food while you slept.")

        for plant in self.plants:
            eaten = random.randint(1, 5)
            plant.food -= eaten
            if plant.food < 0:
                plant.food = 0

            print(f"{plant.name} used {eaten} food while you slept.")

class Fish():
    def __init__(self, name, food = 0):
        self.name = name
        self.food = food

    def feed_me(self, amount):
        self.food += amount * 0.6

    def am_I_hungry(self):
        return self.food < 10

    def __str__(self):
        if self.am_I_hungry() == True:
            return f"{self.name} needs food"
        return f"{self.name} does not need food"

class Plant():
    def __init__(self, name, food = 0):
        self.name = name
        self.food = food

    def feed_me(self, amount):
        self.food += amount * 0.5

    def am_I_hungry(self):
        return self.food < 15

    def __str__(self):
        if self.am_I_hungry() == True:
            return f"{self.name} needs food"
        return f"{self.name} does not need food"


def main():
    goldfish = Fish("Goldfish", 8)
    clownfish = Fish("Clownfish",3)
    seaweed = Plant("Seaweed",11)
    kelp = Plant("Kelp",6)
    my_Aquarium = Aquarium()

    my_Aquarium.add_fish(goldfish)
    my_Aquarium.add_fish(clownfish)
    my_Aquarium.add_plant(seaweed)
    my_Aquarium.add_plant(kelp)

    choice = 100
    while choice != 0:
        choice = int(input("Do you want to feed (1), go to bed (2) or Quit (0): "))

        if choice == 1:
            food_amount = int(input("How much food do you want to give your Aquarium? "))
            my_Aquarium.feeding_time(food_amount)

        elif choice == 2:
            my_Aquarium.go_to_bed()
            print("\nAfter sleeping:")
            my_Aquarium.who_is_hungry()

        else:
            print("IDIOT")

if __name__ == "__main__":
    main()