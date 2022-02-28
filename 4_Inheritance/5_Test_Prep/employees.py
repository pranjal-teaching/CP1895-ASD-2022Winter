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
        self.__old_sins = []
        Employee.employee_counter += 1

    @property
    def SIN(self):
        return "PRIVATE"

    @SIN.setter
    def SIN(self, new_sin):
        if not isinstance(new_sin, int):
            raise TypeError("sin must be an int")
        if len(str(new_sin)) != 9:
            raise ValueError('SIN must be a 9-digit number')
        self.__old_sins.append(self.__sin)
        self.__sin = new_sin


class HourlyEmployee(Employee):
    def __init__(self, name, sin, hourly_wage):
        Employee.__init__(self, name, sin)
        self.__wage = hourly_wage
        self.__id = f'HE_{str(Employee.employee_counter).zfill(2)}'  # HE_01, HE_02, ...

    @property
    def id(self):
        return self.__id


class SalariedEmployee(Employee):
    def __init__(self, name, sin, annual_salary):
        Employee.__init__(self, name, sin)
        self.__salary = annual_salary
        self.__id = f'SE_{str(Employee.employee_counter).zfill(2)}'  # SE_01, SE_02, ...

    @property
    def id(self):
        return self.__id


employee_dawson = HourlyEmployee('Dawson', 111222111, 80)
print(employee_dawson.id)

employee_robin = SalariedEmployee('Robin', 111222112, 800000)
print(employee_robin.id)
