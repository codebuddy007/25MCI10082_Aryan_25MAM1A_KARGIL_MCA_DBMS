x4

INSERT INTO employees(emp_name,experience,salary) VALUES
('Amit',3,50000),
('Rohan',5,70000),
('Isha',2,45000),
('Sneha',4,60000),
('Anish',3,52000);

SELECT*FROM employees;

--Implementing a Simple Forward-Only Cursor
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

----Complex Row-by-Row Manipulation

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

---Exception and Status Handling

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

