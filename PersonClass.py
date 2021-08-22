class Person:
    def __init__(self, name):
        # The property self.name (Object.name) is assigned to the passed by parameters name.
        self.name = name

    def talk(self):
        print(f'Hello my name is {self.name}')


person1 = Person('Ricardo')

person1.talk()
