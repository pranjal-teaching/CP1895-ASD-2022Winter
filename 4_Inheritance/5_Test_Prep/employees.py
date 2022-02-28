class Employee:
    employee_counter: int = 0

    def __init__(self, name, sin):
        assert isinstance(name, str), "name must be a string"
        # if sin is not an int, raise a typeerror
        if not isinstance(sin, int):
            raise TypeError("sin must be an int")
        if len(str(sin)) != 9:
            raise ValueError('SIN must be a 9-digit number')
        self.name = name  # public var
        self.__sin = sin  # private var
        Employee.employee_counter += 1


class HourlyEmployee(Employee):
    def __init__(self, name, sin, hourly_wage):
        Employee.__init__(self, name, sin)
        self.__wage = hourly_wage
        self.__id = f'H{str(Employee.employee_counter).zfill(2)}'  # H01, H02, ...

    @property
    def id(self):
        return self.__id


class SalariedEmployee(Employee):
    pass


dawson = HourlyEmployee('Dawson', 111222111, 80)
print(dawson.id)
