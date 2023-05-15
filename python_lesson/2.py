
class Student:
    def __init__(self, name,university, curs=1):
        self.name = name
        self.university = university
        self.curs = curs
    def get_name(self):
        return self.name
    def get_university(self):
        return self.university
    def get_year(self):
        return self.curs
    def study(self):
        if self.curs < 6:
            self.curs =+ 1
class Employee:
    def __init__(self, name, company):
        self.all_mesto=('junior','middle','senior', 'lead')
        self.name = name
        self.company = company
        self.mesto = self.all_mesto[0]
    def get_name(self):
        return self.name
    def get_company(self):
        return self.company
    def get_position(self):
        return self.mesto, self.mesto.index

    def work(self):
        if self.mesto != 'lead':
            self.mesto = self.all_mesto[self.all_mesto.index(self.mesto) +1]
class Human:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
st_1 = Student("Petr", "MSU")
st_2 = Student("Sonya", "Cambridge")
h = Human("Shrek")
empl_1 = Employee("Ivan", "Yandex")
empl_2 = Employee("Ann", "Gazprom")
people = [st_1, empl_2, st_2, h, empl_1]
for person in people:
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
