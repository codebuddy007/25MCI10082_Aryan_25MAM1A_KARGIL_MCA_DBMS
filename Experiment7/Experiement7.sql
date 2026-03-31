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

--1. Write queries to list students with their enrolled courses (INNER JOIN).
SELECT s.name,c.course_name
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

--2. Find students not enrolled in any course (LEFT JOIN).
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;


--  3. Display all courses with or without enrolled students (RIGHT JOIN).
SELECT c.course_name, s.name
FROM students s
RIGHT JOIN enrollments e ON s.student_id = e.student_id
RIGHT JOIN courses c ON e.course_id = c.course_id;


--  4. Show students with department info using SELF JOIN or multiple joins.
SELECT s.name, d.department_name
FROM students s
LEFT JOIN departments d ON s.department_id = d.department_id;


--  5. Display all possible student-course combinations (CROSS JOIN). 
SELECT s.name, c.course_name
FROM students s
CROSS JOIN courses c;