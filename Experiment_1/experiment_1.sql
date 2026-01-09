-- Table Creation

CREATE TABLE Department (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL UNIQUE
);

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

CREATE TABLE Project (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(150) NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE,
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Data Insertion

INSERT INTO Department (dept_name)
VALUES
('HR'),
('IT'),
('Finance'),
('Marketing'),
('Operations'),
('Research');

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

INSERT INTO Project (project_name, start_date, end_date)
VALUES
('HR Automation', '2024-01-01', '2024-06-30'),
('Website Revamp', '2024-02-15', NULL),
('Marketing Analytics', '2024-03-01', '2024-09-30'),
('ERP Implementation', '2024-04-15', NULL),
('AI Research', '2024-01-10', '2025-01-10'),
('Customer Engagement Platform', '2024-05-01', NULL);

-- Update Commands

UPDATE Employee
SET salary = 65000
WHERE emp_name = 'Aryan';

UPDATE Employee
SET salary = salary * 1.10
WHERE dept_id = 2;

UPDATE Employee
SET dept_id = 1
WHERE emp_name = 'Sneha';

UPDATE Project
SET end_date = '2024-12-31'
WHERE project_name = 'ERP Implementation';

-- Delete Commands
DELETE FROM Employee
WHERE dept_id = 1;

DELETE FROM Department
WHERE dept_id = 1;

-- Role Creation
CREATE ROLE reporting_user
WITH
    LOGIN
    PASSWORD 'report123';

GRANT SELECT ON Department TO reporting_user;
GRANT SELECT ON Employee TO reporting_user;
GRANT SELECT ON Project TO reporting_user;

REVOKE CREATE ON SCHEMA public FROM reporting_user;
REVOKE INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM reporting_user;

-- Role verifiction
SET ROLE reporting_user;
SELECT * FROM Employee;    
INSERT INTO Employee (emp_name, email, salary, dept_id)
VALUES ('Test User', 'testuser@company.com', 40000, 2);  

-- Role Reset
RESET ROLE;

-- Alter Table
ALTER TABLE Employee
ADD COLUMN phone_number VARCHAR(15);

ALTER TABLE Employee
ADD COLUMN joining_date DATE NOT NULL DEFAULT CURRENT_DATE;

-- Drop Table
-- DROP TABLE Project;





