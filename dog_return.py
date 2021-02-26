class Dog:

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

    def description(self):
        return print(f"{self.name} is {self.age} years old")

    def breeding(self):
        return print(f"{self.name}  is a {self.gender} and a {self.breed} ")

    def birthday(self):
        self.age += 1


navi = Dog("Navi", 5, "Female", "Shitzu")
atlantis = Dog("Atlantis", 3, "Male", "Poodle")
navi.description()
navi.breeding()
atlantis.description()
atlantis.breeding()



