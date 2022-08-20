--Generate data from node.js

--Find the earliest user
SELECT * FROM users WHERE  created_at = (SELECT Min(created_at) FROM users); 

-- Most user registration month
SELECT Monthname(created_at) AS month, Count(*) count FROM   users 
GROUP  BY month 
ORDER  BY count DESC; 

-- Number of yahoo user
SELECT Count(*) AS yahoo_users FROM users WHERE  email LIKE '%@yahoo.com'; 

-- Number of users for different providers
SELECT CASE 
         WHEN email LIKE '%@gmail.com' THEN 'gmail' 
         WHEN email LIKE '%@yahoo.com' THEN 'yahoo' 
         WHEN email LIKE '%@hotmail.com' THEN 'hotmail' 
         ELSE 'other' 
       end      AS provider, 
       Count(*) AS total_users 
FROM   users 
GROUP  BY provider 
ORDER  BY total_users DESC; 