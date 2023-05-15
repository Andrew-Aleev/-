class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    @property
    def fullname(self):
        return self.name + ' ' + self.surname


person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)
