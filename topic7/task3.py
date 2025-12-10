class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


class StudentData:
    def __init__(self, students):
        self.students = students

    def sort_students(self, column):
        if column == "name":
            sorted_students = sorted(self.students, key=lambda student: student.name)
            print("\nSorted by name:\n")

        elif column == "age":
            sorted_students = sorted(self.students, key=lambda student: student.age)
            print("\nSorted by age:\n")

        else:
            print("\nYou entered an incorrect column name. Try again.\n")
            return

        for student in sorted_students:
            print(student)



students = [
    Student('Anna', 19),
    Student('Peter', 20),
    Student('Marina', 18),
    Student('Alex', 21),
    Student('Mykola', 22),
    Student('Nick', 23),
    Student('Fred', 20),
    Student('Alisa', 18),
    Student('William', 25),
    Student('John', 24)
]

while True:
    column = input("Select the column to sort by (name, age): ")
    if column in ("name", "age"):
        break
    else:
        print("\nYou entered something wrong. Please, try again!\n")

student_data = StudentData(students)
student_data.sort_students(column)
