# **DBMS Lab – Worksheet 5**  
## **Implementation of Cursors for Row-by-Row Processing in PostgreSQL**

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
To gain hands-on experience in creating and using cursors for row-by-row processing in a database, enabling sequential access and manipulation of query results for complex business logic.

(Company Relevance: Infosys, Wipro, TCS, Capgemini)

---

## 💻 **Software Requirements**  
- PostgreSQL (Database Server)  
- pgAdmin  
- Windows Operating System  

---

## 📌 **Objective of the Session**  

- **Sequential Data Access:** To fetch rows one by one using cursor mechanisms.  
- **Row-Level Manipulation:** To perform conditional logic and calculations on individual records.  
- **Resource Management:** To understand DECLARE, OPEN, FETCH, CLOSE lifecycle of cursors.  
- **Exception Handling:** To handle cursor-related edge cases such as empty result sets.  

---

## 🛠️ **Practical / Experiment Steps**

### **Prerequisite Understanding**
- Cursors are used inside PL/pgSQL blocks for row-by-row processing.  
- Cursors differ from set-based SQL execution.  
- A table with multiple records is required for demonstration.  
- The table must include:
  - A primary key  
  - A descriptive column (e.g., employee name)  
  - A numeric column (e.g., salary or experience)  
- Cursor lifecycle includes DECLARE → OPEN → FETCH → CLOSE.  
- Basic IF–ELSE logic is required for conditional processing.  

---

# ⚙️ **Procedure of the Practical**

---

## ✅ **Step 1: Database Creation**

```sql
create database Practical5;
```

---

## ✅ **Step 2: Table Creation**

```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100),
    salary NUMERIC(10,2),
    experience INT );

```

---

## ✅ **Step 3: Insert Records**

```sql
INSERT INTO employees(emp_name,experience,salary) VALUES
('Amit',3,50000),
('Rohan',5,70000),
('Isha',2,45000),
('Sneha',4,60000),
('Anish',3,52000);
```

---

## ✅ **Step 4: Display Records**

```sql
SELECT*FROM employees;
```
<img width="849" height="285" alt="image" src="https://github.com/user-attachments/assets/b553065d-f54f-46d7-8163-1c759a7e49cd" />

---

## ✅ **Step 5: Implementing a Simple Forward-Only Cursor**

```sql
DO $$
	DECLARE
		emp_rec record;
		emp_cursor cursor for
		  SELECT emp_id,emp_name,salary FROM employees;
	BEGIN
	   OPEN emp_cursor;

	   LOOP
	   	 FETCH emp_cursor INTO emp_rec;
		 EXIT WHEN NOT FOUND;

		 RAISE NOTICE 'ID: %, Name: %, Salary: %',
        emp_rec.emp_id, emp_rec.emp_name, emp_rec.salary;
		END LOOP;
		CLOSE emp_cursor;
	END $$;


```
<img width="805" height="386" alt="image" src="https://github.com/user-attachments/assets/af6e391d-181c-40f0-956b-c36b98ed4812" />


---
## ✅ **Step 6: Complex Row-by-Row Manipulation**

```sql
do $$
declare
    emp_rec record;
    emp_cursor cursor for 
        select emp_id, experience, salary from employees;
begin
    open emp_cursor;

    loop
        fetch emp_cursor into emp_rec;
        exit when not found;

        if emp_rec.experience >= 4 then
            update employees
            set salary = salary * 1.35
            where emp_id = emp_rec.emp_id;

        elseif emp_rec.experience >= 3 then
            update employees
            set salary = salary * 1.20
            where emp_id = emp_rec.emp_id;

        else
            update employees
            set salary = salary * 1.10
            where emp_id = emp_rec.emp_id;
        end if;

    end loop;

    close emp_cursor;
end $$; 


```
<img width="1133" height="382" alt="image" src="https://github.com/user-attachments/assets/7f6cf24d-cc6e-4fc8-b869-1deec969a383" />

---

## ✅ **Step 7: Exception and Status Handling**

```sql
do $$
declare
    emp_rec record;
    emp_cursor cursor for 
        select * from employees where experience > 10;
begin
    open emp_cursor;
    fetch emp_cursor into emp_rec;
    if not found then
        raise notice 'No employees found with experience > 10.';
    else
        raise notice 'Employees exist.';
    end if;

    close emp_cursor;
end $$; 


```
<img width="839" height="187" alt="image" src="https://github.com/user-attachments/assets/f1711ab8-77bb-4691-a272-ccbff0445abb" />


---

## 📥📤 **6. I/O Analysis (Input / Output)**

### 🔹 Input  
- Employee records inserted into table  
- PL/pgSQL DO blocks containing cursor logic  
- DECLARE, OPEN, FETCH, CLOSE statements  
- IF–ELSE conditional logic  
- UPDATE statements inside cursor loops  
- Exception handling for empty result sets  

### 🔹 Output  
- Sequential row-by-row processing of employee records  
- Display of employee details using FETCH  
- Conditional salary updates based on experience  
- Notice messages generated during execution  
- Proper termination of cursor after processing  
- Successful handling of empty result sets  

📸 Screenshots of execution and obtained results are attached.

---

## 📘 **7. Learning Outcomes**

- Students can design and implement cursors for row-wise processing.  
- Students understand the complete cursor lifecycle.  
- Students can apply conditional business logic using cursors.  
- Students can handle empty result sets and prevent logical errors.  
- Students can apply cursor logic to real-world payroll and migration scenarios.  

---

## 📂 **Repository Contents**
- README.md  
- Worksheet (Word & PDF)  
- SQL Queries  
- Screenshots  

---
