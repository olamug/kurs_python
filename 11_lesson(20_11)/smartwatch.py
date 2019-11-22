class UsefulStuff:
    def __init__(self):
        print("I'm useful.")


class Watch(UsefulStuff):
    def __init__(self):
        print("I can check what time is it.")
        super().__init__()


class Phone(UsefulStuff):
    def __init__(self):
        print("I can call.")
        super().__init__()


class Smartwatch(Watch, Phone):
    def __init__(self):
        print("I'm a smartwatch.")
        super().__init__()

# u = UsefulStuff()
# w = Watch()
# p = Phone()
sw = Smartwatch()