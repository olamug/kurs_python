class Animal:
    eucaryont = True

    def __init__(self):
        print("Animals are multicellular eukaryotic organisms that consume organic material, breathe oxygen, "
              "are able to move, can reproduce sexually, and grow from a hollow sphere of cells, the blastula, "
              "during embryonic development.")

    def breathing(self):
        return "Oxygen"

    def feed(self):
        return "organic material"


class Mammal(Animal):

    vertebrate = True

    def __init__(self, enviroment = 0):
        self.enviroment = enviroment
        print("Mammals are vertebrate animals characterized by the presence of mammary glands which in females "
              "(and sometimes males) produce milk for feeding (nursing) their young")

    def feed(self):
        return "milk"

    def show_description(self):
        super().__init__()

class Cat(Mammal):
    def __init__(self, enviroment = 0):
        print("The cat (Felis catus) is a small carnivorous mammal. It is the only domesticated species in the family "
              "Felidae and often referred to as the domestic cat to distinguish it from wild members of the family.")
        self.enviroment = enviroment

    def feed(self):
        return "whiskas"

    def show_description(self):
        super().__init__()


class Dog(Mammal):

    def __init__(self, enviroment = 0):
        print("The domestic dog is a member of the genus Canis (canines), which forms part of the wolf-like canids and "
        "was the first species to be domesticated and has been selectively bred over millennia for various "
        "behaviors, sensory capabilities, and physical attributes.")
        self.enviroment = enviroment

    def feed(self, different_food):
        self.different_food = different_food
        return different_food

    def show_description(self):
        super().__init__()


class Human(Mammal):

    def __init__(self, enviroment = 0):
        self.enviroment = enviroment
        print("Humans (Homo sapiens) are the only extant members of the subtribe Hominina. A terrestrial animal, "
        "humans are characterized by their erect posture and bipedal locomotion; high manual dexterity and heavy "
        "tool use compared to other animals; open-ended and complex language use compared to other animal "
        "communications; larger, more complex brains than other animals; and highly advanced and organized "
        "societies")

    def feed(self):
        return "spaghetti"

    def show_description(self):
        super().__init__()

def how_it_feeds(species):
    print(species.feed())


# obj_animal = Animal()
# obj_mammal = Mammal()
obj_cat = Cat()
obj_dog = Dog()

obj_human = Human("earth")
print(obj_human.enviroment)

obj_human.show_description()
print(obj_human.eucaryont)


how_it_feeds(obj_cat)
how_it_feeds(obj_dog)


