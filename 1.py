class Person:
    def __init__(self, name='человек', job='работник', salary=0):
        self.name = name
        self.job = job
        self.salary = salary

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} - должность {self.job}. Оклад {self.salary}$'


class Manager(Person):
    pass


a = Person('Александр', 'программист', 400)
b = Manager('Наталья', 'менеджер', 300)
print(a, b, sep='\n')