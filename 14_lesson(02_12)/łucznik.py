class �ucznik(Wojownik):

    def __init__(self):
        super().__init__()
        self.life = 40
        self.arrows = 10

    def atakuj(self):
        if self.arrows > 0:
            print('�ucznik: wypu�ci�em strza�y!')
            self.exp += 0.4
            self.arrows -= 1
        else:
            print('Nie masz strza�, nie masz ju� czym strzela�')