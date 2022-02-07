class Dog:
    tag = 0

    def __init__(self, name):
        self.name = name
        Dog.tag += 1
        self.dog_id = Dog.tag

spot = Dog("Spot")
buster = Dog("Buster")

print(spot.dog_id)
print(buster.dog_id)

print(spot)