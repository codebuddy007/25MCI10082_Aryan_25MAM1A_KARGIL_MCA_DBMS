create table Department (
    dept_id serial primary key,
    dept_name varchar(50)
);

create table EmployeeV (
    emp_id serial primary key,
    emp_name varchar(50),
    salary numeric(10,2),
    status varchar(20),
    dept_id int references Department(dept_id)
);


insert into Department (dept_name) values
('HR'),
('IT'),
('Finance'),
('Sales');


insert into EmployeeV (emp_name, salary, status, dept_id) values
('Amit', 30000, 'Active', 1),
('Ankit', 45000, 'Active', 2),
('Khushi', 58000, 'Inactive', 2),
('Manisha', 40000, 'Inactive', 3),
('Arman', 70000, 'Active', 4);



select * from EmployeeV;
select * from Department;



create view active_emp as
select emp_id, emp_name, salary, dept_id
from EmployeeV
where status = 'Active';

select * from active_emp;



create view emp_dept_view as
select 
    e.emp_id,
    e.emp_name,
    e.salary,
    d.dept_name
from EmployeeV e
join Department d
on e.dept_id = d.dept_id;

select * from emp_dept_view;


create view dept_summary as
select 
    d.dept_name,
    count(e.emp_id) as total_employees,
    avg(e.salary) as average_salary,
    sum(e.salary) as total_salary
from Department d
left join EmployeeV e
on d.dept_id = e.dept_id
group by d.dept_name;

select * from dept_summary;



create or replace view active_employees as
select emp_id, emp_name, salary
from EmployeeV
where status = 'Active';

select * from active_employees;