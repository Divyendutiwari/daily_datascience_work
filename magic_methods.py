##these methods allow you to define how your objects behave with built-in operations
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"person(name={self.name}, age={self.age})"
person1 = person("Alice", 30)
print(person1)
print(type(person1))