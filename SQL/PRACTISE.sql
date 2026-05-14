-- CREATE database programminghero;

USE Programminghero;
CREATE TABLE Student(
Roll CHAR(4) PRIMARY KEY,  
Name VARCHAR(50), 
Marks DOUBLE
);
Drop Table Student;

INSERT INTO Student
(Roll, Name, Marks) VAULES(1, 'Oishee', 90);
