import random

class Player:
    """ Gracz w grze strzelance. """

    def blast(self, enemy):
        print('Gracz razi wroga.\n')
        enemy.die()

    def shoot(self, enemy):
        aim = list(range(1, 11))
        target = random.choice(aim)
        if target < 4:
            print(f'Celność strzału Bohatera wynosiła {target}, niestety ale to za mało, aby pokonać Obcego.')
            enemy.win()
        else:
            print(f'Celność strzału Bohatera wynosiła {target}.')
            enemy.die()


class Alien:
    """ Obcy w grze strzelance. """

    def die(self):
        print('Obcy z trudem lapie oddech, "To juz koniec. Ale prawdziwie wielki koniec... \n',
              'Walczylismy do konca. Nie, to nie koniec. Larwy moje jednoczcie sie! \n',
              'O tak one pomszcza mnie pewnego dnia... \n',
              'zegnaj, okrutny Wszechswiecie! Umieeeraaam"')

    def win(self):
        print('Obcy: *mlask mlask* niezbyt smaczni ci Ziemianie, ale ostatni z gatunku Ziemian to nie lada rarytas. '
              'Najedzony mogę iść spać.')


if __name__ == '__main__':
    print('************ smierc obcego  ************\n')
    hero = Player()
    invader = Alien()
    hero.shoot(invader)
    input('\n\nAby zakonnczyc program, nacisnij klawisz Enter.')
