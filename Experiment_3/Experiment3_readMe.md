# **DBMS Lab – Worksheet 2**  
## **Design and Implementation of Sample Database System using DDL, DML and DCL**

---

## 👨‍🎓 **Student Details**  
**Name:** Aryan  
**UID:** 25MCI10082  
**Branch:** MCA (AI & ML)  
**Semester:** 2nd  
**Section/Group:** 1/A  
**Subject:** DBMS Lab  
**Date of Performance:** 27/01/2026  

---

## 🎯 **Aim of the Session**  
To implement conditional decision-making logic in PostgreSQL using IF–ELSE constructs and CASE expressions for classification, validation, and rule-based data processing.

---
## 💻 **Software Requirements**

- PostgreSQL (Database Server)  
- pgAdmin
- Windows Operating System  

---
## 📌 **Objective of the Session**  
•	To understand conditional execution in SQL
•	To implement decision-making logic using CASE expressions
•	To simulate real-world rule validation scenarios
•	To classify data based on multiple conditions
•	To strengthen SQL logic skills required in interviews and backend systems

---

## 🛠️ **Practical / Experiment Steps**  
•	Design the database schema for implementing conditional logic.
•	Create tables using appropriate constraints.
•	Insert sample records into tables.
•	Perform data classification using CASE expressions.
•	Perform conditional data updates using CASE logic.
•	Implement IF–ELSE logic using PL/pgSQL blocks.
•	Perform custom sorting using CASE expressions.
•	Display and verify results.  

---

## 🗄️ **Database Design**  

The database is designed to manage Departments, Employees, and Projects within an organization.

### **Table**  
- schema_violations

### **Constraints Used**  
- PRIMARY KEY – to uniquely identify each record  
- NOT NULL – to avoid missing important values  
- UNIQUE – to prevent duplicate entries  

---
# ⚙️ **Procedure of the Practical**

# ⚙️ **Step 1: Table Creation (DDL)**  

### **Schema Violation Table**
```sql
CREATE TABLE schema_violations (
    schema_id INT PRIMARY KEY,
    schema_name VARCHAR(50),
    violation_count INT 
);
```

---

# 🧾 **Step 2: Data Manipulation (DML)**  

### **Insert into Schema Violations**
```sql
INSERT INTO schema_violations VALUES
(1, 'Finance', 0),
(2, 'HR', 2),
(3, 'Sales', 6),
(4, 'Audit', 12);
```
<img width="688" height="249" alt="image" src="https://github.com/user-attachments/assets/5d99953e-703f-42b1-a28e-447517ee331d" />


---

# ✏️ **Step 3: Classifying Data Using CASE Expression**  
```sql
SELECT 
    schema_name,
    violation_count,
    CASE
        WHEN violation_count = 0 THEN 'No Violation'
        WHEN violation_count BETWEEN 1 AND 3 THEN 'Minor Violation'
        WHEN violation_count BETWEEN 4 AND 7 THEN 'Moderate Violation'
        ELSE 'Critical Violation'
    END AS violation_status
FROM schema_violations;
```

<img width="626" height="215" alt="image" src="https://github.com/user-attachments/assets/a3b137bb-0bb0-42a7-8767-521dee44f2e3" />

---

# 🗑️ **Step 4: Applying CASE Logic in Data Updates**  

```sql
ALTER TABLE schema_violations
ADD COLUMN approval_status VARCHAR(20);
UPDATE schema_violations
SET approval_status =
    CASE
        WHEN violation_count = 0 THEN 'Approved'
        WHEN violation_count <= 5 THEN 'Needs Review'       
ELSE 'Rejected'
    END;
```
<img width="726" height="191" alt="image" src="https://github.com/user-attachments/assets/a12b595d-2b1b-4782-a0f2-11dafa0e676b" />
---

# 🔐 **Step 5: Implementing IF–ELSE Logic Using PL/pgSQL.**

```sql
DO $$
DECLARE
    v_count INT := 6;
BEGIN
    IF v_count = 0 THEN
        RAISE NOTICE 'No violations detected.';
    ELSIF v_count <= 5 THEN
        RAISE NOTICE 'Minor issues found. Review required.';
    ELSE
        RAISE NOTICE 'Critical violations detected!';
    END IF;
END $$;

```
<img width="521" height="161" alt="image" src="https://github.com/user-attachments/assets/f90523d8-01f5-4283-95de-2b88423f7526" />

### **Real-World Classification Scenario (Grading System).**
```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    marks INT
);
INSERT INTO students VALUES
(1, 'Aman', 85),
(2, 'Riya', 72),
(3, 'Kunal', 58),
(4, 'Neha', 40);
```
<img width="585" height="235" alt="image" src="https://github.com/user-attachments/assets/806ddc6d-36e6-4f09-bc42-122fd74d954c" />

---

# 🏗️ **Grade Classification**

```sql
SELECT 
    student_name,
    marks,
    CASE
        WHEN marks >= 80 THEN 'A'
        WHEN marks >= 60 THEN 'B'
        WHEN marks >= 50 THEN 'C'
        ELSE 'Fail'
   
 END AS grade
FROM students;
```
<img width="621" height="275" alt="image" src="https://github.com/user-attachments/assets/deef5495-de77-4034-9c6a-a6630cfd9d4d" />

### **Using CASE for Custom Sorting**
```sql
SELECT schema_name, violation_count
FROM schema_violations
ORDER BY
    CASE
        WHEN violation_count = 0 THEN 1
        WHEN violation_count <= 3 THEN 2
        WHEN violation_count <= 7 THEN 3
        ELSE 4
    END;
```
<img width="626" height="297" alt="image" src="https://github.com/user-attachments/assets/6d2cd99b-05c7-47a6-970d-0d6da8462135" />

---

## 📘 **Learning Outcomes**  
•	How data can be filtered to retrieve only relevant records from a database.
•	Learn how sorting improves readability and usefulness of query results in reports.
•	Gain the ability to group data for analytical purposes. 
•	Differentiate between row-level conditions and group-level conditions.
•	Develop confidence in writing analytical SQL queries used in real-world scenarios.
•	Better prepared to answer SQL-based placement and interview questions related to filtering, grouping, and aggregation. 

---
