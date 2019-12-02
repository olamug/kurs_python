import datetime, holidays

class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg

    def __repr__(self):
        return self.name.capitalize() + " " + self.last.capitalize()

    @property
    def email(self):
        return '{}.{}.university.com'.format(self.name, self.last)

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
        else:
            print('Odmowa przyznania stypendium')

    @classmethod
    def set_min_avg(cls, new_avg):
        """this method sets min avg for scholarship"""
        cls.min_avg = new_avg

    @staticmethod
    def academic_football_team_cheer(nr):
        return "Go go NYA " * nr

    @staticmethod
    def academic_day(day):
        pl_holidays = holidays.Poland()
        what_holiday = pl_holidays.get(day)
        if what_holiday != None:
            print(f'Wybrany (dzisiejszy) dzień jest świętem: {what_holiday}.')
        else:
            print('Wybrany (dzisiejszy) dzień nie jest świętem.')
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    @property
    def fullname(self):
        return f'{self.last}.{self.name}'

    @fullname.setter
    def fullname(self, last_name):
        self.last, self.name = last_name.split()

obj_anna = Student('anna', 'kowalska', 23, 4.7)
obj_arek = Student('arkadiusz', 'nowak', 21, 3.9)

# print(obj_anna.min_avg)
# print(Student.min_avg)
# obj_anna.set_min_avg(3.0)
# print(obj_anna.min_avg)
# print(obj_arek.min_avg)
# print(Student.academic_football_team_cheer(5))
# print(obj_anna.email)
print('****************** dzień tygodnia***********')
today = datetime.date.today()
print("Dzisiaj mamy dzień:", today)
print('Czy dzisiaj są zajęcia? ', Student.academic_day(datetime.date(2019, 12, 25)))
print('****************** setter *****************')
obj_anna.fullname = 'Zamężna Anna'
print(obj_anna)