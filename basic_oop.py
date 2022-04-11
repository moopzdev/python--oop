# CLASSES AND OBJECTS
# creating a Class ( Usually starts with Uppercase letter)
class Person:
    # Constructor Function
    def __init__(self, _name, _age, _job):
        print("An instance of Class Person is created.")
        # setting data on object initialization
        self.name = _name
        self.age = _age
        self.job = _job

        # setter method
    def jobChange(self, newJob):
        self.job = newJob

    def getDetails(self):
        # getting data
        print("Person's name = {}".format(self.name))
        print("Person's age = {}".format(self.age))
        print("Person's job = {}".format(self.job))

    # assumption: auto-fires on program exit
    def __del__(self):
        print("Calling Destructor")


# creating an object passing along constructor arguments ( Usually starts with lowercase letter)
moopz = Person("Moopz", 30, "Programmer")

# invoking a getter method
moopz.getDetails()

# invoking a setter method
moopz.jobChange("Unemployed")

# double checking consistency of setter method
moopz.getDetails()

# setting a property outside of a setter function
moopz.age = 88  # this also works

moopz.getDetails()
