CREATE TABLE IF NOT EXISTS Salesman(
Store_salesman_id INT PRIMARY KEY,
Name TEXT,
City TEXT,
Commision REAL);

INSERT INTO Salesman(Store_salesman_id,Name,City,Commision)VALUES
(5001,"James Hoog","New York",0.15),
(5002,"Nail Knite","Paris",0.13),
(5005,"Pit Alex","London",0.11),
(5006,"Mc Lyon","Paris",0.14),
(5007,"Paul Adam","Rome",0.13),
(5003,"Lauson Hen","San Jose",0.12);

CREATE TABLE IF NOT EXISTS Customer(
Store_customer_id INT PRIMARY KEY,
Name TEXT,
City TEXT,
Grade INT,
Salesman_id INT);

INSERT INTO Customer(Store_customer_id,Name,City,Grade,Salesman_id)VALUES
(3002,"Nick Rimando","New York",100,5001),
(3007,"Brad Davis","New York",200,5001),
(3005,"Graham Zusi","California",200,5002),
(3008,"Julian Green","London",300,5002),
(3004,"Fabian Johnson","Paris",300,5006),
(3009,"Geoff Cameron","Berlin",100,5003),
(3003,"Jozy Altidor","Moscow",200,5007),
(3001,"Brad Guzan","London",NULL,5005);

CREATE TABLE IF NOT EXISTS Orders(
Store_order_number INT PRIMARY KEY,
Purchase_amount INT,
Date TEXT,
Customer_id INT,
Salesman_id INT);

INSERT INTO Orders (Store_order_number,Purchase_amount,Date,Customer_id,Salesman_id)VALUES
(70001,150.5,'2012-10-05',3005,5002),
(70009,270.65,'2012-09-10',3001,5001),
(70002,65.26,'2012-10-05',3002,5003),
(70004,110.5,'2012-08-17',3009,5007),
(70007,948.5,'2012-09-10',3005,5005),
(70005,2400.6,'2012-07-27',3007,5006);

SELECT * FROM Salesman;
SELECT * FROM Customer;
SELECT * FROM Orders;

SELECT Customer.Name,Salesman.Name FROM Customer JOIN Salesman ON Customer.Salesman_id=Salesman.Store_salesman_id;
SELECT Customer.Name,Salesman.Name,Salesman.City FROM Customer JOIN Salesman ON Customer.City=Salesman.City;
SELECT Orders.Store_order_number,Customer.Name,Orders.Customer_id,Orders.Salesman_id FROM Orders JOIN Customer ON Orders.Customer_id=Customer.Store_customer_id JOIN Salesman ON Orders.Salesman_id=Salesman.Store_salesman_id WHERE LOWER(Customer.City) <> LOWER(Salesman.City);
SELECT Orders.Store_order_number,Customer.Name FROM Customer JOIN Orders ON Orders.Customer_id=Customer.Store_customer_id;
SELECT Customer.Name,Customer.Grade FROM Customer JOIN Salesman ON Customer.Salesman_id=Salesman.Store_salesman_id WHERE Customer.Grade IS NOT NULL;
SELECT Customer.Name,Salesman.Name,Salesman.Commision FROM Salesman JOIN Customer ON Customer.Salesman_id=Salesman.Store_salesman_id WHERE Salesman.Commision BETWEEN 0.12 AND 0.14;
SELECT Orders.Store_order_number,Customer.Name,Customer.Grade,Salesman.Commision AS "Commision %",Orders.Purchase_amount*Salesman.Commision AS "Commision" FROM Customer JOIN Salesman ON Customer.Salesman_id=Salesman.Store_salesman_id JOIN Orders ON Orders.Customer_id=Customer.Store_customer_id WHERE Customer.Grade>=200;
SELECT Orders.*,Customer.* FROM Customer JOIN Orders ON Orders.Customer_id=Customer.Store_customer_id WHERE Orders.Date="2012-10-05";