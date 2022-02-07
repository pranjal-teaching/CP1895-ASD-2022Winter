class Dog:
    tag = 0

    def __init__(self, name):
        self.name = name
        Dog.tag += 1
        self.dog_id = Dog.tag

    def __str__(self):
        return f"I am a dog! My name is {self.name}. My ID is {self.dog_id}."


spot = Dog("Spot")
buster = Dog("Buster")

print(spot.dog_id)
print(buster.dog_id)

print(spot)
print(buster)
