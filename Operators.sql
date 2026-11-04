CREATE TABLE Students(
Roll_no TEXT PRIMARY KEY,
Name TEXT,
Address TEXT,
Phone TEXT,
Age INT);

INSERT INTO Students(Roll_no,Name,Address,Phone,Age)VALUES
("24","Nivaan","Mumbai","9865858325",12),
("42","Yurav","Ahemdabad","9544565861",13),
("16","Naman","Surat","9894895285",11),
("30","Rivaan","Mumbai","9751685295",12),
("28","Prithviraj","Surat","9258462589",12),
("18","Manay","Amritsar","9895262148",13);

SELECT * FROM Students;
SELECT * FROM Students WHERE Address="Mumbai" AND Age=12;
SELECT * FROM Students WHERE Address="Mumbai" AND Name="Nivaan";
SELECT * FROM Students WHERE Name="Nivaan" OR Name="Yurav";
SELECT * FROM Students WHERE Name="Nivaan" OR Age=13;
SELECT * FROM Students WHERE Address="Mumbai" AND Name="Nivaan";
SELECT * FROM Students WHERE Age=12 AND (Name="Nivaan" OR Name="Naman");
SELECT * FROM Students WHERE Name LIKE "N%";
SELECT * FROM Students WHERE Name LIKE "_anay";