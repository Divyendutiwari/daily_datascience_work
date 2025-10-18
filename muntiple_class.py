class animals:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
class pet:
    def __init__(self, owner):
        self.owner = owner
class Dog(animals,pet):
    def __init__(self, name, owner):
        animals.__init__(self, name)
        pet.__init__(self, owner)
    def speak(self):
        return "Woof!"
Doggy=Dog("Buddy","Alice")
print(Doggy.speak())