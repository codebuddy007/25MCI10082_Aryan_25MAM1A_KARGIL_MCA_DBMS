-- DROP TABLES (optional, to avoid errors if re-running)
DROP TABLE IF EXISTS Tbl_Supply_logs;
DROP TABLE IF EXISTS Tbl_Orders;
DROP TABLE IF EXISTS Tbl_Suppliers;
DROP TABLE IF EXISTS Tbl_Products;

-- =========================
-- CREATE TABLES
-- =========================

CREATE TABLE Tbl_Products (
    prod_id INT PRIMARY KEY,
    prod_name VARCHAR(100),
    category VARCHAR(50),
    price INT,
    stock_qty INT
);

CREATE TABLE Tbl_Suppliers (
    sup_id INT PRIMARY KEY,
    sup_name VARCHAR(100),
    city VARCHAR(50),
    rating INT
);

CREATE TABLE Tbl_Orders (
    order_id INT PRIMARY KEY,
    prod_id INT,
    cust_id INT,
    order_date DATE,
    qty INT,
    FOREIGN KEY (prod_id) REFERENCES Tbl_Products(prod_id)
);

CREATE TABLE Tbl_Supply_logs (
    log_id INT PRIMARY KEY,
    action_type VARCHAR(20),
    prod_id INT,
    old_qty INT,
    new_qty INT,
    log_time TIMESTAMP,
    FOREIGN KEY (prod_id) REFERENCES Tbl_Products(prod_id)
);

-- =========================
-- INSERT DATA
-- =========================

-- Products
INSERT INTO Tbl_Products VALUES
(501, 'Laptop Pro', 'Electronics', 75000, 15),
(502, 'Ergo Chair', 'Furniture', 15000, 8);

-- Suppliers
INSERT INTO Tbl_Suppliers VALUES
(701, 'NextGen Tech', 'Bangalore', 5),
(702, 'Comfort Hub', 'Mumbai', 4);

-- Orders
INSERT INTO Tbl_Orders VALUES
(9001, 501, 101, '2026-04-20', 1),
(9002, 502, 102, '2026-04-21', 2);

-- Supply Logs
INSERT INTO Tbl_Supply_logs VALUES
(1, 'UPDATE', 501, 20, 15, '2026-04-20 10:00:00');

-- =========================
-- VERIFY
-- =========================

SELECT * FROM Tbl_Products;
SELECT * FROM Tbl_Suppliers;
SELECT * FROM Tbl_Orders;
SELECT * FROM Tbl_Supply_logs;


-- Q1 Ans
SELECT p.prod_name,
COALESCE(SUM(o.qty),0) AS tota_quantity
FROM Tbl_products p
LEFT JOIN Tbl_Orders o
ON p.prod_id = o.prod_id
GROUP BY p.prod_name

-- Q2 Ans
CREATE OR REPLACE FUNCTION check_stock_before_insert()
RETURNS TRIGGER AS $$
DECLARE
    available_stock INT;
BEGIN
    SELECT stock_qty INTO available_stock
    FROM Tbl_Products
    WHERE prod_id = NEW.prod_id;

    IF available_stock IS NULL THEN
        RAISE EXCEPTION 'Product with ID % does not exist', NEW.prod_id;
    END IF;

    IF NEW.qty > available_stock THEN
        RAISE EXCEPTION 
        'Insufficient stock! Available: %, Requested: %',
        available_stock, NEW.qty;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_stock
BEFORE INSERT ON Tbl_Orders
FOR EACH ROW
EXECUTE FUNCTION check_stock_before_insert();

INSERT INTO Tbl_Orders VALUES (9003, 501, 103, '2026-04-25', 50);
INSERT INTO Tbl_Orders VALUES (9004, 501, 104, '2026-04-25', 5);




