# **DBMS Lab – Worksheet 4**  
## **Implementation of Iterative Control Structures in PostgreSQL**

---

## 👨‍🎓 **Student Details**  
**Name:** Aryan 
**UID:** 25MCI10082  
**Branch:** MCA (AI & ML)  
**Semester:** 2nd  
**Section/Group:** 1/A  
**Subject:** DBMS Lab  
**Subject Code:** 25CAP-652  
**Date of Performance:** 04/02/2026  

---

## 🎯 **Aim of the Session**  
To understand and implement iterative control structures in PostgreSQL conceptually, including FOR loops, WHILE loops, and basic LOOP constructs, for repeated execution of database logic.

---

## 💻 **Software Requirements**  
- PostgreSQL (Database Server)  
- pgAdmin  
- Windows Operating System  

---

## 📌 **Objective of the Session**  
- To understand why iteration is required in database programming  
- To learn the purpose and behavior of FOR, WHILE, and LOOP constructs  
- To understand how repeated data processing is handled in databases  
- To relate loop concepts to real-world batch processing scenarios  
- To strengthen conceptual knowledge of procedural SQL used in enterprise systems  

---

## 🛠️ **Practical / Experiment Steps**

### **Prerequisite Understanding**
- Iterative control structures are executed inside PL/pgSQL blocks, not normal SQL queries  
- A table containing multiple records is required to demonstrate loop execution  
- The table should include:
  - A unique identifier  
  - A descriptive attribute  
  - A numeric value for repeated processing  

---

# ⚙️ **Procedure of the Practical**

---

## ✅ **Step 1: Database Creation**

```sql
create database Practical4;
```

---

## ✅ **Step 2: Table Creation**

```sql
CREATE TABLE employee ( emp_id SERIAL PRIMARY KEY,
emp_name VARCHAR(50), salary NUMERIC(10,2)
);
```

---

## ✅ **Step 3: Insert Records**

```sql
INSERT INTO employee (emp_name, salary) VALUES
('Amit Sharma', 45000.00),
('Neha Verma', 52000.50),
('Rahul Mehta', 60000.00),
('Priya Singh', 48000.75),
('Karan Gupta', 55000.00),
('Anjali Rao', 62000.25);
```

---

## ✅ **Step 4: Display Records**

```sql
select * from employee;
```
<img width="663" height="323" alt="image" src="https://github.com/user-attachments/assets/e4949bcd-8938-41ae-861a-8c8ebc092a62" />

---

## ✅ **Step 5: FOR Loop – Simple Iteration**

```sql
DO $$ BEGIN
FOR i IN 1..6 LOOP
RAISE NOTICE 'Iteration number: %', i; END LOOP;
END $$;
```
<img width="531" height="336" alt="image" src="https://github.com/user-attachments/assets/d7916c72-1768-4e19-a63d-61f2c2c316e3" />

---

## ✅ **Step 6: FOR Loop with Query (Row-by-Row Processing)**

```sql
DO $$ DECLARE
emp RECORD; BEGIN
FOR emp IN SELECT emp_id, emp_name FROM employee LOOP
RAISE NOTICE 'Employee ID is % and Name is %', emp.emp_id, emp.emp_name; END LOOP;
END $$;
```
<img width="641" height="305" alt="image" src="https://github.com/user-attachments/assets/444c6115-c772-4645-9ea4-bcb624aef7eb" />

---

## ✅ **Step 7: WHILE Loop – Conditional Iteration**

```sql
DO $$ DECLARE
counter INT := 1; BEGIN
WHILE counter <= 6 LOOP
RAISE NOTICE 'Counter is %', counter; counter := counter + 1;
END LOOP;
END $$;
```
<img width="525" height="325" alt="image" src="https://github.com/user-attachments/assets/a21a0627-9c6d-4fe4-a428-e04d7eeed531" />

---

## ✅ **Step 8: LOOP with EXIT WHEN**

```sql
DO $$ DECLARE
x INT := 1; BEGIN
LOOP
RAISE NOTICE 'Value is %', x; x := x + 1;
EXIT WHEN x > 6; END LOOP;
END $$;
```
<img width="703" height="441" alt="image" src="https://github.com/user-attachments/assets/b8cad21f-10fa-456b-a443-7c2efe3ec9b4" />

---

## ✅ **Step 9: Salary Increment Using FOR Loop**

```sql
DO $$ DECLARE
emp RECORD; BEGIN
FOR emp IN SELECT emp_id, salary FROM employee LOOP UPDATE employee
SET salary = salary * 1.25 WHERE emp_id = emp.emp_id;
END LOOP;
END $$;

```

```sql
select * from employee;
```
<img width="698" height="339" alt="image" src="https://github.com/user-attachments/assets/70b6d943-1e3c-4bee-bda7-4b675f835eea" />

---

## ✅ **Step 10: Combining LOOP with IF Condition**

```sql
DO $$ DECLARE
emp RECORD; BEGIN
FOR emp IN SELECT emp_name, salary FROM employee LOOP IF emp.salary > 70000 THEN
RAISE NOTICE '% is a High Earner', emp.emp_name; ELSE
RAISE NOTICE '% is a Regular Employee', emp.emp_name; END IF;
END LOOP;
END $$;
```
<img width="629" height="398" alt="image" src="https://github.com/user-attachments/assets/b968647e-d113-4d52-b5a2-c926fdf83ae1" />

---

## 📥📤 **6. I/O Analysis (Input / Output)**

### 🔹 Input  
- Employee records stored in a table for iterative processing  
- PL/pgSQL DO blocks containing procedural logic  
- FOR loops for fixed-range and query-based iteration  
- WHILE loop for condition-based execution  
- LOOP construct with EXIT WHEN condition  
- IF–ELSE logic used inside loops  
- UPDATE statements executed repeatedly  

### 🔹 Output  
- Repeated execution of SQL statements using loops  
- Row-by-row processing of table records  
- Conditional messages displayed during iteration  
- Salary updates applied using iterative logic  
- Proper termination of loops based on conditions  
- Successful execution of procedural SQL demonstrating iteration control  

📸 Screenshots of execution and obtained results are attached.

---

## 📘 **7. Learning Outcomes**

- Understood the need for iterative control structures in database programming  
- Learned the usage of FOR, WHILE, and LOOP constructs in PostgreSQL  
- Gained knowledge of executing repeated logic using PL/pgSQL  
- Understood row-by-row processing and conditional execution in databases  
- Developed foundational skills for writing procedural SQL in real-world applications  

---

## 📂 **Repository Contents**
- README.md  
- Worksheet (Word & PDF)  
- SQL Queries  
- Screenshots  

---
