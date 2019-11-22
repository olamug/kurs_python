class Vertebrate:
    backbone = True

    def __init__(self):
        print("Random kręgowiec")

    def desc(self):
        print("Zewnętrzną pokrywe ciała kręgowców stanowi skóra.")


class Cat(Vertebrate):
    def __init__(self, name):
        print("Kotek")
        self.name = name

    def desc(self):
        print("Koty są super")
        super().__init__()


ver = Vertebrate()
kitty = Cat("Kitty")
kitty.desc()