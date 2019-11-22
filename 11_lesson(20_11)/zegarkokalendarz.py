class Kalendarz():
    def __init__(selfself):
        pass

    def current_date(self):
        return datetime.datetime.now().date()

class ZegarkoKalendarz(Zegarek, Kalendarz):

    def current_date_time(self):
        print(super().current_date)
        print(suepr().current_time())


