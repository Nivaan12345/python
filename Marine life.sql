CREATE TABLE IF NOT EXISTS Marine_life(
Animal_id INT PRIMARY KEY,
Animal_name TEXT,
Animal_type TEXT,
Animal_habitat TEXT,
Depth_m INT,
Est_Weight_kg REAL);

INSERT INTO Marine_life(Animal_id,Animal_name,Animal_type,Animal_habitat,Depth_m,Est_Weight_kg)VALUES
(101,"Blue Whale","Mammal","Open ocean",30,120000.0),
(102,"Bottlenose Dolphin","Mammal","Open ocean",15,250.0),
(103,"Green Sea Turtle","Reptile","Coral reef",10,160.0),
(104,"Clownfish","Fish","Coral Reef",5,0.3),
(105,"Hammerhead Shark","Fish","Open ocean",70,230.0),
(106,"Giant Octopus","Mollusc","Seabed",40,25.0),
(107,"Manta Ray","Fish","Open ocean",25,1350.0),
(108,"Starfish","Echinoderm","Seabed",20,0.5);

SELECT * FROM Marine_life;
SELECT DISTINCT Animal_type FROM Marine_life;
SELECT COUNT(DISTINCT Animal_type) AS unique_types FROM Marine_life;
SELECT COUNT(Animal_id) AS unique_animals FROM Marine_life;
SELECT COUNT(Animal_id) AS unique_animals_ocean FROM Marine_life WHERE Animal_habitat="Open ocean";
SELECT SUM(Est_Weight_kg) AS Total_Est_Weight_kg FROM Marine_life;
SELECT AVG(Depth_m) AS Avg_Depth_m FROM Marine_life;
SELECT
COUNT(Animal_id) AS Animals,
COUNT(DISTINCT Animal_type) AS Unique_types,
SUM(Est_Weight_kg) AS Total_Est_Weight_kg,
AVG(Depth_m) AS Avg_Depth_m
FROM Marine_life;
UPDATE Marine_life SET Est_Weight_kg=240.0 WHERE Animal_id=105;
UPDATE Marine_life SET Animal_type="Mammal" WHERE Animal_name="Hammerhead Shark";
SELECT * FROM Marine_life;
UPDATE Marine_life SET Animal_type="Fish" WHERE Animal_name="Hammerhead Shark";
UPDATE Marine_life SET Est_Weight_kg=230.0 WHERE Animal_id=105;
SELECT * FROM Marine_life;