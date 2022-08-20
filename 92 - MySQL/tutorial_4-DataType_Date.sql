--Data type and Date

Data Type	            Description

    INT                 for whole numbers
DECIMAL(5,2)            (total number of digits include decimal, digits after decimals), give maximum if numbers exceed   
float                   store larger number with lesser space, less precise, 7 digits
double                  store larger number with lesser space, less precise 15 digits
VARCHAR(20)             for String with defined length
CHAR                    fixed length from 0 to 255, will add spaces after the word if too short,consistent storage spaces
DATE                    date with no time, YYYY-MM-DD
TIME                    time with n date, HH:MM:SS
DATETIME                invlove both date and time, YYYY-MM-DD HH:MM:SS
TIMESTAMPS              Only from 1970 to 2038, for instant time recording, take up less space 

--~~~~~~~~~~~~~Example~~~~~~~~~~~~~~~~~~
CREATE TABLE people (name VARCHAR(100), birthdate DATE, birthtime TIME, birthdt DATETIME);
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Padma', '1983-11-11', '10:07:35', '1983-11-11 10:07:35');

INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Larry', '1943-12-25', '04:10:42', '1943-12-25 04:10:42');

SELECT CURDATE();           --gives current date
SELECT CURTIME();           --gives current time
SELECT NOW ();              --gives current date and time
INSERT INTO people (name, birthdate, birthtime, birthdt)
VALUES('Toast', CURDATE(), CURTIME(), NOW());

--Different format of Date
SELECT * FROM people;
SELECT name, DAY(birthdate),DAYNAME(birthdate), DAYOFWEEK(birthdate), DAYOFYEAR(birthdate),
FROM people;   

--Shortcut
SELECT DATE_FORMAT(birthdt, '%m/%d/%Y') as New FROM people;
SELECT DATE_FORMAT(birthdt, '%m/%d/%Y at %h:%i') as New FROM people;

--Substration and Addition of Date
SELECT name, birthdate, DATEDIFF(NOW(), birthdate) AS Difference FROM people;       --Find difference between now and birthdate
SELECT birthdt, DATE_ADD(birthdt, INTERVAL 1 MONTH) FROM people;                    --Addition with interval
SELECT birthdt, DATE_ADD(birthdt, INTERVAL 10 SECOND) FROM people; 
SELECT birthdt, DATE_ADD(birthdt, INTERVAL 3 QUARTER) FROM people;
 
SELECT birthdt, birthdt + INTERVAL 1 MONTH FROM people;
SELECT birthdt, birthdt - INTERVAL 5 MONTH FROM people;
SELECT birthdt, birthdt + INTERVAL 15 MONTH + INTERVAL 10 HOUR FROM people;         --Without function

--New Datatype,timestamps

CREATE TABLE comment(
contents VARCHAR(100), created_at TIMESTAMP DEFAULT NOW());  --timestamps can be replaced by datetime
INSERT INTO comment (contents) VALUES ('This Suck!');
SELECT * from comment; 

CREATE TABLE comments2 (content VARCHAR(100),
changed_at TIMESTAMP DEFAULT NOW() ON UPDATE NOW());    --It will record the date if there is any changes to the contents

INSERT INTO comments2 (content) VALUES('dasdasdasd'),('hahasd'),('lololololo');
SELECT * FROM comments2;

UPDATE comments2 SET content='THIS IS NOT GIBBERISH' WHERE content='hahasd';
SELECT * FROM comments2 ORDER BY changed_at;                --shows the update date


-- LOGICAL OPERATOR - Between the date, cast() is to make sure the input as datetime
SELECT name, birthdt FROM people 
WHERE birthdt BETWEEN CAST('1980-01-01' AS DATETIME) AND CAST('2000-01-01' AS DATETIME);
