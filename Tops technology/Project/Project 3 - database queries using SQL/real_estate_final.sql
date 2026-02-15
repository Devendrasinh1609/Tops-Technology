CREATE DATABASE Real_EstateDB;
USE Real_EstateDB;

CREATE TABLE cities (
    city_id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(50),
    state VARCHAR(50)
);

INSERT INTO cities (city_name, state) VALUES
("Ahmedabad", "Gujarat"),
("Mumbai", "Maharashtra"),
("Delhi", "Delhi"),
("Pune", "Maharashtra"),
("Surat", "Gujarat"),
("Jaipur", "Rajasthan"),
("Bangalore", "Karnataka"),
("Chennai", "Tamil Nadu"),
("Hyderabad", "Telangana"),
("Kochi", "Kerala");

select *from cities;
CREATE TABLE property_types (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50)
);

INSERT INTO property_types (type_name) VALUES
("Apartment"),
("Villa"),
("Plot"),
("Commercial"),
("Office Space"),
("Studio"),
("Farmhouse"),
("Bungalow"),
("Penthouse"),
("Duplex");

select *from property_types;
CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

INSERT INTO agents (name, phone, email, city_id) VALUES
("Ravi Patel", "9876543210", "ravi.patel@email.com", 1),
("Priya Sharma", "9988776655", "priya.sharma@email.com", 2),
("Amit Mehta", "9123456789", "amit.mehta@email.com", 3),
("Neha Singh", "9765432189", "neha.singh@email.com", 4),
("Rahul Desai", "9845123765", "rahul.desai@email.com", 5),
("Kavita Joshi", "8899776655", "kavita.joshi@email.com", 6),
("Vikram Shah", "9001122334", "vikram.shah@email.com", 7),
("Sonal Gupta", "9887766554", "sonal.gupta@email.com", 8),
("Arjun Reddy", "9445566778", "arjun.reddy@email.com", 9),
("Meera Nair", "9556677889", "meera.nair@email.com", 10);

select *from agents;

CREATE TABLE properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id INT,
    type_id INT,
    title VARCHAR(100),
    location VARCHAR(100),
    price DECIMAL(12,2),
    status VARCHAR(20),
    bedrooms INT,
    bathrooms INT,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id),
    FOREIGN KEY (type_id) REFERENCES property_types(type_id)
);

INSERT INTO properties (agent_id, type_id, title, location, price, status, bedrooms, bathrooms) VALUES
(1, 1, "2BHK Apartment in Navrangpura", "Ahmedabad", 4500000, "Available", 2, 2),
(2, 2, "Luxury Villa in Bandra", "Mumbai", 15000000, "Sold", 4, 3),
(3, 1, "3BHK Flat in Dwarka", "Delhi", 7200000, "Available", 3, 2),
(4, 1, "2BHK Flat in Kothrud", "Pune", 5600000, "Rented", 2, 2),
(5, 3, "Plot near Dumas Beach", "Surat", 3200000, "Available", 0, 0),
(6, 2, "4BHK Villa in Mansarovar", "Jaipur", 9500000, "Available", 4, 3),
(7, 6, "Studio Apartment in Whitefield", "Bangalore", 3500000, "Sold", 1, 1),
(8, 4, "Office Space in T Nagar", "Chennai", 8700000, "Available", 0, 1),
(9, 1, "3BHK Apartment in Gachibowli", "Hyderabad", 7800000, "Available", 3, 2),
(10, 1, "2BHK Flat in Kakkanad", "Kochi", 5400000, "Sold", 2, 2);

select *from properties;

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    email VARCHAR(100),
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(city_id)
);

INSERT INTO clients (name, phone, email, city_id) VALUES
("Manish Kumar", "9876501234", "manish.kumar@email.com", 3),
("Sneha Patel", "9887123456", "sneha.patel@email.com", 2),
("Rohit Sharma", "9765412345", "rohit.sharma@email.com", 1),
("Divya Mehta", "9898012345", "divya.mehta@email.com", 5),
("Karan Singh", "9845012345", "karan.singh@email.com", 4),
("Pooja Nair", "9777712345", "pooja.nair@email.com", 8),
("Ajay Joshi", "9000012345", "ajay.joshi@email.com", 6),
("Isha Reddy", "9444412345", "isha.reddy@email.com", 9),
("Aditi Shah", "9555512345", "aditi.shah@email.com", 7),
("Neelam Rao", "9666612345", "neelam.rao@email.com", 10);

select *from  clients;

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    client_id INT,
    agent_id INT,
    sale_price DECIMAL(12,2),
    transaction_date DATE,
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

INSERT INTO transactions (property_id, client_id, agent_id, sale_price, transaction_date) VALUES
(2, 2, 2, 15000000, "2024-06-12"),
(4, 5, 4, 5600000, "2024-07-25"),
(7, 9, 7, 3500000, "2024-08-10"),
(10, 10, 10, 5400000, "2024-09-14"),
(5, 4, 5, 3200000, "2024-10-01"),
(6, 7, 6, 9500000, "2024-11-03"),
(3, 1, 3, 7200000, "2024-11-11"),
(9, 8, 9, 7800000, "2024-12-15"),
(1, 3, 1, 4500000, "2025-01-05"),
(8, 6, 8, 8700000, "2025-02-22");

select *from transactions;

SELECT * FROM cities;
SELECT * FROM property_types;
SELECT * FROM agents;
SELECT * FROM properties;
SELECT * FROM clients;
SELECT * FROM transactions;

-- Arithmetic operations
-- Add 1,00,000 to each property
SELECT property_id , price , price + 100000 AS increased_price FROM properties;

-- 10% discount
SELECT property_id, price, price - (price * 0.10) AS discounted_price
FROM properties;

-- WHERE conditions
SELECT * FROM properties
WHERE price < 5000000;

SELECT * FROM properties
WHERE bedrooms > 2;

-- Logical Operators 
update properties
SET title = "3BHK in Science City" 
WHERE property_id = 3;

SELECT * FROM properties
WHERE location = "Ahmedabad" AND price > 600000;

SELECT * FROM properties
WHERE price < 500000 OR (status='Sold' AND bedrooms >= 2);

-- GROUP BY 
SELECT status, COUNT(*) AS total_properties
FROM properties
GROUP BY status;

-- Having cluse
select *from properties;
SELECT type_id, MAX(price) AS max_price
FROM properties
GROUP BY type_id
HAVING MAX(price) > 10000000;

SELECT type_id, ROUND(AVG(price)) AS avg_price
FROM properties
GROUP BY type_id
HAVING avg_price BETWEEN 3000000 AND 7000000;

-- Order By and LIMIT
SELECT property_id, title, price
FROM properties
ORDER BY price DESC
LIMIT 5;

-- 3rd most expensive property
SELECT property_id, title, price
FROM properties
ORDER BY price DESC
LIMIT 1 OFFSET 2;

-- DISTINCT
SELECT DISTINCT type_id , bedrooms
FROM properties
ORDER BY type_id , bedrooms;

-- IN Operator
SELECT *FROM agents
WHERE city_id IN (1,3,4);

-- Like operator
select *from clients;
SELECT *FROM clients
WHERE name like "A%";

SELECT * FROM properties
WHERE title LIKE '%BHK%';

SELECT * FROM agents
WHERE email LIKE '%gmail.com';

SELECT *FROM agents
WHERE phone LIKE "%10%";

-- JOIN Queries
-- Agent name with title and property id
SELECT p.property_id , p.title , a.name AS agent_name
FROM properties p
JOIN agents a ON p.agent_id = a.agent_id;

select a.agent_id , a.name AS agent_name , c.city_name , c.state
FROM agents a
INNER JOIN cities c ON a.city_id = c.city_id;

SELECT a.agent_id, a.name AS agent_name, p.property_id, p.title
FROM agents a
LEFT JOIN properties p ON a.agent_id = p.agent_id;

-- Q1 List all transactions along with thier corresponding client names
 SELECT 
    t.transaction_id,
    c.name AS client_name,
    t.sale_price,
    t.transaction_date
FROM transactions t
INNER JOIN clients c 
ON t.client_id = c.client_id;

-- Q2 Show transation details with property titles from the properties table
SELECT t.transaction_id , p.title ,p.status, t.sale_price , t.transaction_date
FROM transactions t
INNER JOIN  properties p
ON t.property_id = p.property_id
WHERE p.status != "Available";

-- Q3 Find all clients who have made at least one purchase (transaction)
SELECT DISTINCT c.client_id , c.name AS client_name , c.phone
FROM clients c
INNER JOIN transactions t
ON c.client_id = t.client_id
INNER JOIN properties p
ON t.property_id = p.property_id
WHERE p.status = "Sold"; 

-- Q4 Display transaction id , clients name and sale price for sold transactions
SELECT t.transaction_id , c.name AS client_name , t.sale_price
FROM transactions t
INNER JOIN clients c ON t.client_id = c.client_id
INNER JOIN properties p ON t.property_id = p.property_id
WHERE p.status = "Sold";

select *from transactions;

-- Q5 List all clients and thier transactions where property status is "Sold"
SELECT c.client_id, c.name AS client_name, t.transaction_id, t.sale_price
FROM clients c
INNER JOIN transactions t ON c.client_id = t.client_id
INNER JOIN properties p ON t.property_id = p.property_id
WHERE p.status = "Sold";

-- Q6 Show all properties with thier agent
SELECT p.property_id , p.title , a.name AS agent_name
FROM properties p
INNER JOIN agents a ON p.agent_id = a.agent_id;

-- Left Join 
-- Q1 List all clients and thier transactions
SELECT c.client_id, c.name AS client_name, t.transaction_id, t.sale_price
FROM clients c
LEFT JOIN transactions t ON c.client_id = t.client_id;

-- Q2 Show all properties and thier transactions (Only sold)
SELECT p.property_id, p.title, p.status, t.transaction_id, t.sale_price
FROM properties p
LEFT JOIN transactions t 
    ON p.property_id = t.property_id 
    AND p.status = "Sold";

-- Q3 Show all agents and their properties 
SELECT a.agent_id, a.name AS agent_name, p.property_id, p.title AS property_title
FROM agents a
LEFT JOIN properties p 
    ON a.agent_id = p.agent_id;
    
-- Q4  List all cities and their clients 
SELECT ci.city_name, a.name AS agent_name
FROM cities ci
LEFT JOIN agents a ON ci.city_id = a.city_id;

Select *from agents;

-- Store procedure
DELIMITER //
CREATE PROCEDURE show_properties()
BEGIN
	SELECT property_id , title , location , price , status
    FROM properties;
END //
DELIMITER ;

CALL show_properties;

-- INSERT value 
DELIMITER //
CREATE PROCEDURE add_property(
    IN p_agent_id INT,
    IN p_type_id INT,
    IN p_title VARCHAR(100),
    IN p_location VARCHAR(100),
    IN p_price DECIMAL(12,2),
    IN p_status VARCHAR(20),
    IN p_bedrooms INT,
    IN p_bathrooms INT
)
BEGIN
    INSERT INTO properties (agent_id, type_id, title, location, price, status, bedrooms, bathrooms)
    VALUES (p_agent_id, p_type_id, p_title, p_location, p_price, p_status, p_bedrooms, p_bathrooms);
END //
DELIMITER ;

CALL add_property(1,1,"3BHK Flat in SG Highway","Ahmedabad",  6200000 , "Available" , 3 , 2);
CALL show_properties;

-- Trigger --> A trigger is a special SQL code that runs automatically when something happens in a table.
DELIMITER //
CREATE TRIGGER prevent_negative_price
BEFORE INSERT ON properties
FOR EACH ROW
BEGIN
    IF NEW.price < 0 THEN
        SIGNAL SQLSTATE "45000"
        SET MESSAGE_TEXT = "Error: Price cannot be negative.";
    END IF;
END //
DELIMITER ;

INSERT INTO properties (agent_id, type_id, title, location, price, status, bedrooms, bathrooms) VALUES
(3, 3, "3BHK Flat in Ranip", "Ahmedabad", -4500, "Available", 2, 2);
SELECT * from properties;
delete from properties where property_id = 12;

-- View statement que
-- question "Create a view named 'property_list' that displays the property title, price, status, and the assigned agent's name."
CREATE VIEW property_list AS
SELECT p.title, p.price, p.status, a.name AS agent_name
FROM properties p
JOIN agents a ON p.agent_id = a.agent_id;

SELECT * FROM property_list;




