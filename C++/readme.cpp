# 💻 C++ Fundamentals

This repository contains basic concepts and examples of **C++ Programming Fundamentals**.  
It is useful for beginners, students, competitive programmers, and interview preparation.

---

# 📚 Topics Covered

- Introduction to C++
- Variables and Data Types
- Input and Output
- Operators
- Conditional Statements
- Loops
- Functions
- Arrays
- Strings
- Pointers
- Structures
- Object-Oriented Programming
- File Handling
- STL Basics

---

# 🗂 Folder Structure

CPlusPlus-Fundamentals/
│
├── Variables-and-DataTypes/
├── Operators/
├── Loops/
├── Functions/
├── Arrays/
├── Pointers/
├── OOP/
├── File-Handling/
└── README.md

---

# 🚀 Basic C++ Program

## 1. Hello World

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

---

# 🔹 Variables and Data Types

```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 22;
    float cgpa = 3.85;
    char grade = 'A';

    cout << "Age: " << age << endl;
    cout << "CGPA: " << cgpa << endl;
    cout << "Grade: " << grade << endl;

    return 0;
}
```

---

# 🔹 Conditional Statement

```cpp
#include <iostream>
using namespace std;

int main() {
    int number;

    cout << "Enter a number: ";
    cin >> number;

    if (number % 2 == 0) {
        cout << "Even Number";
    } else {
        cout << "Odd Number";
    }

    return 0;
}
```

---

# 🔹 Loops Example

```cpp
#include <iostream>
using namespace std;

int main() {

    for (int i = 1; i <= 5; i++) {
        cout << i << endl;
    }

    return 0;
}
```

---

# 🔹 Function Example

```cpp
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {

    int result = add(5, 3);

    cout << "Sum: " << result << endl;

    return 0;
}
```

---

# 🔹 Array Example

```cpp
#include <iostream>
using namespace std;

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 5; i++) {
        cout << numbers[i] << " ";
    }

    return 0;
}
```

---

# 🔹 Pointer Example

```cpp
#include <iostream>
using namespace std;

int main() {

    int number = 100;
    int *ptr = &number;

    cout << "Value: " << number << endl;
    cout << "Address: " << ptr << endl;

    return 0;
}
```

---

# 🔹 OOP Example

```cpp
#include <iostream>
using namespace std;

class Student {
public:
    string name;
    int age;

    void display() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

int main() {

    Student s1;

    s1.name = "Rahim";
    s1.age = 22;

    s1.display();

    return 0;
}
```

---

# 🔹 File Handling Example

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {

    ofstream file("data.txt");

    file << "C++ File Handling Example";

    file.close();

    cout << "File Created Successfully";

    return 0;
}
```

---

# 🎯 Advantages of C++

- Fast and Efficient
- Supports OOP
- Portable Language
- Rich Standard Library
- Used in Game Development
- Useful for Competitive Programming

---

# 💡 Mini Project Ideas

- Calculator
- Student Management System
- Library Management System
- Banking System
- Inventory System

---

# 📖 Learning Goals

- Understand C++ syntax
- Build problem-solving skills
- Learn Object-Oriented Programming
- Prepare for coding interviews
- Improve competitive programming skills

---

# 🤝 Contribution

Contributions are welcome.  
Feel free to fork this repository and improve it.

---

# ⭐ Support

If you found this repository useful, give it a ⭐ on GitHub.
