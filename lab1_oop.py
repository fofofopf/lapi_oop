class Console:
    def __init__(self, cost: int, power: int):
        '''
        :param cost: Стоимость консоли
        :param power: Мощность консоли
        '''
        self.cost = cost
        self.power = power
        if not isinstance(cost, int):
            raise TypeError('Стоимость должна быть типа int')
        if not isinstance(power, int):
            raise TypeError('Мощность должна быть типа int')
        if cost <= 0:
            raise ValueError('Стоимость может быть только положительным числом')
        if power <=0:
            raise ValueError('Мощность может быть только положительным числом')
    def is_it_PlayStation(self):
        "Функция которая проверяет является ли консоль плейстейшн"
        ...
    def is_it_5th_generation(self):
        'Функция, которая проверяет является ли консоль 5-го поколения'
        ...

class Desk:
    def __init__(self, material: str, height: float):
        '''
        :param material: Материал стола
        :param height: Высота стола
        '''
        self.material = material
        self.height = height
        if height <=0:
            raise ValueError('Высота может быть только положительным числом')
    def raise_table(self, height_change: float) -> int:
        '''
        Функция, которая поднимает стол на определенную высоту
        :param height_change: высота на которую мы поднимаем стол
        '''
        if height_change <=0:
            raise ValueError('Нельзя поднять стол на отрицательное число')
        if not isinstance(height_change, float):
            raise TypeError('Поднять можно только на число')
        ...
    def reduce_height(self, height_change: float):

        '''
        Функция, которая опускает высоту стола
        :param height_change: высота, на которую мы опускаем стол
        '''
        if height_change <=0:
            raise ValueError('Нельзя поднять стол на отрицательное число')
        if not isinstance(height_change, float):
            raise TypeError('Поднять можно только на число')
        ...

class Employer:
    def __init__(self, department: str, salary: int):
        '''
        :param department: отдел сотрудника
        :param salary: зарплата сотрудника
        '''
        self.department = department
        self.salary = salary
        if not isinstance(salary, int):
            raise TypeError('Зарплата должна быть типа int')
        if salary <= 0:
            raise ValueError('Зарплата может быть только положительным числом')
    def what_category(self, surname: str):
        '''
        Функция, которая определяет какой категории сотрудник
        '''
        if not isinstance(surname, str):
            raise TypeError('Фамилия должна быть только типа str')
        ...
    def what_projects(self, surname: str):
        '''
        Функция, которая определяет какие проекты закреплены за сотрудником
        '''
        if not isinstance(surname, str):
            raise TypeError('Фамилия должна быть только типа str')
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()     # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
