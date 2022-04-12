# Encapsulation, Getters , Setters , Class Variables and Instance Variables
# creating a Class ( Usually starts with Uppercase letter)
class Person:
    # class variables
    _minAge = 1
    _species = "Homo sapiens"

    # Constructor Function data are now private
    def __init__(self, _name, _age, _job):
        print("An instance of Class Person is created.")
        # setting data on object initialization
        self.__name = _name
        self.__age = _age
        self.__job = _job

    # setter methods
    def setJob(self, newJob):
        self.__job = newJob

    def setAge(self, newAge):
        self.__age = newAge

    def setName(self, newName):
        self.__name = newName

    # getter methods
    def getName(self):
        return self.__name

    # getting all data
    def getDetails(self):
        print("Person's name = {}".format(self.__name))
        print("Person's age = {}".format(self.__age))
        print("Person's job = {}".format(self.__job))


moopz = Person("Moopz", 30, "Programmer")
moopz.setAge(99)
moopz.setName("Pongsathorn")
moopz.setJob("Programmer")
print("The name of this person is {}".format(moopz.getName()))
print(Person._minAge)
print(Person._species)
