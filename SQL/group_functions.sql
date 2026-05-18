select * 
from countries; 

select *  
from departments;  

select first_name,last_name
from employees;
---Logical And  Logical or------ 
select  * 
from employees
where department_id = 60 or salary >5000;
--Comparison (=,>,<,<=,=>)---
select  *   
from employees 
where salary > 10000
--Distinct---
select  distinct  job_id 
from employees

--OrderBy---- 
select *  
from  employees  
order by salary asc

select *  
from  employees  
order by salary desc


---Limit---  
select *  
from employees  
order by salary  desc
limit 5,6

--Offset--  
select *  
from employees  
order by salary  desc
limit 5
offset  6

---Like---  
select  * 
from employees  
where last_name like 'Green%'

--AS------ 
select first_name, last_name, salary+1000 AS Increment  
from employees  
