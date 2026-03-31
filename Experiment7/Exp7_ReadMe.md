# **DBMS Lab – Worksheet 2**  
## **Implementation of SELECT Queries with Filtering, Grouping and Sorting in PostgreSQL**

---

## 👨‍🎓 **Student Details**  
**Name:** Aryan
**UID:** 25MCI10082  
**Branch:** MCA (AI & ML)  
**Semester:** 2nd  
**Section/Group:** 1/A  
**Subject:** DBMS Lab  
**Date of Performance:** 30/03/2026  

---

## 🎯 **Aim of the Session**  
Implementation of joins in PostgreSQL (inner join ,left join,right join, self join and cross join).
---

## 💻 **Software Requirements**

- PostgreSQL (Database Server)  
- pgAdmin
- Windows Operating System  

---

## 📌 **Objective of the Session**  
Apply joins to a real-world database schema (e.g., Students, Courses, Enrollments, Departments)

---

## 🛠️ **Practical / Experiment Steps**  
- Design the database schema for different tables.  
- Create table using appropriate constraints.  
- Insert sample records into tables.  
- Perform joins. 
  

---

# ⚙️ **Procedure of the Practical**

## **Step 1: Database and Table Creation**

```sql
create database Experiment7;
```

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50)
);
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

---

## **Step 2: Insert Records (DML)**

```sql
INSERT INTO departments VALUES
(1, 'Computer Science'),
(2, 'Mechanical'),
(3, 'Electrical');

INSERT INTO students VALUES
(1, 'Aryan', 1),
(2, 'Rohit', 2),
(3, 'Priya', 1),
(4, 'Simran', 3),
(5, 'Karan', NULL);

INSERT INTO courses VALUES
(101, 'DBMS'),
(102, 'OS'),
(103, 'Maths'),
(104, 'Physics');

INSERT INTO enrollments VALUES
(1, 101),
(1, 102),
(2, 103),
(3, 101);

```

---



## **Step 3: Queries to list students with their enrolled courses (INNER JOIN).**

```sql
SELECT s.name,c.course_name
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

```
<img width="519" height="217" alt="image" src="https://github.com/user-attachments/assets/d621ad22-733a-4274-9cc2-6d9106779b1f" />


---

## **Step 4: Students not enrolled in any course (LEFT JOIN).**

### **Ascending Order**
```sql
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;


```
<img width="455" height="213" alt="image" src="https://github.com/user-attachments/assets/3a20fb21-650c-40c0-8c45-5ce5b8f7c224" />



## **Step 5: Courses with or without enrolled students (RIGHT JOIN)**

```sql
SELECT c.course_name, s.name
FROM students s
RIGHT JOIN enrollments e ON s.student_id = e.student_id
RIGHT JOIN courses c ON e.course_id = c.course_id;

```
<img width="597" height="291" alt="image" src="https://github.com/user-attachments/assets/3af3c382-2a11-42cf-a490-ffb75c6f353a" />


---

## **Step 6: Students with department info using SELF JOIN or multiple joins.**

```sql
SELECT s.name, d.department_name
FROM students s
LEFT JOIN departments d ON s.department_id = d.department_id;

```
<img width="721" height="351" alt="image" src="https://github.com/user-attachments/assets/cd895109-0eb1-488a-8574-e6818ee7cb14" />


---

## **Step 7: Display all possible student-course combinations (CROSS JOIN).**

```sql
SELECT s.name, c.course_name
FROM students s
CROSS JOIN courses c;
```
<img width="450" height="706" alt="image" src="https://github.com/user-attachments/assets/526c6711-8ffc-4e03-a529-3659ed2193ab" />

---

## 📥📤 **I/O Analysis (Input / Output)**

### **Input**
- Customer order details  
- Filtering, sorting, grouping, and aggregation queries  

### **Output**
- Filtered customer records  
- Sorted result sets  
- Group-wise sales summary  
- Aggregated revenue reports  

📸 Screenshots of execution and output are attached in this repository.

---

## 📘 **Learning Outcomes**  
•	Understand the concept of relational databases and how data is distributed across multiple tables. 
•	Apply different types of SQL joins such as INNER JOIN, LEFT JOIN, RIGHT JOIN, SELF JOIN, and CROSS JOIN. 
•	Retrieve meaningful information by combining data from multiple related tables like Students, Courses, Enrollments, and Departments. 
•	Identify the appropriate join type based on the problem requirement and data relationship. 
•	Analyze query results to understand how NULL values and unmatched records are handled in different joins.


---

## 📂 **Repository Contents**
- README.md  
- Worksheet (Word & PDF)  
- SQL Queries  
- Screenshots  

---
