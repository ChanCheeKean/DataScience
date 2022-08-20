--Introduction
--SQL Tutorial 1 

--Set Up
* Do it in cloud 9.
* mysql-ctl start
* mysql-ctl cli
* mysql-ctl stop

--Basic Command
show databases;				    show all query
create database <db_name>;		create a query 
drop database <db_name>;		delete a query 
use <db_name>;			        set directory in this query
select database  ();			check currently used database


--Data Type
Data Type	    Description
INT	            for whole number
VarChar	        for String
--wrong datatype will set the data to 0

--Create Tables
create table <table_name>	        create new table
show Tables; 	                    show what’s inside database
Show Columns from <table_name>;	    show the content
DESC <table_name>;	                same as show columns
drop table <table_name>;	        delete table
CREATE DATABASE <data_name>;
use <data_name>;

--Example
create table unique_cat 
(name varchar(100) not null, 
age int, primary key (name));
insert into unique_cat (name,age)
Value('bibi',2);

/* insert into unique_cat (name, age)		--error, as name cannot be duplicated
Value('bibi’,3); */


