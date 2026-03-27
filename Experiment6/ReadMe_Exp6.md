# **DBMS Lab – Worksheet 6**  
## **Implementation of Views in PostgreSQL**

---

## 👨‍🎓 **Student Details**  
**Name:** Aryan  
**UID:** 25MCI10082  
**Branch:** MCA (AI & ML)  
**Semester:** 2nd  
**Section/Group:** 1/A  
**Subject:** DBMS Lab  
**Subject Code:** 25CAP-652  
**Date of Performance:** 01/03/2026  

---

## 🎯 **Aim of the Session**  
To learn how to create, query, and manage views in SQL to simplify database queries and provide a layer of abstraction for end-users.

---

## 💻 **Software Requirements**  
- PostgreSQL (Database Server)  
- pgAdmin  
- Windows Operating System  

---

## 📌 **Objective of the Session**

- **Data Abstraction:** Hide complex joins and calculations behind a simple virtual table.  
- **Enhanced Security:** Restrict access to sensitive columns using views.  
- **Query Simplification:** Pre-join multiple tables for easier reporting.  
- **View Management:** Understand creation, replacement, and deletion of views.  

---

## 🛠️ **Practical / Experiment Steps**

### **Prerequisite Understanding**

- A View is a virtual table created from a SELECT query.  
- Views do not store data physically.  
- Base tables must be created before creating views.  
- JOIN operations must be understood for multi-table views.  
- Aggregate functions (COUNT, SUM, AVG) are required for summary views.  
- Commands required:
  - CREATE VIEW  
  - SELECT  
  - CREATE OR REPLACE VIEW  
  - DROP VIEW  

---

# ⚙️ **Procedure of the Practical**

---

## ✅ **Step 1: Database Creation**

```sql
create database Practical6;
```

---

## ✅ **Step 2: Table Creation**

```sql
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

```

---

## ✅ **Step 3: Insert Records**

```sql
insert into Department (dept_name) values
('HR'),
('IT'),
('Finance'),
('Sales');




```

```sql
insert into EmployeeV (emp_name, salary, status, dept_id) values
('Amit', 30000, 'Active', 1),
('Ankit', 45000, 'Active', 2),
('Khushi', 58000, 'Inactive', 2),
('Manisha', 40000, 'Inactive', 3),
('Arman', 70000, 'Active', 4); 
```

---

## ✅ **Step 4: Display Base Tables**

```sql
select * from EmployeeV;
select * from Department;
```
<img width="1133" height="313" alt="image" src="https://github.com/user-attachments/assets/3535bfc0-4928-488a-812c-4e5cae18c243" />

<img width="661" height="323" alt="image" src="https://github.com/user-attachments/assets/d3308af7-fca3-47d9-bd67-98aed45fd645" />

---

## ✅ **Step 5: Creating a Simple View (Filtering)**

```sql
create view active_emp as
select emp_id, emp_name, salary, dept_id
from EmployeeV
where status = 'Active';

```

```sql
select * from active_emp;
```
<img width="1024" height="270" alt="image" src="https://github.com/user-attachments/assets/28256c2f-05ce-481a-99f3-c6f91f962a71" />


---

## ✅ **Step 6: Creating a Join View (Multiple Tables)**

```sql
create view emp_dept_view as
select 
    e.emp_id,
    e.emp_name,
    e.salary,
    d.dept_name
from EmployeeV e
join Department d
on e.dept_id = d.dept_id;

```

```sql
select * from emp_dept_view;
```
<img width="1133" height="366" alt="image" src="https://github.com/user-attachments/assets/3a55bace-65dd-4fd5-80a6-98df105ccd9e" />


---

## ✅ **Step 7: Advanced Summarization View**

```sql
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


```

```sql
select * from dept_summary; 
```
<img width="1133" height="292" alt="image" src="https://github.com/user-attachments/assets/8cce1b71-8d2f-46ac-b5e9-1c9374933583" />


---

## ✅ **Step 8: Modifying View**

```sql
create or replace view active_employees as
select emp_id, emp_name, salary
from EmployeeV
where status = 'Active';

```

```sql
select * from active_employees;
```
<img width="864" height="266" alt="image" src="https://github.com/user-attachments/assets/9e614486-6ae2-400b-bab0-ad95cf6551b2" />

---

## 📥📤 **6. I/O Analysis (Input / Output)**

### 🔹 Input  
- Creation of base tables (Employee & Department)  
- Insertion of sample records  
- SQL commands for simple and complex views  
- JOIN operations inside views  
- Aggregate functions for summary views  

### 🔹 Output  
- Virtual tables created successfully  
- Filtered employee data displayed  
- Combined employee-department data retrieved  
- Department-level statistics generated  
- Simplified reporting queries  
- Real-time updated results when base tables change  

📸 Screenshots of execution and obtained results are attached.

---

## 📘 **7. Learning Outcomes**

- Students can create and manage simple and complex views.  
- Students understand abstraction using virtual tables.  
- Students can implement view-based security concepts.  
- Students can simplify reporting using JOIN and aggregation views.  
- Students can apply views in real-world systems like Payroll or Library Management.  

---

## 📂 **Repository Contents**
- README.md  
- Worksheet (Word & PDF)  
- SQL Queries  
- Screenshots  

---
