CREATE TABLE employee ( emp_id SERIAL PRIMARY KEY,
emp_name VARCHAR(50), salary NUMERIC(10,2)
);

INSERT INTO employee (emp_name, salary) VALUES
('Amit Sharma', 45000.00),
('Neha Verma', 52000.50),
('Rahul Mehta', 60000.00),
('Priya Singh', 48000.75),
('Karan Gupta', 55000.00),
('Anjali Rao', 62000.25);

SELECT * FROM Employee;

DO $$ BEGIN
FOR i IN 1..6 LOOP
RAISE NOTICE 'Iteration number: %', i; END LOOP;
END $$;

DO $$ DECLARE
emp RECORD; BEGIN
FOR emp IN SELECT emp_id, emp_name FROM employee LOOP
RAISE NOTICE 'Employee ID is % and Name is %', emp.emp_id, emp.emp_name; END LOOP;
END $$;

DO $$ DECLARE
counter INT := 1; BEGIN
WHILE counter <= 6 LOOP
RAISE NOTICE 'Counter is %', counter; counter := counter + 1;
END LOOP;
END $$;

DO $$ DECLARE
x INT := 1; BEGIN
LOOP
RAISE NOTICE 'Value is %', x; x := x + 1;
EXIT WHEN x > 6; END LOOP;
END $$;

DO $$ DECLARE
emp RECORD; BEGIN
FOR emp IN SELECT emp_id, salary FROM employee LOOP UPDATE employee
SET salary = salary * 1.25 WHERE emp_id = emp.emp_id;
END LOOP;
END $$;
select*from employee;

DO $$ DECLARE
emp RECORD; BEGIN
FOR emp IN SELECT emp_name, salary FROM employee LOOP IF emp.salary > 70000 THEN
RAISE NOTICE '% is a High Earner', emp.emp_name; ELSE
RAISE NOTICE '% is a Regular Employee', emp.emp_name; END IF;
END LOOP;
END $$;



