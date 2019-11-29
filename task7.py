# Implement Students room using OOP:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Students_room:
    """ Данные о студенте """
    def __init__(self, name, surname, age, major):
        self.name = name
        self.surname = surname
        self.age = age
        self.major = major

    """ Вывод информации о студенте """
    def printer(self):
        print(f"name: {self.name.title()} {self.surname.title()}, "
              f"age: {self.age}, major: {self.major.title()}")

Steve = Students_room("Steven", "Schultz", 23, "English")
Johnny = Students_room("Jonathan", "Rosenberg", 24, "Biology")

Steve.printer()
Johnny.printer()