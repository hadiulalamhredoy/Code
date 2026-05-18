# 📘 DBMS Fundamentals

This repository contains basic concepts, SQL queries, and mini examples related to **Database Management System (DBMS)** fundamentals.  
It is useful for beginners, students, interview preparation, and academic practice.

---

# 📚 Topics Covered

- Introduction to DBMS
- Types of Databases
- ER Model
- Relational Model
- Keys in DBMS
- Normalization
- SQL Basics
- Joins
- Constraints
- Transactions
- Indexing
- Views
- Stored Procedures
- Triggers

---

# 🗂 Folder Structure

DBMS-Fundamentals/
│
├── SQL-Basics/
├── Joins/
├── Normalization/
├── Transactions/
├── Constraints/
├── Mini-Projects/
└── README.md

---

# 🛠 SQL Fundamentals Examples

## 1. Create Database

```sql
CREATE DATABASE StudentDB;
2. Create Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    age INT
);


3. Insert Data
INSERT INTO Students (student_id, name, department, age)
VALUES
(1, 'Rahim', 'CSE', 22),
(2, 'Karim', 'EEE', 23),
(3, 'Sakib', 'BBA', 21);


4. Select Data
SELECT * FROM Students;
5. Update Data
UPDATE Students
SET age = 24
WHERE student_id = 2;



6. Delete Data
DELETE FROM Students
WHERE student_id = 3;



🔑 Types of Keys in DBMS
Key Type---------------	Description
Primary Key------------	Uniquely identifies each record
Foreign Key-----------	Connects two tables
Candidate Key----------	Possible primary keys
Super Key	---------------Set of unique attributes


🔄 Normalization Levels
1NF
Remove repeating groups
2NF
Remove partial dependency
3NF
Remove transitive dependency


🔗 SQL Joins
INNER JOIN
SELECT Students.name, Courses.course_name
FROM Students
INNER JOIN Courses
ON Students.student_id = Courses.student_id;


🤝 Contribution

Contributions are welcome.
Feel free to fork this repository and improve it.














⚡ DBMS Advantages
Reduces data redundancy
Improves data consistency
Better security
Multi-user access
Backup and recovery support
