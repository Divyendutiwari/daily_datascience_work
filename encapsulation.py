class person:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.gender=gender
def get_name(person):
    return person.__name
def get_age(person):
    return person.__age
person1=person("John",30,"Male")
get_name(person1)
###the above line will raise an AttributeError because __name is private and cannot be accessed directly outside the class.