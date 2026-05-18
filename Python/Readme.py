# 🐍 Python OOP Fundamentals

This repository contains basic concepts and examples of **Object-Oriented Programming (OOP)** in Python.  
It is designed for beginners, students, and interview preparation.

---

# 📚 Topics Covered

- Class and Object
- Constructor (`__init__`)
- Instance Variables
- Methods
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
- Method Overriding
- Operator Overloading
- Static Methods
- Class Methods

---

# 🗂 Folder Structure

Python-OOP-Fundamentals/
│
├── Classes-and-Objects/
├── Inheritance/
├── Polymorphism/
├── Encapsulation/
├── Abstraction/
├── Projects/
└── README.md

---

# 🚀 OOP Basics Example

## 1. Class and Object

```python
class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")


student1 = Student("Rahim", "CSE")
student1.show_info()
```

---

# 🔹 Constructor Example

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"{self.brand} - {self.model}")


car1 = Car("Toyota", "Corolla")
car1.display()
```

---

# 🔹 Inheritance Example

```python
class Animal:
    def sound(self):
        print("Animals make sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog1 = Dog()
dog1.sound()
dog1.bark()
```

---

# 🔹 Polymorphism Example

```python
class Bird:
    def sound(self):
        print("Birds chirp")


class Cat:
    def sound(self):
        print("Cats meow")


for animal in (Bird(), Cat()):
    animal.sound()
```

---

# 🔹 Encapsulation Example

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(1000)
account.deposit(500)
account.show_balance()
```

---

# 🔹 Abstraction Example

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(5, 10)
print("Area:", rect.area())
```

---

# 🔹 Static Method Example

```python
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(5, 3))
```

---

# 🔹 Class Method Example

```python
class University:
    university_name = "Daffodil International University"

    @classmethod
    def show_university(cls):
        print(cls.university_name)


University.show_university()
```

---

# 🎯 Advantages of OOP

- Code Reusability
- Better Code Organization
- Easy Maintenance
- Improved Security
- Modular Programming
- Real-world Modeling

---

# 💡 Mini Project Ideas

- Student Management System
- Library Management System
- Bank Account System
- Employee Management System
- Inventory Management System

---

# 📖 Learning Goals

- Understand OOP concepts clearly
- Build reusable Python code
- Improve problem-solving skills
- Prepare for coding interviews

---

# 🤝 Contribution

Contributions are welcome.  
Feel free to fork this repository and improve it.

---

# ⭐ Support

If you found this repository useful, give it a ⭐ on GitHub.
