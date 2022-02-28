import pickle

from employees import HourlyEmployee, SalariedEmployee


def display_menu():
    print('1. Save file')
    print('2. Read file')
    print('3. Add a new hourly employee')
    print('4. Add a salaried employee')
    print('5. Display all employees')
    print('0. Exit')


def save_file(data, filename):
    with open(filename, 'wb') as file_handler:
        pickle.dump(data, file_handler)


def read_file(filename):
    with open(filename, 'rb') as file_handler:
        data = pickle.load(file_handler)
    return data


def main():
    employees = []
    while True:
        display_menu()
        choice = input('Enter Choice: ')
        if choice == '0':
            break
        elif choice == '1':
            filename = input('Enter filename: ')
            save_file(employees, filename)
        elif choice == '2':
            filename = input('Enter filename: ')
            employees = read_file(filename)
        elif choice == '3':
            name = input('Enter employee name: ')
            sin = int(input('Enter employee sin: '))
            hourly_rate = input('Enter hourly rate: ')
            hourly_employee = HourlyEmployee(name, sin, hourly_rate)
            employees.append(hourly_employee)
        elif choice == '4':
            name = input('Enter employee name: ')
            sin = int(input('Enter employee sin: '))
            salary = input('Enter annaual salary: ')
            salaried_employee = SalariedEmployee(name, sin, salary)
            employees.append(salaried_employee)
        elif choice == '5':
            for employee in employees:
                print(employee)


if __name__ == '__main__':
    main()
