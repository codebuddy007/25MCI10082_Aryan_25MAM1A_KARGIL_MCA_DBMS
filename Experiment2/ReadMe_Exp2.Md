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
**Date of Performance:** 22/01/2026  

---

## 🎯 **Aim of the Session**  
To implement and analyze SQL SELECT queries using filtering, sorting, grouping, and aggregation concepts in PostgreSQL for efficient data retrieval and analytical reporting.

---

## 💻 **Software Requirements**

- PostgreSQL (Database Server)  
- pgAdmin
- Windows Operating System  

---

## 📌 **Objective of the Session**  
- To retrieve specific data using filtering conditions  
- To sort query results using single and multiple attributes  
- To perform aggregation using grouping techniques  
- To apply conditions on aggregated data using HAVING clause  
- To understand real-world analytical queries commonly asked in placement interviews  

---

## 🛠️ **Practical / Experiment Steps**  
- Create a sample table representing customer orders  
- Insert realistic records into the table  
- Retrieve filtered data using WHERE clause  
- Sort query results using ORDER BY  
- Group records and apply aggregate functions  
- Apply conditions on grouped data using HAVING  
- Analyze execution order of WHERE and HAVING clauses  

---

# ⚙️ **Procedure of the Practical**

## **Step 1: Database and Table Creation**

```sql
create database Experiment2;
```

```sql
CREATE TABLE customer_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price NUMERIC(8,2),
    order_date DATE
);
```

---

## **Step 2: Insert Records (DML)**

```sql
INSERT INTO customer_orders
(customer_name, product, quantity, price, order_date)
VALUES
('Aryan', 'Laptop', 1, 55000, '2024-01-10'),
('Rahul', 'Mobile', 2, 30000, '2024-01-12'),
('Sneha', 'Laptop', 1, 60000, '2024-01-15'),
('Neha', 'Tablet', 3, 15000, '2024-01-18'),
('Amit', 'Mobile', 1, 28000, '2024-01-20');
```

---

## **Step 3: Display All Records**

```sql
select * from customer_orders;
```

<img width="1125" height="387" alt="image" src="https://github.com/user-attachments/assets/bb8f886d-073e-4957-a41a-50968468de3e" />

---

## **Step 4: Filtering Data Using WHERE Clause**

```sql
SELECT * FROM customer_orders
WHERE price > 30000;

```
<img width="1020" height="244" alt="image" src="https://github.com/user-attachments/assets/a4da601f-3065-4b24-9193-5375702fd542" />

---

## **Step 5: Sorting Query Results**

### **Ascending Order**
```sql
SELECT * FROM customer_orders
ORDER BY price DESC;

```
<img width="1013" height="242" alt="image" src="https://github.com/user-attachments/assets/1645b309-a337-42c5-bd95-ea0b2dbf800f" />


## **Step 6: Grouping Data for Aggregation**

```sql
SELECT product, SUM(price * quantity) AS total_sales
FROM customer_orders
GROUP BY product;

```
<img width="530" height="320" alt="image" src="https://github.com/user-attachments/assets/931b4c80-7d5d-4a05-8b8a-a21df6b2d17f" />

---

## **Step 7: Applying Conditions on Aggregated Data (HAVING)**

```sql
SELECT product, SUM(price * quantity) AS total_sales
FROM customer_orders
GROUP BY product
HAVING SUM(price * quantity) > 30000;

```
<img width="656" height="211" alt="image" src="https://github.com/user-attachments/assets/8be53c62-3230-4ba1-8219-7177bc58524e" />

---

## **Step 8: Using WHERE and HAVING Together**

```sql
select product, sum(quantity*price) as total_revenue
from customer_orders
where order_date >= '2025-01-01'
group by product
having sum(quantity*price) > 50000;
```
<img width="728" height="226" alt="image" src="https://github.com/user-attachments/assets/df807258-ae9f-4526-812c-edb81b12b1c0" />

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
- Students understand how data can be filtered to retrieve only relevant records.  
- Students learn how sorting improves readability and usefulness of reports.  
- Students gain the ability to group data for analytical purposes.  
- Students clearly differentiate between WHERE and HAVING clauses.  
- Students develop confidence in writing analytical SQL queries.  
- Students are better prepared for SQL-based placement and interview questions.

---

## 📂 **Repository Contents**
- README.md  
- Worksheet (Word & PDF)  
- SQL Queries  
- Screenshots  

---
