class Employee:
    firm = "Love Python"

    def __init__(self, workplace, salary, name, surname, experience, is_student):
        self.workplace = workplace
        self.salary = salary
        self.name = name
        self.surname = surname
        self.experience = experience
        self.is_student = is_student

    def salary_bump(self):
        if self.experience < 1:
            return "podwyżki nie obowiązują w pierwszym roku pracy. Jedynie premie."
        else:
            increrase = self.experience / 50
            self.salary = self.salary + (self.salary * increrase)
            return "Wynagrodzenie po podwyżce powinno wynosić:", self.salary

    def taxes(self):
        healthcare = 150
        if self.salary > 10000:
            tax = (self.salary - (self.salary * 0.2)) - healthcare
            return "Po odjęciu podatku i składki:", tax
        else:
            tax = self.salary - (self.salary * 0.05) - healthcare
            return "Po odjęciu podatku i składki:", tax

    def email(self):
        primary = self.name + "." + self.surname
        primary = primary.lower()
        secondary = self.firm.replace(" ", "").lower() + ".com"
        email1 = primary + "@" + secondary
        return email1



p1 = Employee("programista", 5500, "Jan", "Kowalski", 3, False)
print(p1.taxes())
print(p1.email())
print(p1.salary_bump())