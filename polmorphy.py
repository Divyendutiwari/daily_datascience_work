class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self):
        return "Some sound"
class dog(animal):
    def speak(self):
        return "Woof!"
class cat(animal):
    def speak(self):
        return "Meow!"
def animal_speak(animal):
    return animal.speak()
dog_instance = animal("Buddy", "Canine") 
cat_instance = animal("Whiskers", "Feline")
print(animal_speak(dog_instance))
dog1=dog("Buddy", "Canine")
print(dog1.speak())