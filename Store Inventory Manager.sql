CREATE TABLE IF NOT EXISTS Product(
Pro_id TEXT PRIMARY KEY,
Pro_name TEXT,
Pro_price INT,
Pro_com TEXT);

INSERT INTO Product(Pro_id,Pro_name,Pro_price,Pro_com)VALUES
("101","Mother Board",3200,"Techpro"),
("102","Key Board",450,"Keymax"),
("103","Zip Drive",250,"Datafix"),
("104","Speaker",550,"Soundco"),
("105","Monitor",5000,"Viewtech"),
("106","DVD Drive",900,"Datafix"),
("107","CD Drive",800,"Datafix"),
("108","Printer",2600,"Printplus"),
("109","Refil Cartridge",350,"Printplus"),
("110","Mouse",250,"Keymax");

SELECT * FROM Product;
SELECT * FROM Product WHERE Pro_price<1000 AND Pro_com="Datafix";
SELECT * FROM Product WHERE Pro_price>800 OR Pro_com="Printplus";
SELECT * FROM Product WHERE Pro_price<1000 AND Pro_com="Datafix";
SELECT * FROM Product WHERE Pro_com LIKE "%i%";
SELECT * FROM Product WHERE Pro_price=(SELECT MAX(Pro_price) FROM Product);
SELECT * FROM Product WHERE Pro_price=(SELECT MIN(Pro_price) FROM Product);
UPDATE Product SET Pro_price=400 WHERE Pro_id="109";
DELETE FROM Product WHERE Pro_price<300;
SELECT * FROM Product;