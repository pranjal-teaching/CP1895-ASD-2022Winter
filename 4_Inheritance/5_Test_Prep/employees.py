import datetime


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        assert isinstance(employee, Employee)  # !!!
        self.employees.append(employee)


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
        self.__work_log = []

    @property
    def id(self):
        return self.__id

    def add_work_log(self, start_time, end_time):
        assert isinstance(start_time, datetime.datetime), "start_time must be a datetime.datetime object"
        assert isinstance(end_time, datetime.datetime), "end_time must be a datetime.datetime object"
        assert end_time > start_time, 'end_time must be after start_time'
        self.__work_log.append({'start_time': start_time, 'end_time': end_time})

    def get_hours_worked_since(self, timestamp):
        # go through the work_log list
        # check if start_time is greater than timestamp, if so, calculate hours worked and add to total
        # return total
        pass

    def __str__(self):
        return f'Hourly Empl: {self.name} ({self.id})'


class SalariedEmployee(Employee):
    def __init__(self, name, sin, annual_salary):
        Employee.__init__(self, name, sin)
        self.__salary = annual_salary
        self.__id = f'SE_{str(Employee.employee_counter).zfill(2)}'  # SE_01, SE_02, ...

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'Salaried Empl: {self.name} ({self.id})'


if __name__ == '__main__':
    employee_dawson = HourlyEmployee('Dawson', 111222111, 80)
    print(employee_dawson.id)

    employee_robin = SalariedEmployee('Robin', 111222112, 800000)
    print(employee_robin.id)

    print(employee_dawson.SIN)
    employee_dawson.SIN = 111222113
