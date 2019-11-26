import datetime

class Kalendarz():
    def __init__(selfself):
        pass

    def current_date(self):
        return datetime.datetime.now().date()

class Zegarek():
    def __init__(self):
        pass

    def current_time(self):
        return

class ZegarkoKalendarz(Zegarek, Kalendarz):

    def current_date_time(self):
        print(super().current_date)
        print(super().current_time())


