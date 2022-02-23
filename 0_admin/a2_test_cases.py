import math
from unittest import TestCase

import pytest

from circle import Circle
from date import Date
from employee import Employee
from line import Line
from point import Point
from rectangle import Rectangle
from student import Student
from bank import BankAccount, Transaction

class TestCircle(TestCase):

    def test_non_positive_radius_raises_AssertionError_1(self):
        with pytest.raises(AssertionError):
            c = Circle(-1.0)

    def test_non_positive_radius_raises_AssertionError_2(self):
        with pytest.raises(AssertionError):
            c = Circle(0.0)

    def test_nonnumerical_radius_raises_AssertionError(self):
        with pytest.raises(AssertionError):
            c = Circle('1.0')

    def test_property_radius_for_type_enforcing(self):
        self.c1 = Circle(10.0, 'Yellow')
        with pytest.raises(TypeError):
            self.c1.radius = 10

    def test_property_radius_for_value_enforcement(self):
        self.c1 = Circle(10.0, 'Yellow')
        with pytest.raises(ValueError):
            self.c1.radius = 0.0

    def test_get_area(self):
        assert Circle(10.0).get_area() == pytest.approx(math.pi * 100)

    def test_get_circumference(self):
        assert Circle(10.0).get_circumference() == pytest.approx(math.pi * 20)

    def test_str(self):
        self.c1 = Circle(10.0, 'Yellow')
        assert str(self.c1.radius) in str(self.c1)


class TestPoint(TestCase):
    def test_point_creation_x(self):
        p = Point(2, 4)
        self.assertTrue(p.x == 2, 'Point\'s x coordinate does not match what is set')

    def test_point_creation_y(self):
        p = Point(2, 4)
        self.assertTrue(p.y == 4, 'Point\'s y coordinate does not match what is set')

    def test_point_str(self):
        p = Point(2, 4)
        self.assertTrue(str(p) == '(2, 4)')

    def test_point_x_is_readonly(self):
        p = Point(2, 4)
        with pytest.raises(AttributeError):
            p.x = 3

    def test_point_y_is_readonly(self):
        p = Point(2, 4)
        with pytest.raises(AttributeError):
            p.y = 3


class TestLine(TestCase):
    def test_line_init(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        line = Line(p1, p2)
        self.assertEqual(line.start_point, p1)
        self.assertEqual(line.end_point, p2)

    def test_line_length(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        line = Line(p1, p2)
        self.assertEqual(line.length, math.sqrt(2))

    def test_line_start_point_is_read_only(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        line = Line(p1, p2)
        with self.assertRaises(AttributeError):
            line.start_point = Point(3, 3)

    def test_line_end_point_can_be_modified(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        line = Line(p1, p2)
        new_end_point = Point(3, 3)
        line.end_point = new_end_point
        self.assertEqual(line.end_point, new_end_point)


class TestRectangle(TestCase):
    def test_rectangle_init(self):
        point = Point(1, 1)
        non_point = 'a'
        with pytest.raises(AssertionError):
            rect = Rectangle(point, non_point)
        with pytest.raises(AssertionError):
            rect = Rectangle(non_point, point)

    def test_rectangle_bottom_left_property(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        rect = Rectangle(p1, p2)
        self.assertEqual(rect.bottom_left_corner, p1)

    def test_rectangle_top_right_property(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        rect = Rectangle(p1, p2)
        self.assertEqual(rect.top_right_corner, p2)

    def test_assertion_error_for_incorrect_type_init_p1(self):
        p2 = Point(1, 1)
        p1 = (2, 2)
        with self.assertRaises(AssertionError):
            Rectangle(p1, p2)

    def test_assertion_error_for_incorrect_type_init_p2(self):
        p1 = Point(1, 1)
        p2 = [2, 2]
        with self.assertRaises(AssertionError):
            Rectangle(p1, p2)

    def test_rectangle_top_left_corner_property(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        rect = Rectangle(p1, p2)
        self.assertEqual(str(rect.top_left_corner), str(Point(1, 2)))

    def test_rectangle_bottom_right_corner_property(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        rect = Rectangle(p1, p2)
        self.assertEqual(str(rect.bottom_right_corner), str(Point(2, 1)))

    def test_rectangle_area(self):
        p1 = Point(1, 4)
        p2 = Point(8, 20)
        rect = Rectangle(p1, p2)
        self.assertEqual(112, rect.area)

    def test_rectangle_perimeter(self):
        p1 = Point(1, 4)
        p2 = Point(8, 20)
        rect = Rectangle(p1, p2)
        self.assertEqual(46, rect.perimeter)


class TestDate(TestCase):
    def test_init_types(self):
        with pytest.raises(TypeError):
            Date(year=1.0, month=1, day=1)
        with pytest.raises(TypeError):
            Date(1, "1", 1)
        with pytest.raises(TypeError):
            Date(1, 1, True)
        with pytest.raises(ValueError):
            Date(year=2022, month=1, day=32)
        with pytest.raises(ValueError):
            Date(year=2022, month=13, day=1)
        with pytest.raises(ValueError):
            Date(year=2022, month=1, day=0)
        with pytest.raises(ValueError):
            Date(year=2022, month=-1, day=1)

    def test_day_property(self):
        d = Date(year=1, month=1, day=1)
        self.assertEqual(d.day, 1)
        d.day = 20
        self.assertEqual(d.day, 20)

    def test_month_property(self):
        d = Date(year=1, month=1, day=1)
        self.assertEqual(d.month, 1)
        d.month = 10
        self.assertEqual(d.month, 10)

    def test_year_property(self):
        d = Date(year=2000, month=1, day=1)
        self.assertEqual(d.year, 2000)
        d.year = 2010
        self.assertEqual(d.year, 2010)

    def test_is_leap_year(self):
        d = Date(year=2020, month=1, day=1)
        self.assertTrue(d.is_leap_year)
        d = Date(year=2022, month=1, day=1)
        self.assertFalse(d.is_leap_year)

    def test_valid_date(self):
        d = Date(year=2020, month=1, day=1)
        self.assertTrue(d.is_valid_date)
        d = Date(year=2020, month=1, day=31)
        self.assertTrue(d.is_valid_date)
        d = Date(year=2020, month=2, day=29)
        self.assertTrue(d.is_valid_date)
        d = Date(year=2021, month=2, day=29)
        self.assertFalse(d.is_valid_date)
        d = Date(year=2020, month=4, day=31)
        self.assertFalse(d.is_valid_date)


class TestStudent(TestCase):
    def test_getter_properties(self):
        s = Student(id=100, name="John", address="1 Main St", program="Software Development")
        self.assertEqual(s.name, "John")
        self.assertEqual(s.address, "1 Main St")
        self.assertEqual(s.id, 100)

    def test_setter_properties(self):
        s = Student(id=100, name="John", address="1 Main St", program="Software Development")
        s.address = "2 Main St"
        self.assertEqual(s.address, "2 Main St")

    def test_student_average_score(self):
        s1 = Student(id=100, name="John", address="1 Main St", program="Software Development")
        s1.add_course("CP1850")
        s1.add_course("CP1860")
        s1.add_course("CP1870")
        s1.course_completed("CP1850", 80)
        s1.course_completed("CP1860", 90)
        s1.course_completed("CP1870", 70)
        self.assertEqual(s1.average_score, 80)


class TestEmployee(TestCase):
    def test_employee_init(self):
        e = Employee(first_name="John", last_name="Doe", employee_id='E1001', salary=1000)
        self.assertEqual(e.name, "John Doe")

    def test_employee_annual_salary(self):
        e = Employee(first_name="John", last_name="Doe", employee_id='E1001', salary=1000)
        self.assertEqual(e.annual_salary, 12000)

    def test_employee_pay_raise(self):
        e = Employee(first_name="John", last_name="Doe", employee_id='E1001', salary=1000)
        e.raise_salary(raise_percent=10)
        self.assertEqual(e.salary, 1100)


class TestBankAccountAndTransaction(TestCase):
    def test_bank_account_init(self):
        ba_1 = BankAccount('0001', 100.00)
        ba_2 = BankAccount('0001', 200.00)
        self.assertEqual(ba_1.balance, 100.00)
        self.assertEqual(ba_2.balance, 200.00)

    def test_bank_account_deposit(self):
        ba_1 = BankAccount('0001', 100.00)
        ba_2 = BankAccount('0001', 200.00)
        transaction_1 = Transaction(ba_2, ba_1, 150.00)
        self.assertEqual(ba_1.balance, 250.00)
        self.assertEqual(ba_2.balance, 50.00)

    def test_bank_account_withdraw(self):
        ba_1 = BankAccount('0001', 100.00)
        ba_2 = BankAccount('0001', 200.00)
        transaction_1 = Transaction(ba_1, ba_2, 50.00)
        self.assertEqual(ba_1.balance, 50.00)
        self.assertEqual(ba_2.balance, 250.00)