CREATE TABLE IF NOT EXISTS Books(
Book_id INT PRIMARY KEY,
Title TEXT,
Genre TEXT,
Rating REAL,
Pages INT,
Public_year INT);

INSERT INTO Books(Book_id,Title,Genre,Rating,Pages,Public_year)VALUES
(101,"Keeper of the Lost Cities","Fantasy",8.9,500,2019),
(102,"Septimus Heap-ExtraOrdinary Apprentice","Adventure",7.3,260,2013),
(103,"Artemis Fowl","Futuristic",8.3,420,2010),
(104,"Keys to the Kingdom","Fantasy",5.7,360,2020),
(105,"Five Kingdoms","Adventure",6.8,530,2017),
(106,"Percy Jackson","Mythology",9.4,410,2013),
(107,"Magnus Chase","Mythology",7.9,390,2018),
(108,"H.I.V.E.","Futuristic",4.8,280,2021);

SELECT * FROM Books;
SELECT Title,Rating FROM Books ORDER BY Rating ASC;
SELECT Title,Rating FROM Books ORDER BY Rating DESC;
SELECT Title,Genre,Rating FROM Books ORDER BY Genre ASC,Rating DESC;
SELECT Title,Rating FROM Books ORDER BY Rating DESC LIMIT 3;
SELECT Title,Public_year FROM Books ORDER BY Public_year ASC LIMIT 5;
SELECT Genre,COUNT(*) AS Book_count FROM Books GROUP BY Genre;
SELECT Genre,SUM(Pages) AS Total_pages,AVG(Rating) AS Avg_rating FROM Books GROUP BY Genre;
SELECT Genre,COUNT(*) AS Book_count FROM Books GROUP BY Genre HAVING COUNT(*)>=2;
SELECT Genre,AVG(Rating) AS Avg_rating FROM Books GROUP BY Genre HAVING AVG(Rating)>=8.5;