--Trigger

CREATE DATABASE trigger_db;
USE  trigger_db;

CREATE TABLE users( username VARCHAR(100), age INT);

--Only can insert when 18 and above
--trigger time, trigger evenr, trigger table
--before, insert,users
--run this code before inserting into users table
--NEW.age is the new data that is just inserted
--45000 representing 'unhandled user-defined exception'
--Delimiter is needed when we dont't want to stop at programm at semicolon, but $$ to end and change to semicolon.



DELIMITER $$

CREATE TRIGGER trigger_label
     BEFORE INSERT ON users FOR EACH ROW
     BEGIN
          IF NEW.age < 18
          THEN
              SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Must be an adult!';
          END IF;
     END;
$$ DELIMITER ;

INSERT INTO users(username,age) 
VALUE('ANdy',54);

--Warning when insert age<18
INSERT INTO users(username,age) 
VALUE('KeiKei',14);