CREATE  DATABASE Employee; 

Use  Employee;  

CREATE TABLE Employee (
    EmpId INT PRIMARY KEY,
    EmpName VARCHAR(100) NOT NULL,
    JoiningYear INT,
    Birthday DATE CHECK (Birthday < DATE '2000-01-01'),
    Designation VARCHAR(50),
    Salary DECIMAL(10,2)
);

SELECT * FROM Employee;
SELECT EmpID  FROM Employee;
SELECT EmpName FROM Employee;
SELECT  JoiningYear From Employee;
SELECT  Birthday From Employee; 
SELECT  Designation FROM Employee;
SELECT  Salary FROM Employee; 

SELECT *
FROM Employee
WHERE EmpName = 'Rahim';

SELECT SUM(Salary) AS Total_Salary
FROM Employee;

SELECT * FROM Employee  Where Salary > 60000;

SELECT * FROM Employee  Where Salary >= 60000;





-- INSERT INTO  (EmpId, EmpName, JoiningYear, Birthday, Designation, Salary)VALUES('101','a', '12-06-2021',  '2001-09-09', 'Manager',  '180k');

INSERT INTO Employee
VALUES (1, 'Rahim', 2022, '1998-05-15', 'Software Engineer', 45000.00);

INSERT INTO Employee VALUES
(2, 'Karim Ahmed', 2021, '1997-08-22', 'Senior Developer', 65000.00);

INSERT INTO Employee VALUES
(3, 'Nusrat Jahan', 2020, '1996-03-10', 'HR Manager', 55000.00);

INSERT INTO Employee VALUES
(4, 'Sabbir Hossain', 2019, '1995-11-05', 'System Analyst', 60000.00);

INSERT INTO Employee VALUES
(5, 'Tania Rahman', 2023, '1999-01-18', 'Junior Developer', 35000.00);

INSERT INTO Employee VALUES
(6, 'Mahmudul Hasan', 2018, '1994-07-30', 'Project Manager', 80000.00);

INSERT INTO Employee VALUES
(7, 'Farzana Akter', 2022, '1998-12-12', 'UI/UX Designer', 48000.00);