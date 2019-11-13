import random


class Dog:
    tail = True

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def bark(self):
        bad = "BARKbarkBaARKBaRk!!!!"
        good = "bark!"
        if self.color == "black":
            return bad
        else:
            return good


    def wave(self):
        tail = ["machu", "machu-machu!", "MACH-MACH-MACH-MACH!", "ting-ting-ting!"]
        return random.choice(tail)

obj_pimpek = Dog("Pimpek", "white", "Cotton de tulear")
obj_odie = Dog("Odie", "white-dotted", "terrier")
obj_aza = Dog("Aza", "ginger", "Jamnik")
obj_brutus = Dog("Brutus", "black", "Cane Corso")

print(obj_pimpek.bark())
print(obj_brutus.bark())