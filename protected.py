class person:
    def __init__(self,name,age,gender):
        self._name=name
        self._age=age
        self.gender=gender
def get_name(person):
    return person._name
def get_age(person):
    return person._age
person1=person("John",30,"Male")
print(get_name(person1))
print(get_age(person1))