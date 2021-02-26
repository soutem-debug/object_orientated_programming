class Dog:

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

    def description(self):
        print(self.name + " is" + " " + str(self.age) + "years old.")

    def breeding(self):
        print(self.name + " is a " + self.gender + " " + self.breed)

    def birthday(self):
        self.age += 1


navi = Dog("Navi", 5, "Female", "Shitzu")
atlantis = Dog("Atlantis", 3, "Male", "Poodle")
navi.description()
navi.breeding()
atlantis.description()
atlantis.breeding()



