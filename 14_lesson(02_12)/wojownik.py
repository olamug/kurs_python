class Wojownik:

    def __init__(self):
        self.exp = 0

    def __repr__(self):
        name = self.__class__.__name__
        return f"{name}: hp={self.life}, exp={self.exp}."

    def maszeruj(self, dystans):
        name = self.__class__.__name__
        print(f'{name}: przeszed³em {dystans} m.')
        self.exp += 0.2*dystans