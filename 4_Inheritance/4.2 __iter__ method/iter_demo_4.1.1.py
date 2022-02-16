class Students:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []

    def get_members_count(self):
        return len(self.members)

    def add_member(self, new_member):
        self.members.append(new_member)

    def __iter__(self):
        # yield one member at a time
        for member in self.members:
            yield member


asd_students = Students('ASD Rocks!')
print(asd_students.get_members_count())

asd_students.add_member('Dawson')
asd_students.add_member('Andre')

for asd_stu in asd_students:
    print(asd_stu)