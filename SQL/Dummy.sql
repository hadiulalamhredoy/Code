

select max(salary)
from  employees
group by employee_id;

select min(salary)
from  employees
group by employee_id;

select *
from employees
where department_id = 10 

select department_id, Max(Salary)  
from employees  
where department_id != 20 
group by department_id 
having max(salary) > 5000
