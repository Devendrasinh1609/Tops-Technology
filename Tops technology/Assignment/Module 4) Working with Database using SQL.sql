CREATE DATABASE marketco;
USE marketco;

-- 1) Statement to create the Contact table
CREATE TABLE Company (
    CompanyID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyName VARCHAR(200) NOT NULL,
    Street VARCHAR(200),   
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    Zip VARCHAR(6) NOT NULL
);
INSERT INTO Company (CompanyName, Street, City, State, Zip) VALUES
("Urban Outfitters, Inc.", "500 Lancaster Ave", "Philadelphia", "PA", "19104"),
("Toll Brothers", "250 Gibraltar Rd", "Horsham", "PA", "19044");

-- 2) Statement to create the Employee table

CREATE TABLE Employee (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Salary DECIMAL(10,2),
    HireDate DATE NOT NULL,
    JobTitle VARCHAR(25) NOT NULL,
    Email VARCHAR(45) NOT NULL,
    Phone VARCHAR(12) NOT NULL UNIQUE
);
INSERT INTO Employee (FirstName, LastName, Salary, HireDate, JobTitle, Email, Phone) VALUES
("Lesley", "Bland", 60000, "2015-04-01", "Sales Rep", "lbland@company.com", "9054134252"), 
("Jack", "Lee", 72000, "2013-06-10", "Account Manager", "jlee@company.com", "9054635263");


-- table contact
CREATE TABLE Contact (
    ContactID INT AUTO_INCREMENT PRIMARY KEY,
    CompanyID INT NOT NULL,
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Street VARCHAR(45),
    City VARCHAR(45) NOT NULL,
    State VARCHAR(45) NOT NULL,
    Zip VARCHAR(10)  NOT NULL,
    IsMain BOOLEAN NOT NULL DEFAULT 0,
    Email VARCHAR(45) NOT NULL UNIQUE,
    Phone VARCHAR(12),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

INSERT INTO Contact (CompanyID, FirstName, LastName, Street, City, State, Zip, IsMain, Email, Phone) VALUES
(1, "Dianne", "Connor", "100 Market St", "Philadelphia", "PA", "19106", 1, "dconnor@uo.com", "6354134252"),
(2, "Mark", "Stevens", "300 Lincoln Dr", "Horsham", "PA", "19044", 1, "mstevens@tollbrothers.com", "7990562573");


-- 3) Statement to create the ContactEmployee table 
CREATE TABLE ContactEmployee (
    ContactEmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    ContactID INT NOT NULL,
    EmployeeID INT NOT NULL,
    ContactDate DATE NOT NULL,
    Description VARCHAR(100),
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

INSERT INTO ContactEmployee (ContactID, EmployeeID, ContactDate, Description) VALUES
(1, 2, "2024-03-10", "Initial meeting with Urban Outfitters"),   
(2, 1, "2024-05-12", "Call regarding Toll Brothers project");     

-- 4)  In the Employee table, the statement that changes Lesley Bland’s phone number to 215-555-8800 
SET foreign_key_checks = 0;
SET foreign_key_checks = 1;

SET SQL_SAFE_UPDATES = 0;
UPDATE Employee
SET Phone = '215-555-8800'WHERE FirstName = 'Lesley' AND LastName = 'Bland';
SET SQL_SAFE_UPDATES = 1;

-- 5) In the Company table, the statement that changes the name of “UrbanOutfitters, Inc.” to “Urban Outfitters” . 
UPDATE Company
SET CompanyName = 'Urban Outfitters'
WHERE CompanyName = 'Urban Outfitters, Inc.';

-- 6) In ContactEmployee table, the statement that removes Dianne Connor’s contactevent with Jack Lee (one statement).
SELECT ContactEmployeeID
FROM ContactEmployee
WHERE ContactID = 1 AND EmployeeID = 2;

DELETE FROM ContactEmployee
WHERE ContactEmployeeId = 1; 

SELECT *FROM ContactEmployee;


/* 7) Write the SQL SELECT query that displays the names of the employees that have contacted Toll Brothers (one statement). 
 Run the SQL SELECT query in MySQL Workbench. Copy the results below as well. */
SELECT DISTINCT e.FirstName, e.LastName
FROM Employee e
INNER JOIN ContactEmployee ce ON e.EmployeeID = ce.EmployeeID
INNER JOIN Contact c ON ce.ContactID = c.ContactID
INNER JOIN Company co ON c.CompanyID = co.CompanyID
WHERE co.CompanyName = 'Toll Brothers';

 
 -- 8) What is the significance of “%” and “_” operators in the LIKE statement?
/* 
% (Persentage) -> matches zero or more characters.
_ (Underscore) -> matches exactly one character. 
*/

-- 9) Explain normalization in the context of databases. 
/*
Normalization means arranging the data in a database in a clean and organized way so there are no duplicate 
values and no unnecessary repetition.
*/

-- 10) What does a join in MySQL mean?
-- A JOIN in MySQL is used to combine data from two or more tables based onn a related column (Usally a foreign key)

-- 11) What do you understand abount DDL, DCL, and DML in MySQL?
/* DDL (Data Definitaion Language) : DDL commands are used to create or change the structure of the database and its tables (CREATE, ALTER, DROP)
--> CREATE , ALTER , DROP , TRUNCATE

DCL (Data Control Language) : DCL commands are used to control access to the database.
--> GRANT : Give permission
--> REVOKE : Remove permission

DML (Data Manipulation Language) : DML commands are used to work with the data inside the tables. They help you add, change, remove.
--> INSERT , UPDATE , DELETE
*/

-- 12) What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?
/* 
The JOIN clause is used to combine data from two or more tables based onn a related column (Usally a foreign key)
--> It allows you to see connected information stored in different tables in one result.

--> Types of JOIN
1) Inner JOIN : Returns only the rows that match in both tables.
2) Left JOIN : Returns all rows from the left table and only matching rows from the right tables.
3) Right JOIN : Returns all rows from the right table and only matching rows from the left tables.
4) Full JOIN : Returns all rows from both tables whenther matches or not.
5) Cross JOIN : Returns the cartesian product (Every row from table A combined with every row from table B).
 