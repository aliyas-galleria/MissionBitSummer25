
class Pet:
    def __init__(self, name, animal_type, hunger = 50, happiness = 50):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.happiness = happiness

    def eat(self):
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 10)
        print(f"{self.name} has eaten.")
        print(f"Hunger is now {self.hunger}.")
   
    def play(self):
        if self.happiness < 100:
            self.happiness = min(100, self.happiness + 10)
            self.hunger = max(0,self.hunger + 5)
        print(f"{self.name} played and is happier!")
        print(f"Happiness: {self.happiness}, Hunger: {self.hunger}")
   
    def status(self):
        print(f"Pet: {self.name}, Hunger: {self.hunger}, Type: {self.animal_type}, Happiness: {self.happiness}")

num_of_pets = int(input("How many pets would you like to create? "))
pets = []

for pet in range(num_of_pets):
    name = input("What's the pet's name? ")
    type_of_animal = input("What type of animal is it? ")
    pet_create = Pet(name, type_of_animal)
    pets.append(pet_create)

for pet in pets:
    pet.status()

for menu in pets:
    print("What would you like to do?")
    print("1. Feed a pet")
    print("2. Play with a pet")
    print("3. Check a pet's status")
    print("4. Exit")
    choose = input("Enter a number to select one of these actions ")
    print(choose)
    if choose == "1":
        print(pets)
    elif choose == "2":
        print(pets)
    elif choose == "3":
        print(pets)
    elif choose == "4":
        print("Exit")


