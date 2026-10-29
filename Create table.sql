CREATE TABLE Employees(
Employee_id TEXT PRIMARY KEY,
Name TEXT,
Wage INT,
avg_hours REAL,
Position TEXT);

INSERT INTO Employees(Employee_id,Name,Wage,avg_hours,Position)VALUES
("NJ94","Bhdra Tolia","₹1000",8.6,"Chief of Operations"),
("NJ68","Prithviraj Mehta","₹850",8.2,"Supervisor"),
("NJ00","Nivaan Jangla","₹1100",5.9,"CEO"),
("NJ69","Rivaan Thakker","₹790",7.3,"Manager"),
("N6\84","Rishaan Shah","₹300",5.6,"Trainee"),
("NJ64","Yurav Shah","₹890",6.9,"Marketing head");

SELECT * FROM Employees;
SELECT Wage FROM Employees;