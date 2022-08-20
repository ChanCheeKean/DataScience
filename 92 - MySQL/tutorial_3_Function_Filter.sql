-- CONCAT, SUBSTR, REPLACE
-- Min, Max, Average, Sum, Count
-- LIKE, DISTINCT
-- ORDER BY, LIMIT, GROUPBY
-- Sub-Query

CREATE DATABASE book_shop;
use book_shop;
show tables;
SELECT database();
 
CREATE TABLE books 
    (
        book_id INT NOT NULL AUTO_INCREMENT,
        title VARCHAR(100),
        author_fname VARCHAR(100),
        author_lname VARCHAR(100),
        released_year INT,
        stock_quantity INT,
        pages INT,
        PRIMARY KEY(book_id)
    );
 
INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343);
 
DESC books;
SELECT * FROM books;

--String Function

--CONCAT, to join string
SELECT CONCAT('Hello','', 'World');             -- Join 2 strings together, type select to show
SELECT author_fname, author_lname FROM books;

SELECT author_fname AS First, author_lname AS Last,
CONCAT(author_fname,' ', author_lname) 
AS Full_name FROM books;                                --Join first and last name with blank in middle

SELECT CONCAT_WS 
('-',author_fname, author_lname,
released_year, stock_quantity, pages) AS Full_Details FROM books;      --Concat with separator 

--SUBSTRING (), to select specific string
SELECT SUBSTRING('HELLO WORLD',3,5);        -- Start from 1st character, 5 letters long
SELECT SUBSTRING('HELLO WORLD',7);          -- Start form 7th character
SELECT SUBSTRING('HELLO WORLD',-3);         --Start from last 3

SELECT title FROM books;
SELECT SUBSTRING(title,1,10) AS short_title FROM books;

SELECT CONCAT(
SUBSTRING(title,1,10),'...') AS short_title
FROM books;  --combine 2 functions

--REPLACE(), to replace words
SELECT REPLACE('HELLO WORLD','HELL','****');
SELECT REPLACE('HELLO WORLD','L','7');
SELECT REPLACE('CHEESE APPLE PIE',' ',' AND ');

SELECT
    SUBSTRING(REPLACE(title, 'e', '3'), 1, 10) AS 'weird string'
FROM books;

-- Reverse ()
SELECT REVERSE('HELLO');
SELECT CONCAT(author_fname,' ', REVERSE(author_fname)) AS R_NAME FROM books;

-- CHAR_LENGTH ()
SELECT CHAR_LENGTH ('HELLO WORLD')
SELECT
  CONCAT(author_lname, ' is ', LEN(author_lname), ' characters long')
FROM books;

--UPPER () LOWER ()
SELECT UPPER(title) FROM books;

--Refining Selection

INSERT INTO books
    (title, author_fname, author_lname, released_year, stock_quantity, pages)
    VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
           ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
           ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);
           
SELECT title from books;

--Show Unique Data
SELECT author_lname FROM books;
SELECT DISTINCT author_lname FROM books;                --no duplicate data
SELECT DISTINCT author_fname, author_lname FROM books;  --only unique full name

--Sorting
SELECT author_lname FROM books ORDER BY author_lname;           --ascending by default
SELECT title FROM books ORDER BY title DESC;                    --go descending
SELECT title,released_year FROM books ORDER BY released_year;   --start from lower number
SELECT title, author_fname, author_lname FROM books ORDER BY 2;  --order by author_lname which is the 2nd one
SELECT title, author_fname, author_lname FROM books ORDER BY 2,1;   --order by 2 then 3

--Limit Selection
SELECT title FROM books LIMIT 3;        --show only 3 titles
SELECT title,released_year FROM books ORDER BY released_year DESC LIMIT 5;   --latest 5 books
SELECT title,released_year FROM books ORDER BY released_year DESC LIMIT 4,2; --start from 5th row 

-- huge data, show everything: SELECT * FROM tbl LIMIT 95,18446744073709551615;

--Searching
SELECT title, author_fname FROM books WHERE author_fname LIKE '%da%';   --Word that have 'da' inside
SELECT title, author_fname FROM books WHERE author_fname LIKE '%da';    --Only end with 'da'
SELECT title, stock_quantity FROM books WHERE stock_quantity LIKE '___';    --Exactly 3 characters long
SELECT title FROM books WHERE (title LIKE '%\%%' OR title LIKE '%\_%');     --to search % or _ in the sentence

--Find the book with longest name
SELECT title FROM books ORDER BY CHAR_LENGTH(title) DESC LIMIT 3;

--Print statement
SELECT DISTINCT CONCAT( 'MY FAVORITE AUTHOR IS ', UPPER(author_fname), ' ',
        UPPER(author_lname), '!') AS yell
FROM books ORDER BY  author_lname;


-- Find the 5 latest book
SELECT 
    title, author_fname
FROM
    books
WHERE
    author_fname = (SELECT DISTINCT
            author_fname
        FROM
            books
        ORDER BY released_year DESC
        LIMIT 3 , 10);
        
--~~~~~~~~~~Aggregate Function~~~~~~~~~~~~

--Count
SELECT COUNT(*) FROM books;                     --how many books in total
SELECT COUNT(author_lname) FROM books;          --some are counted twice,WRONG!
SELECT COUNT(DISTINCT author_lname) FROM books; --Only count non-repeated, but some authors had repeated last name! 
SELECT COUNT(DISTINCT author_fname, author_lname) FROM books;
SELECT COUNT(*) FROM books WHERE title LIKE '%the%';

--Group By, summarise into single row
SELECT title, author_lname FROM books;
SELECT title, author_fname, author_lname FROM books GROUP BY author_fname, author_lname;    --same author group together
SELECT author_fname, author_lname, COUNT(*) FROM books GROUP BY author_fname, author_lname;

SELECT Concat('In ', released_year, ' ', Count(*), ' book(s) released') AS year 
FROM   books GROUP  BY released_year; 

--Max and Min Function 
SELECT MAX(pages) from books;
SELECT * FROM books WHERE pages=(SELECT MIN(pages) FROM books);     --To show the longest book
--The longest book of each author
SELECT CONCAT(author_fname,' ', author_lname) AS author, MAX(pages) FROM books GROUP BY author_fname, author_lname;

--SUM
SELECT SUM(pages) FROM books;
--The total pages of books each author writes
SELECT author_fname, author_lname , SUM(pages) FROM books GROUP BY author_fname, author_lname ORDER BY SUM(pages);

--Average
SELECT AVG(released_year) FROM books;
--Calculate average stock quantity for book in each year
SELECT  released_year, AVG(stock_quantity) FROM books GROUP BY released_year;