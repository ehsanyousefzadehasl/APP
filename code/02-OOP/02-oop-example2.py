class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1

    def get_name(self):
        print('This object\'s name is %s'%self.name)

    def get_age(self):
        print('This object\'s age is %d'%self.age)

    def get_info(self):
        print('name: %s, age: %d'%(self.name, self.age))

    def return_count_of_persons(self):
        return Person.count

    def __del__(self):
        Person.count = Person.count - 1

ehsan = Person('ehsan', 26)
ehsan.get_name()
ehsan.get_age()
ehsan.get_info()

john = Person("Johnny", 12)
Ahmet = Person("Ahmet Kaya", 65)

print("Number of persons: %d" % ehsan.return_count_of_persons())

del Ahmet

print("Number of persons: %d" % ehsan.return_count_of_persons())