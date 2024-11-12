SELECT *
from Customers;

SELECT City
FROM Customers;

SELECT Customers.ContactName, City
FROM Customers;

SELECT DISTINCT Country
FROM Customers;

select LastName,BirthDate from Employees;

SELECT COUNT(DISTINCT Country)
FROM Customers;

select distinct City,Country from Customers;

select CompanyName, City  from Customers where Country = 'France';

SELECT *
FROM Products
WHERE Products.UnitPrice BETWEEN 50 AND 60;

SELECT *
FROM Customers
WHERE City LIKE 's%';

SELECT *
FROM Products
ORDER BY UnitPrice DESC;

SELECT *
FROM Products
ORDER BY ProductName;

SELECT *
FROM Products
ORDER BY ProductName DESC;


SELECT Country,CompanyName
FROM Customers where Country is not NULL
ORDER BY Country, CompanyName


SELECT *
FROM Customers
WHERE Country = 'Spain'
  AND CompanyName LIKE 'G%';

SELECT *
FROM Customers
WHERE Country = 'Germany'
  AND City = 'Berlin'
  AND PostalCode > 12000;


SELECT *
FROM Customers
WHERE NOT Country = 'Spain';

SELECT *
FROM Customers
WHERE Country = 'Spain'
  AND (CompanyName LIKE 'G%' OR CompanyName LIKE 'R%');


SELECT *
FROM Customers
WHERE CompanyName NOT LIKE 'A%';

SELECT *
FROM Customers
WHERE CustomerID NOT BETWEEN 10 AND 60;

SELECT *
FROM Customers
WHERE City NOT IN ('Paris', 'London');

SELECT CompanyName, ContactName, Address
FROM Customers
WHERE Address IS NULL;


SELECT *
FROM Customers
limit 3;

SELECT *
FROM Customers
WHERE Country = 'Germany'
LIMIT 3;

SELECT *
FROM Customers
ORDER BY CompanyName DESC
limit 3;

SELECT MAX(Products.UnitPrice)
FROM Products;

SELECT Min(Products.UnitPrice)
FROM Products;

select avg(Products.UnitPrice)
from Products;

SELECT MIN(UnitPrice) AS SmallestPrice
FROM Products;

SELECT MIN(UnitPrice) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;


SELECT AVG(UnitPrice) AS [average price]
FROM Products;

SELECT *
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);

SELECT *
FROM Customers
WHERE city LIKE 'L_nd__';

SELECT *
FROM Customers
WHERE CompanyName LIKE 'a%';

SELECT *
FROM Customers
WHERE Country IN ('Germany', 'France', 'UK');

SELECT *
FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);


