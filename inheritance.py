class animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

        def speak(self):
            raise NotImplementedError("childclasses must implement this method")


class dog(animal):
    def speak(self):
        return "woofs!"


class cat(animal):
    def speak(self):
        return "Meows!"


class Goat(animal):
    def speak(self):
        return "Meee!"


Goat = Goat("Matata", "Black")

dog = dog("Tom", "Brown")

cat = cat("Kebo", "White")
print(cat.name)
print(cat.color)
print(cat.speak())

print(dog.name)
print(dog.color)
print(dog.speak())

print(Goat.name)
print(Goat.color)
print(Goat.speak())
