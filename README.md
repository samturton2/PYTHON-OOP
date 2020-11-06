# OOP Example Lesson
#### Object Oriented Programming

- **Step 1**
  - create an animal class as Parent
- **Step 2**
  - create reptile class as the child class
  - why? so we can inherit from our parent class
  - abstract
- **Step 3**
  - create snake class as child of reptile
- **Step 4**
  - Create a Python class

`__name__` and `__main__` are used to check if the code is run from current file/ directory for different file/ importing it
- We will create 2 files and use `__name__` and `__main__` in both files and the outcome will show the difference.

## getter and setter code along
```python
class Student:
    def __init__(self, name, company):
        self.__name = name
        self.__company = company
```
- getters method with hidden information
```python
    def getStudent(self):
        return self.__name # __ are used to hide the data

```
- defining a setter function
```python
     def setStudent(self, value):
         self.__name = value
```

student_object = Student("Sam", "SpartaGlobal")
print("student name is " + student_object.setStudent())

**second iteration**

```python 
class Student:
    def __init__(self, name, company):
        self.__name = name
        self.__company = company
```
- Using @property decorator with student function
- property make a function act like a variable
```python
    @property
    def Student(self):
        print("This prints when you trigger the variable/function")
        return self.__name
```
- a decorator in Python is any callable python object that is used to modify a function or class
```python
    @Student.setter
    def Student(self, value):
        print("calling @student.student method")
        self.__name = value
```
- creating an object with required information
```python
student_object = Student("Sam", "SpartaGlobal")
```
- now using the property and setter, we can change the name dispite the __
```python
student_object.Student = "ben"
print(student_object.Student) # calling the student function like a variable
```