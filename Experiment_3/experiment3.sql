-- Creation
CREATE TABLE schema_violations (
    schema_id INT PRIMARY KEY,
    schema_name VARCHAR(50),
    violation_count INT
);

--Insertion
INSERT INTO schema_violations VALUES
(1, 'Finance', 0),
(2, 'HR', 2),
(3, 'Sales', 6),
(4, 'Audit', 12);

SELECT * FROM schema_violations

--Step 1: Classifying Data Using CASE Expression
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

--Step 2: Applying CASE Logic in Data Updates 

ALTER TABLE schema_violations
ADD COLUMN approval_status VARCHAR(20);

UPDATE schema_violations
SET approval_status =
    CASE
        WHEN violation_count = 0 THEN 'Approved'
        WHEN violation_count <= 5 THEN 'Review'
        ELSE 'Rejected'
    END;

--Step 3: Implementing IF–ELSE Logic Using PL/pgSQL

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


--Step 4: Real-World Classification Scenario (Grading System)

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

SELECT * FROM students

-- Grade Classification
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

--Step 5: Using CASE for Custom Sorting

SELECT schema_name, violation_count
FROM schema_violations
ORDER BY
    CASE
        WHEN violation_count = 0 THEN 1
        WHEN violation_count <= 3 THEN 2
        WHEN violation_count <= 7 THEN 3
        ELSE 4
    END;


