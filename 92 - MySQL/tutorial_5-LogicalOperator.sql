--Logical Operator

SELECT title,released_year 
FROM books WHERE released_year != 2017 ORDER BY released_year DESC;         --all book not published in 2017

SELECT title FROM books WHERE title NOT LIKE 'the%' ORDER BY title;         --title not start with the

SELECT title,released_year FROM books WHERE released_year <=2000 ORDER BY released_year DESC; 
SELECT title,stock_quantity FROM books WHERE stock_quantity >100 ORDER BY stock_quantity; 

--Note: A==a, sql is case insensitive

SELECT title,released_year FROM books WHERE released_year != 2017 && title NOT LIKE 'the%' 
ORDER BY released_year DESC;        --Combine 2 statement by using && or and 

SELECT title, author_fname, author_lname FROM books WHERE author_fname='Dave' OR author_lname='Harris';

--Between, can be replaced by < and >
SELECT title,released_year FROM books WHERE released_year BETWEEN 2005 AND 2015; 
SELECT title,released_year FROM books WHERE released_year NOT BETWEEN 2005 AND 2015 ORDER BY released_year DESC;

--In and Not In, same as OR statement
Select title,author_fname,author_lname FROM books WHERE author_lname IN ('Carver','Lahiri','Smith');
SELECT title,released_year FROM books WHERE released_year NOT IN (2000,2010,2017) ORDER BY released_year DESC;

--Year that are odd
SELECT title,released_year FROM books WHERE 
released_year>=2000 AND released_year%2!=0 ORDER BY released_year DESC;

--Case statement, WHEN THEN same as if else
SELECT title,released_year,
CASE WHEN released_year>=2000 THEN 'Modern Hit' ELSE '20th Century Lit' END AS Genre 
FROM books;

SELECT title, stock_quantity,
    CASE 
        WHEN stock_quantity <= 50 THEN '*'
        WHEN stock_quantity <= 100 THEN '**'
        ELSE '***'
    END AS STOCK
FROM books; 
    
--Select book which the author name start form C or S
SELECT title, author_lname FROM books WHERE SUBSTR(author_lname,1,1) IN ('C', 'S');

-- Select how many book being published
SELECT author_fname, author_lname,
    CASE 
        WHEN COUNT(*) = 1 THEN '1 book'
        ELSE CONCAT(COUNT(*), ' books')
    END AS Book-Count
FROM books GROUP BY author_lname, author_fname;