class animal:
    def speak(self):
        return "The animal makes a sound"
class dog(animal):
    def speak(self):
        return f"The dog barks"
class cat(animal):
    def speak(self):
        return f"the cat meowas"
def animal_sound(animal):
    print(animal.speak())
dog=dog()
cat=cat()
print(animal_sound(dog))
print(animal_sound(cat))