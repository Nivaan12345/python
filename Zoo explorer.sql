CREATE TABLE Zoo_Animals(
Animal_id INT PRIMARY KEY ,
Name TEXT NOT NULL,
Species TEXT NOT NULL,
Age INT NOT NULL,
Weight_kg REAL NOT NULL);

INSERT INTO Zoo_Animals(Animal_id,Name,Species,Age,Weight_kg)VALUES
(1,"Lion","Big Cat",5,120.0),
(2,"Tiger","Big Cat",3,220.0),
(3,"Elephant","Pachyderm",12,4500.0),
(4,"Giraffe","Ungulate",7,800.0),
(5,"Penguin","Bird",2,5.0),
(6,"Panda","Bear",6,95.0),
(7,"Cheetha","Big Cat",4,55.0),
(8,"Rhino","Pachyderm",9,2300.0);

SELECT * FROM Zoo_Animals;
SELECT Species FROM Zoo_Animals;
SELECT DISTINCT Species FROM Zoo_Animals;
SELECT COUNT(DISTINCT Species) AS Unique_species FROM Zoo_Animals;
SELECT COUNT(DISTINCT Animal_id) AS Unique_animals FROM Zoo_Animals;
SELECT COUNT(DISTINCT Animal_id) AS Unique_animals FROM Zoo_Animals WHERE Age>5;
SELECT SUM(Weight_kg)AS Total_weight FROM Zoo_Animals;
SELECT AVG(Age)AS Avg_age FROM Zoo_Animals;
SELECT
COUNT(Animal_id) AS animal_count,
COUNT(DISTINCT Species) AS Unique_Species,
SUM(Weight_kg) AS Total_weight,
AVG(Age) AS Avg_age 
FROM Zoo_Animals;
