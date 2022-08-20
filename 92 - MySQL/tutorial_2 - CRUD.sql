--Create Read Update Delete

--Create Data Base
SHOW databases;				   
CREATE database cat_app;	
USE cat_app;			        
SELECT database  ();		

--Create Table
CREATE TABLE cat
  ( 
     cat_id INT NOT NULL AUTO_INCREMENT,        --cat_id cannot be empty, auto assigned values
     name   VARCHAR(100) DEFAULT 'unknowns',    --set default value, when no value input
     breed  VARCHAR(100), 
     age    INT, 
     PRIMARY KEY (cat_id)                       --cat_id cannot be duplicated
  ); 
 SHOW tables;
 DESC cat;
 
--Create Data
INSERT INTO cat(name, breed, age)               --value () will insert empty value/ become default value
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);

--Select Data
SELECT * from cat;                              --* mean all columns
SELECT name,cat_id from cat;                    --Specify columns to be shown, followed by the sequence of input

SELECT * from cat WHERE age=4;                  --Specify data to be shown.
SELECT cat_id,name from cat WHERE name='Misty';
SELECT cat_id,name,age from cat WHERE cat_id=age;

SELECT cat_id as ID,name as 'Cat Name',age from cat;     -- change the name of variables with aliases

--Update Data
SELECT * from cat;
UPDATE cat SET breed='Short Leg' WHERE breed='Tabby';   --Update the data which fulfill the condition
SELECT * from cat;
UPDATE cat SET age=14 WHERE name='Dumbledore';
--Good  rule of thumb: Select data before updating

--DELETE Data
DELETE from cat WHERE name='egg';
DELETE from cat;            --Delete the whole entries in the table, but the cat table remain

--~~~~~~~~~~~~~~~~~~New Example~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
--New Database
CREATE DATABASE shirt_db;
SHOW DATABASES;
USE shirt_db;
SELECT DATABASE();

--New Table
CREATE TABLE shirt_table
(shirt_id INT NOT NULL AUTO_INCREMENT,      --shirt_id cannot be empty
article VARCHAR(20),
color VARCHAR(20),
shirt_size VARCHAR(5),
last_worn INT,
primary key(shirt_id));                     --shirt_id cannot be duplicated

SHOW TABLES;
DESC shirt_table;

--Create Entries
INSERT INTO shirt_table (article, color,shirt_size,last_worn) VALUES 
('t-shirt', 'white', 'S', 10),
('t-shirt', 'green', 'S', 200),
('polo shirt', 'black', 'M', 10),
('tank top', 'blue', 'S', 50),
('t-shirt', 'pink', 'S', 0),
('polo shirt', 'red', 'M', 5),
('tank top', 'white', 'S', 200),
('tank top', 'blue', 'M', 15);
SELECT * FROM shirt_table;                  --* mean all columns

--Add Entries
INSERT INTO shirt_table (article, color,shirt_size,last_worn) VALUE 
('polo shirt', 'purple', 'M', 50);
SELECT * FROM shirt_table;

--Select Entries
SELECT * FROM shirt_table WHERE shirt_size='M';
SELECT article,color,shirt_size,last_worn FROM shirt_table WHERE shirt_size='s';    --specific which columnand data to be shown

--Update Entries
SELECT * FROM shirt_table WHERE article='Tank top';
UPDATE shirt_table SET shirt_size='L' WHERE article='Tank top';                 
UPDATE shirt_table SET last_worn=0 WHERE last_worn<=55;

SELECT * FROM shirt_table WHERE color='white';
UPDATE shirt_table SET color='off white',shirt_size='XS' WHERE color='white';

SELECT * FROM shirt_table;

--Delete Entries

SELECT * FROM shirt_table WHERE last_worn>=200;
DELETE FROM shirt_table WHERE last_worn>=200;
SELECT * FROM shirt_table;

DELETE FROM shirt_table;
SELECT * FROM shirt_table;
DROP TABLE shirt_table;
SHOW TABLES;

--source Tutorial_2-Practice.sql 