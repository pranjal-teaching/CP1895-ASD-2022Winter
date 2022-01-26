class A:
    def __init__(self, a1, a2):
        print("init method is invoked")
        self.a1 = a1
        self.a2 = a2

    def afoo(self):
        print(self.a1, self.a2)

# creating a new object and passing values for the attributes
a_object = A(10, 20)


# calling the afoo() method from a_obj
a_object.afoo()

"""
class A
attributes: a1, a2
method: afoo
"""
