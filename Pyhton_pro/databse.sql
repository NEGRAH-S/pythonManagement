CREATE TABLE people (
account_number INT PRIMARY KEY,
name VARCHAR(255),
balance DECIMAL(10,2)
);
INSERT INTO people (account_number, name, balance) VALUES
(1, 'nikku', 1000.00),
(2, 'Jane Doe', 2000.00),
(3, 'Bill Smith', 3000.00),
(4, 'Mary Johnson', 4000.00),
(5, 'Mike Jones', 5000.00),
(6, 'Susan Williams', 6000.00),
(7, 'David Brown', 7000.00),
(8, 'Elizabeth Green', 8000.00),
(9, 'Michael White', 9000.00),
(10, 'Sarah Black', 10000.00);
