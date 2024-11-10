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
WHERE Country = 'Spain'
  AND (CompanyName LIKE 'G%' OR CompanyName LIKE 'R%');