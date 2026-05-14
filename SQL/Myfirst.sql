-- CREATE database programminghero;

USE Programminghero;
CREATE TABLE Student(
Roll CHAR(4) PRIMARY KEY,  
Name VARCHAR(50), 
Marks DOUBLE
);
-- Drop Table Student;

INSERT INTO Student
(Roll, Name, Marks) values(1,'Oishee',90);

SET  SQL_SAFE_UPDATES= 0;  
UPDATE Student  
Set name = 'Lubaba  binte nehal oishee' 
where roll =1;  
SET  SQL_SAFE_UPDATES = 1;  
