from datetime import date


class Dog:
    tag = 0

    def __init__(self, name: str, birthday: date):
        self.name = name
        self.__birthday = birthday
        Dog.tag += 1
        self.dog_id = Dog.tag

    def __str__(self):
        return f"I am a dog! My name is {self.name}. My ID is {self.dog_id}. I am {round(self.age)} year(s) old."

    # derived property
    @property
    def age(self):
        current_date = date.today() # get current date
        time_passed = current_date - self.__birthday
        return time_passed.days//365.25


spot = Dog("Spot", date(year=2018, month=2, day=20))
buster = Dog("Buster", date(year=2020, month=8, day=5))

print(spot.dog_id)
print(buster.dog_id)

print(spot)
print(buster)
