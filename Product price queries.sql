CREATE TABLE Product(
Pro_id TEXT PRIMARY KEY,
Pro_name TEXT,
Pro_price TEXT,
Pro_com TEXT);

INSERT INTO Product(Pro_id,Pro_name,Pro_price,Pro_com)VALUES
("10","Chair","₹570","8"),
("20","Table","₹1100","2"),
("30","Spoon","₹65","6"),
("40","Fork","₹65","6"),
("50","Knife","₹65","6"),
("60","Plate","₹200","10"),
("70","Pens","₹15","5");

SELECT * FROM Product WHERE Pro_Price=(SELECT MAX(Pro_price) FROM Product);
SELECT * FROM Product WHERE Pro_Price=(SELECT MIN(Pro_price) FROM Product);
SELECT Pro_price FROM Product WHERE Pro_Price=(SELECT MIN(Pro_price) FROM Product);