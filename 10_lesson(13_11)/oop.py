import random


class Dog:
    tail = True

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        # self.pseudo = name + "-" + color *** nie może zostać, jeśli chcę wywołać metodę

    def pseudo(self):
        adj = ["Destroyer", "Butcher", "Scavenger", "Nice Guy"]
        return self.name + "the" + random.choice(adj)


obj_pimpek = Dog("Pimpek", "Collie", 5, "white")
obj_dyzio = Dog("Dyzio", "Cotton de tulear", 7, "blond")

# print(obj_pimpek.name)
# print(Dog.pseudo(obj_pimpek))
print(obj_pimpek.pseudo())

# names = "Anna, Marta, Marek, Paweł"
# print(names.split(","))
# print(str.split(names, ","))
