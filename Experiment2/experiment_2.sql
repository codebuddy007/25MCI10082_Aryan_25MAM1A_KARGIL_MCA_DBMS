CREATE TABLE customer_orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price NUMERIC(8,2),
    order_date DATE
);

INSERT INTO customer_orders
(customer_name, product, quantity, price, order_date)
VALUES
('Aryan', 'Laptop', 1, 55000, '2024-01-10'),
('Rahul', 'Mobile', 2, 30000, '2024-01-12'),
('Sneha', 'Laptop', 1, 60000, '2024-01-15'),
('Neha', 'Tablet', 3, 15000, '2024-01-18'),
('Amit', 'Mobile', 1, 28000, '2024-01-20');

SELECT *  FROM customer_orders

SELECT * FROM customer_orders
WHERE price > 30000;

SELECT * FROM customer_orders
ORDER BY price DESC;

SELECT product, SUM(price * quantity) AS total_sales
FROM customer_orders
GROUP BY product;

SELECT product, SUM(price * quantity) AS total_sales
FROM customer_orders
GROUP BY product
HAVING SUM(price * quantity) > 30000;


