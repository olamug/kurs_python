import

class Rycerz(Wojownik):

    def __init__(self):
        super().__init__()
        self.life = 60

    def atakuj(self):
        print('Rycerz: Machn¹³em mieczem!')
        self.exp += 0.3