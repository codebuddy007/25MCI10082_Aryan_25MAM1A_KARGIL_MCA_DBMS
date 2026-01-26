# **DBMS Lab – Worksheet 1**  
## **Design and Implementation of Sample Database System using DDL, DML and DCL**

---

## 👨‍🎓 **Student Details**  
**Name:** Aryan  
**UID:** 25MCI10082  
**Branch:** MCA (AI & ML)  
**Semester:** 2nd  
**Section/Group:** 1/A  
**Subject:** DBMS Lab  
**Date of Performance:** 13/01/2026  

---

## 🎯 **Aim of the Session**  
To design and implement a sample database system using DDL, DML, and DCL commands for managing departments, employees, and projects, and to apply role-based access control for secure data handling.

---
## 💻 **Software Requirements**

- PostgreSQL (Database Server)  
- pgAdmin
- Windows Operating System  

---
## 📌 **Objective of the Session**  
- To understand the use of DDL commands to create and modify database structures.  
- To perform DML operations such as INSERT, UPDATE, DELETE, and SELECT.  
- To implement relationships using primary and foreign keys.  
- To apply DCL commands to manage roles and privileges.  
- To analyze input and output of SQL queries in a real database environment.  

---

## 🛠️ **Practical / Experiment Steps**  
- Design the database schema for Department, Employee, and Project tables.  
- Create tables using appropriate constraints.  
- Insert sample records into tables.  
- Perform update and delete operations.  
- Retrieve data using SELECT queries.  
- Create a role and grant and revoke privileges.  
- Alter and drop database objects.  

---

## 🗄️ **Database Design**  

The database is designed to manage Departments, Employees, and Projects within an organization.

### **Tables**  
- Department  
- Employee  
- Project  

### **Constraints Used**  
- PRIMARY KEY – to uniquely identify each record  
- FOREIGN KEY – to maintain relationships between tables  
- NOT NULL – to avoid missing important values  
- UNIQUE – to prevent duplicate entries  

---
# ⚙️ **Procedure of the Practical**

# ⚙️ **Step 1: Table Creation (DDL)**  

### **Department Table**
```sql
CREATE TABLE Department (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);
```

### **Employee Table**
```sql
CREATE TABLE Employee (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    salary NUMERIC(10,2) CHECK (salary > 0),
    dept_id INT NOT NULL,
    CONSTRAINT fk_department
        FOREIGN KEY (dept_id)
        REFERENCES Department(dept_id)
);
```

### **Project Table**
```sql
CREATE TABLE Project (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(150) NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);
```

---

# 🧾 **Step 2: Data Manipulation (DML)**  

### **Insert into Department**
```sql
INSERT INTO Department (dept_name)
VALUES
('HR'),
('IT'),
('Finance'),
('Marketing'),
('Operations'),
('Research');
```

<img width="536" height="350" alt="image" src="https://github.com/user-attachments/assets/cf68eec4-5d33-492b-b095-d465667f313f" />

### **Insert into Employee**
```sql
INSERT INTO Employee (emp_name, email, salary, dept_id)
VALUES
('Aryan', 'aryan@company.com', 55000, 2),
('Rahul', 'rahul@company.com', 60000, 1),
('Sneha', 'sneha@company.com', 50000, 3),
('Neha', 'neha@company.com', 62000, 2),
('Amit', 'amit@company.com', 45000, 4),
('Pooja', 'pooja@company.com', 70000, 5),
('Karan', 'karan@company.com', 52000, 6),
('Ritika', 'ritika@company.com', 58000, 1);
```
<img width="1125" height="440" alt="image" src="https://github.com/user-attachments/assets/e085aa44-73ad-4c4b-8bb1-50e39d025e08" />

### **Insert into Project**
```sql
INSERT INTO Project (project_name, start_date, end_date)
VALUES
('HR Automation', '2024-01-01', '2024-06-30'),
('Website Revamp', '2024-02-15', NULL),
('Marketing Analytics', '2024-03-01', '2024-09-30'),
('ERP Implementation', '2024-04-15', NULL),
('AI Research', '2024-01-10', '2025-01-10'),
('Customer Engagement Platform', '2024-05-01', NULL);
```
<img width="899" height="364" alt="image" src="https://github.com/user-attachments/assets/559ce117-e00c-48e8-80a8-22f0f22644bb" />

---

# ✏️ **Step 3: UPDATE Operation**  
```sql
UPDATE Employee
SET salary = 65000
WHERE emp_name = 'Aryan';

UPDATE Employee
SET salary = salary * 1.10
WHERE dept_id = 2;
```

<img width="1125" height="441" alt="image" src="https://github.com/user-attachments/assets/441aaf63-ff43-4de7-a330-7ce9fbc927b0" />

---

# 🗑️ **Step 4: DELETE Operations**  

(Employee 105 was assigned to a project, so the project record was deleted first.)

```sql
DELETE FROM Employee
WHERE dept_id = 1;

DELETE FROM Department
WHERE dept_id = 1;
```
<img width="708" height="408" alt="image" src="https://github.com/user-attachments/assets/4827a70d-7ea5-4c67-88f4-4b7eb1177465" />
<img width="1019" height="320" alt="image" src="https://github.com/user-attachments/assets/652a9a99-8b2f-4bc8-8289-0c2f79621bd3" />

---

# 🔐 **Step 5: Create Role and Assign Privileges**

### **Create Role**
```sql
CREATE ROLE reporting_user
WITH
    LOGIN
    PASSWORD 'report123';
```
<img width="561" height="336" alt="image" src="https://github.com/user-attachments/assets/e1e6b1dc-a137-4112-a528-66a2cd740578" />
<img width="690" height="45" alt="image" src="https://github.com/user-attachments/assets/e81acd18-983b-4187-a508-f458131d186d" />

### **Grant SELECT Privileges**
```sql
GRANT SELECT ON Department TO reporting_user;
GRANT SELECT ON Employee TO reporting_user;
GRANT SELECT ON Project TO reporting_user;
```

### **Revoke Privilege**
```sql
REVOKE CREATE ON SCHEMA public FROM reporting_user;
REVOKE INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM reporting_user;
```

---

# 🏗️ **Step 6: Schema Modification**

### **Add Column**
```sql
ALTER TABLE Employee
ADD COLUMN phone_number VARCHAR(15);
```

<img width="995" height="247" alt="image" src="https://github.com/user-attachments/assets/2820bbbe-f3c9-46ca-beea-597d2f2d6bf6" />

### **Drop Table**
```sql
DROP TABLE Project;
```
<img width="541" height="227" alt="image" src="https://github.com/user-attachments/assets/c0d504d1-5467-4cfc-a4fd-29e87ca0d34d" />

---

## 📘 **Learning Outcomes**  
- Understood the basics of relational database design using tables, keys, and relationships.  
- Learned to apply primary and foreign key constraints to maintain data integrity.  
- Gained hands-on experience with INSERT, UPDATE, and DELETE operations.  
- Understood role-based access control using GRANT and REVOKE.  
- Learned how to create read-only users for secure data access.  
- Practiced ALTER TABLE and DROP TABLE commands for schema management.  

---
