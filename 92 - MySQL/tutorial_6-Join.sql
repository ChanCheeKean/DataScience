--One to many relationship, one customer to many orders

CREATE DATABASE customer_db;
USE customer_db;

CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,      --Can choose to insert manually without auto_increment
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders(
    id INT AUTO_INCREMENT PRIMARY KEY,                          --do not confuse with customer_id
    order_date DATE,
    amount DECIMAL(8,2),
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)           --associate to the id in customers(table)
);

INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016/02/10', 99.99, 1),
       ('2017/11/11', 35.50, 1),
       ('2014/12/12', 800.67, 2),
       ('2015/01/03', 12.50, 2),
       ('1999/04/11', 450.25, 5);
       
-- This will be error as 98 is not stored as customer_id
-- INSERT INTO orders (order_date, amount, customer_id) VALUES ('2016/06/06', 33.67, 98);


--To check what did Geroge buy
SELECT * FROM orders WHERE customer_id=
        (
        SELECT id FROM customers WHERE last_name='George'
        );
        
--Implicit Inner Join, Intersection
SELECT * 
FROM   orders, 
       customers 
WHERE  customers.id = orders.customer_id;       --table name.data

SELECT orders.id, 
       first_name, 
       last_name, 
       order_date, 
       amount 
FROM   orders, 
       customers 
WHERE  customers.id = orders.customer_id; 

--Explicit Join, Use Join
SELECT * 
FROM   customers 
       JOIN orders 
         ON customers.id = orders.customer_id;    

--Sequence of customers and orders does not matter, but the print out will be different
SELECT * 
FROM   orders 
       JOIN customers 
         ON customers.id = orders.customer_id ;

--Can work together with group by and order by
SELECT first_name, 
       last_name, 
       Sum(amount) AS total_spending 
FROM   orders 
       JOIN customers 
         ON customers.id = orders.customer_id 
GROUP  BY customers.first_name, 
          customers.last_name 
ORDER  BY total_spending; 


--Left Join, take everything in first table
--Show all users including those who buy nothing
SELECT first_name, 
       last_name, 
       order_date, 
       amount 
FROM   customers 
       LEFT JOIN orders 
              ON customers.id = orders.customer_id; 

--Find people who spend a lot
SELECT first_name, 
       last_name, 
       order_date, 
       IFNULL(Sum(amount),0) as total_spending      --check whether is it null, stay as it is if not
FROM   customers 
       LEFT JOIN orders 
              ON customers.id = orders.customer_id 
GROUP  BY customers.id
ORDER  BY total_spending; 

--Right Join, take everything from other table
SELECT first_name, 
       last_name, 
       order_date, 
       amount 
FROM   customers 
       RIGHT JOIN orders 
              ON customers.id = orders.customer_id; 
              
--System show error when 
--DELETE FROM customers WHERE first_name='Boys'
--The customer id/foreign key in orders(table) dependent on that data
--ON DELETE CASCADE allow deletion
--FOREIGN KEY(customer_id) REFERENCES customers(id) ON DELETE CASCADE



--Practice 
CREATE TABLE students (     id INT auto_increment PRIMARY KEY, 
                            first_name VARCHAR(100) ); 
  
CREATE TABLE papers (title VARCHAR(100),
                     grade INT,
                     student_id INT,
                     FOREIGN KEY(student_id) REFERENCES students(id)
                     ON DELETE CASCADE);
                     
INSERT INTO students (first_name) 
VALUES      ('Caleb'), 
            ('Samantha'), 
            ('Raj'), 
            ('Carlos'), 
            ('Lisa'); 
 
INSERT INTO papers (student_id, title, grade) 
VALUES      (1, 'My First Book Report', 60), 
            (1, 'My Second Book Report', 75), 
            (2, 'Russian Lit Through The Ages', 94), 
            (2, 'De Montaigne and The Art of The Essay', 98), 
            (4, 'Borges and Magical Realism', 89); 
            
SELECT first_name, title, grade 
FROM   students INNER JOIN papers ON student_id = students.id 
ORDER  BY grade DESC; 
            
SELECT first_name, IFNULL(title,'Missing'), IFNULL(grade,0) as average
FROM   students LEFT JOIN papers ON student_id = students.id 
ORDER  BY grade DESC; 

--must have '' after as/end if there is space between
SELECT first_name, 
       IFNULL(AVG(grade),0) AS average,
       CASE 
       WHEN AVG(grade) <=75 THEN 'PASSING'
       ELSE 'FAILING'
       END AS Passing_status
FROM  students LEFT JOIN papers ON papers.student_id = students.id 
GROUP BY students.id
ORDER  BY grade DESC; 


--Many to many relationship, many students to many classes
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100));

--Year is a data type
CREATE TABLE series(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    released_year YEAR(4),
    genre VARCHAR(100));

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rating DECIMAL(2,1),
    series_id INT,
    reviewer_id INT,
    FOREIGN KEY(series_id) REFERENCES series(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id));

INSERT INTO series (title, released_year, genre) VALUES
    ('Archer', 2009, 'Animation'),
    ('Arrested Development', 2003, 'Comedy'),
    ("Bob's Burgers", 2011, 'Animation'),
    ('Bojack Horseman', 2014, 'Animation'),
    ("Breaking Bad", 2008, 'Drama'),
    ('Curb Your Enthusiasm', 2000, 'Comedy'),
    ("Fargo", 2014, 'Drama'),
    ('Freaks and Geeks', 1999, 'Comedy'),
    ('General Hospital', 1963, 'Drama'),
    ('Halt and Catch Fire', 2014, 'Drama'),
    ('Malcolm In The Middle', 2000, 'Comedy'),
    ('Pushing Daisies', 2007, 'Comedy'),
    ('Seinfeld', 1989, 'Comedy'),
    ('Stranger Things', 2016, 'Drama');
 
INSERT INTO reviewers (first_name, last_name) VALUES
    ('Thomas', 'Stoneman'),
    ('Wyatt', 'Skaggs'),
    ('Kimbra', 'Masters'),
    ('Domingo', 'Cortes'),
    ('Colt', 'Steele'),
    ('Pinkie', 'Petit'),
    ('Marlon', 'Crafford');
 
INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
    (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
    (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
    (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
    (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
    (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
    (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
    (7,2,9.1),(7,5,9.7),
    (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
    (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
    (10,5,9.9),
    (13,3,8.0),(13,4,7.2),
    (14,2,8.5),(14,3,8.9),(14,4,8.9);
    
SELECT * FROM reviewers;
SELECT * FROM series;
SELECT * FROM reviews;

SELECT title, Ifnull(Avg(rating), 0) 
FROM   series LEFT JOIN reviews ON series_id = series.id 
GROUP  BY series.id
ORDER BY Avg(rating) DESC; 

--SELECT UNRATE SERIES
SELECT title as unreviewed_series, rating 
FROM   series LEFT JOIN reviews ON series_id = series.id 
WHERE rating IS NULL; 

SELECT genre, ROUND(Avg(rating), 2) AS avg_rating             --MAKE DECIMAL TO 2
FROM   series JOIN reviews ON series_id = series.id 
GROUP  BY series.genre
ORDER BY Avg(rating) DESC; 

SELECT first_name, last_name,                   
       Count(rating) AS count,
       IFNULL(Min(rating),0) AS Min,
       IFNULL(Max(rating),0) AS Max,
       ROUND(IFNULL(Avg(rating), 0),2) AS Average, 
       CASE                                                 
         WHEN Count(rating)>=10 THEN 'POWER USER' 
         WHEN Count(rating)>=1 THEN 'ACTIVE'
         ELSE 'INACTIVE'
       END AS Status 
FROM   reviewers 
       LEFT JOIN reviews 
              ON reviewer_id = reviewers.id 
GROUP  BY first_name, 
          last_name; 

--Join 3 tables together
SELECT reviews.id, title, first_name, last_name, rating 
FROM   reviewers 
       INNER JOIN reviews 
               ON reviewers.id = reviews.reviewer_id 
       INNER JOIN series 
               ON series.id = reviews.series_id; 

SELECT reviews.id, title, first_name, last_name, rating 
FROM   reviewers 
       LEFT JOIN reviews 
               ON reviewers.id = reviews.reviewer_id 
       LEFT JOIN series 
               ON series.id = reviews.series_id; 