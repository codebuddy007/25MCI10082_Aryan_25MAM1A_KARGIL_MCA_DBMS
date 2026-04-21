CREATE TABLE Employees ( 
emp_id INT PRIMARY KEY, 
emp_name VARCHAR(50), 
manager_id INT, 
department VARCHAR(50), 
salary INT 
); 
INSERT INTO Employees VALUES 
(1, 'Amit', NULL, 'Management', 120000), 
(2, 'Ravi', 1, 'Engineering', 80000), 
(3, 'Neha', 1, 'Engineering', 82000), 
(4, 'Karan', 2, 'Engineering', 60000), 
(5, 'Simran', 2, 'Engineering', 62000), 
(6, 'Pooja', 3, 'Engineering', 61000), 
(7, 'Rahul', 3, 'Engineering', 64000), 
(8, 'Arjun', 1, 'HR', 70000);
select *  from employees;

CREATE OR REPLACE PROCEDURE add_employee( 
p_id INT, 
p_name VARCHAR, 
p_manager INT, 
p_dept VARCHAR, 
p_salary INT 
) 
LANGUAGE plpgsql 
AS $$ 
BEGIN 
INSERT INTO Employees VALUES (p_id, p_name, p_manager, p_dept, p_salary); 
END; 
$$;
--call:
CALL add_employee(9, 'Ankit', 2, 'Engineering', 65000);

create or replace Procedure UPDATE_SALARY_PROCC(IN P_EMP_ID int, INOUT P_SALARY numeric(20,3) , OUT STATUS 
varchar(20)) 
AS  
$$ 
DECLARE  
CURR_SAL NUMERIC(20,3); 
BEGIN  
SELECT SALARY+P_SALARY INTO CURR_SAL FROM employees WHERE EMP_ID = P_EMP_ID; 
IF NOT FOUND THEN 
RAISE EXCEPTION 'EMPLOYEE NOT FOUND'; 
END IF ; 
UPDATE employees  
SET SALARY = CURR_SAL WHERE EMP_ID = P_EMP_ID; 
P_SALARY:= CURR_SAL; 
STATUS :='SUCCESS'; 
EXCEPTION  
WHEN OTHERS THEN  
IF SQLERRM LIKE '%EMPLOYEE NOT FOUND%' THEN  
STATUS:='EMPLOYEE NOT FOUND'; 
END IF; 
END; 
$$ LANGUAGE PLPGSQL ; 
--call:
DO 
$$ 
DECLARE  
EMP_ID INT :=3; 
STATUS VARCHAR(20); 
SALARY NUMERIC(20,3):=525; 
BEGIN 
CALL UPDATE_SALARY_PROCC(EMP_ID ,SALARY , STATUS); 
RAISE NOTICE 'YOUR STATUS IS % AND THE UPDATED SALARY IS %',STATUS , SALARY; 
END; 
$$

CREATE OR REPLACE PROCEDURE delete_employee( 
p_id INT 
) 
LANGUAGE plpgsql 
AS $$ 
BEGIN 
DELETE FROM Employees 
WHERE emp_id = p_id; 
END; 
$$;
--call:
CALL delete_employee(5);