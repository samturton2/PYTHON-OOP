# getter and setters
# why - use cases
# To hide the data - seperation of concern

# syntax 2 functions 1 to get information and to set information


# create a class called student

# class Student:
#     def __init__(self, name, company):
#         self.name = name
#         self.company = company
#
#     def getStudent(self):
#         self.__name # __ are used to hide the data
#
#     def setStudent(self, value):
#         self.__name = value
#
# student_object = Student("Sam", "SpartaGlobal")
# print(f"student name is {student_object.setStudent('ben')}")

class Student:
    def __init__(self, name, company):
        self.__name = name
        self.__company = company

    # A decorator in python is any callable python object that is used to modify a function or class
    @property  # property makes functions act like variables
    def Student(self):
        print("This print function will print when you trigger the variable")
        return self.__name # __ are used to hide the data

    @Student.setter
    def Student(self, value):
        print("calling @student.student method")
        self.__name = value

student_object = Student("Sam", "SpartaGlobal")

student_object.Student = "ben"
print(student_object.Student)