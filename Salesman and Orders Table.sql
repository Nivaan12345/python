CREATE TABLE IF NOT EXISTS Salesman(
Salesman_id TEXT PRIMARY KEY,
name TEXT,
city TEXT,
Commision REAL
);

INSERT INTO Salesman(Salesman_id,name,city,Commision)VALUES
("5001","James Hoog","New York",0.15),
("5002","Nail Knite","Paris",0.13),
("5005","Pit Alex","London",0.11),
("5006","Mc Lyon","Paris",0.14),
("5007","Paul Adam","Rome",0.13),
("5003","Lauson Hen","San Jose",0.12);

SELECT * FROM Salesman;

Create TABLE Orders(
ord_no TEXT PRIMARY KEY,
purch_amt REAL,
ord_date TEXT,
customer_id TEXT,
Salesman_id TEXT);

INSERT INTO Orders(ord_no,purch_amt,ord_date,customer_id,Salesman_id)VALUES
("70001",150.5,"2012-10-05","3005","5062"),
("70009",270.65,"2012-09-10","3001","5002"),
("70002",65.26,"2012-08-17","3003","5702"),
("70004",110.5,"2012-10-05","3405","5002"),
("70007",948.5,"2012-10-05","3005","5032"),
("70005",2400.6,"2012-10-05","3905","5022");

SELECT * FROM Orders;

SELECT name,Commision FROM Salesman;