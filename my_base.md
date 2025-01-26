
connection powershell
```powershell
psql -d my_database -U my_user -p 5432
-User
-port
-database
```

```sql
SELECT version();
\q --quit
\l --list databases
\c \connect database_name -- \c ga naar andere database
\e -- open notepad to create multiline query
\h -- help with SQL commands
\? -- help with psql commands
\g -- \go? or terminate with semicolon to execute query
\d <table_name> -- describe
\dt -- describe tables
\dv -- describe views
\r -- query reset
\d+ person_location_phonenumber
```

# TABLES SETUP
```sql
DROP TABLE IF EXISTS cars;
CREATE TABLE cars(
	brand varchar(255),
	model varchar(255),
	year int,
	color VARCHAR
	);
SELECT * FROM cars;
```
+ integer
+ serial
+ bool
+ varchar
+ date
+ time
# COLUMN MODIFICATION
```sql
ALTER TABLE persons;

ADD COLUMN id serial;
ADD COLUMN last_name varchar(100)

RENAME COLUMN test_old TO test
ALTER COLUMN test TYPE INTEGER USING test::integer
DROP COLUMN column_name


```

# CONSTRAINTS
```sql
-- Step 1: Ensure the id column in locations table is unique
ALTER TABLE locations
ADD CONSTRAINT locations_id_unique UNIQUE (id);

-- Step 2: Add the location_id column to persons table
ALTER TABLE persons
ADD COLUMN location_id INTEGER;

-- Step 3: Add the foreign key constraint
ALTER TABLE persons
ADD CONSTRAINT fk_location
FOREIGN KEY (location_id)
REFERENCES locations(id);
```

# ROLLBACK
```sql
BEGIN;
-- Your commands here
ALTER TABLE locations
ADD CONSTRAINT locations_id_unique UNIQUE (id);
-- If you need to rollback
ROLLBACK;
```

# RECORDS
```sql
INSERT INTO cars(brand, model, year)
VALUES ('Fork','Mustang',1964),
VALUES ('BMW','M1',1978)
;
```
+ return
	+ INSERT 0 2
		+ 0 voorlopig niets van aantrekken
		+ 2: 2 row were insterted

```sql
UPDATE persons
SET last_name = 'Vandenholen'
WHERE id = 1
;
```

# VIEWS
```sql
ALTER VIEW viewname_old 
RENAME TO viewname_new
;
```
# QUERIES
## ORDER BY
```sql
SELECT (DISTINCT) * 
FROM cars
ORDER BY customer_name
ORDER BY year DESC
ORDER BY ... ASC

SELECT COUNT(DISTINCT Country) FROM customers;
```

```SQL
SELECT * FROM Customers
WHERE CustomerID>80;
WHERE CustomerID BETWEEN, LIKE, IN
```

```SQL
SELECT _column1_, _column2, ..._  
FROM _table_name_  
ORDER BY _column1, column2, ..._ ASC|DESC;
```
## WHERE
```sql
SELECT *  
FROM Customers  
WHERE Country = 'Spain' 
AND CustomerName LIKE 'G%'
OR CustomerName = 'Spain';
AND CustomerName LIKE 'B%'
```

```sql
SELECT * FROM Customers  
WHERE CustomerName NOT LIKE 'A%';
```

```sql
SELECT * FROM Customers  
WHERE CustomerID NOT BETWEEN 10 AND 60;
```

```sql
SELECT * FROM Customers  
WHERE City NOT IN ('Paris', 'London');
```

## INSERT INTO
```sql
INSERT INTO _table_name_ (_column1_, _column2_, _column3_, ...)  
VALUES (_value1_, _value2_, _value3_, ...);
```

```sql
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)  
VALUES  
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),  
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),  
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
```

## NULL
```sql
SELECT _column_names  
_FROM _table_name_  
WHERE _column_name_ IS (NOT)NULL;
```
## UPDATE
```SQL
UPDATE _table_name_  
SET _column1_ = _value1_, _column2_ = _value2_, ...  
WHERE _condition_;
```

## DELETE
```SQL
DELETE FROM _table_name_ WHERE _condition_;
```

delete all records
```sql
DELETE FROM table_name;
```

## DROP TABLE
```sql 
DROP TABLE table_name;
```

## TOP / LIMIT
```sql
SELECT _column_name(s)_  
FROM _table_name  
_WHERE _condition_  
LIMIT _number_;
```

## WHERE
```sql
SELECT TOP 3 * FROM Customers  
WHERE Country='Germany';
```

## AGGREGATE 
min max count sum avg
```sql
SELECT MIN(Price)  
FROM Products;
WHERE condition
```

## ALIAS
```sql
SELECT MIN(Price) AS SmallestPrice  
FROM Products;
```

```sql
SELECT MIN(Price) AS "Smallest Price"  
FROM Products;
```

## GROUP BY
```SQL
SELECT MIN(Price) AS SmallesPrice, CategoryID -- moet altijd matchen
FROM Products
GROUP BY CategoryID; -- moet altijd op matchen 
```

## COUNT
returns number of rows
```sql
SELECT COUNT(_column_name_)  
FROM _table_name_  
WHERE _condition_;
```

```sql
SELECT COUNT(DISTINCT price) AS [Number of records]
FROM Products;
```

```sql
SELECT COUNT(*) AS [Number of records], CategoryId
FROM Products
GROUP BY CategoryID;
```

## SUM
```sql
SELECT OrderID, SUM(Quantity) AS [Total Quantity]  
FROM OrderDetails  
GROUP BY OrderID;
```
## NESTED QUERIES
```sql
SELECT * FROM Products
WHERE price > (SELECT AVG(price) FROM Products)
```

## AVG GROUP BY
```sql
SELECT AVG(price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;
```

## LIKE WILDCARDS
always in where clause
+ % muliple characters
+ _ one character
+ like zonder wildchar is exacte match
```sql
SELECT _column1, column2, ..._  
FROM _table_name_  
WHERE _columnN_ LIKE _pattern_;
```

### OR WILDCARD
```SQL
SELECT * FROM Customers  
WHERE CustomerName LIKE '[bsp]%';
```

### TO WILDCARD
```SQL
SELECT * FROM Customers  
WHERE CustomerName LIKE '[a-e]%';
```

## IN
```sql
SELECT _column_name(s)_  
FROM _table_name_  
WHERE _column_name_ (NOT)IN (_value1_, _value2_, ...);
```

## IN SELECT
```SQL
SELECT * FROM Customers  
WHERE CustomerID IN (SELECT CustomerID FROM Orders);
```

## BETWEEN
```sql
SELECT _column_name(s)_  
FROM _table_name_  
WHERE _column_name_ (NOT) BETWEEN _value1_ AND _value2;_
```

```sql
SELECT * FROM Products  
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella di Giovanni'  
ORDER BY ProductName;
```

```sql
SELECT * FROM Orders  
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
```

## CONCATENATE COLUMS
```SQL
SELECT product_name || unit AS product  
FROM products;
```

```SQL
SELECT product_name ||' '|| unit AS product  
FROM products;
```

## JOIN
```sql
SELECT product_id, product_name, category_name  
FROM products  
INNER JOIN categories ON products.category_id = categories.category_id;
```

### INNER JOIN
```sql
SELECT testproduct_id, product_name, category_name  
FROM testproducts  
INNER JOIN categories ON testproducts.category_id = categories.category_id;
```
### LEFT JOIN
```sql 
SELECT testproduct_id, product_name, category_name  
FROM testproducts  
LEFT JOIN categories ON testproducts.category_id = categories.category_id;
```
### RIGHT JOIN
```sql
SELECT testproduct_id, product_name, category_name  
FROM testproducts  
RIGHT JOIN categories ON testproducts.category_id = categories.category_id;
```
### FULL JOIN
```sql
SELECT testproduct_id, product_name, category_name  
FROM testproducts  
FULL JOIN categories ON testproducts.category_id = categories.category_id;
```
## CROSS JOIN
```
SELECT testproduct_id, product_name, category_name  
FROM testproducts  
CROSS JOIN categories;
```
## UNION (distinct)
+ same values = same row
+ must have same number of cols
+ cols must have same datatypes
+ cols must be in same order
```sql
SELECT product_id, product_name  
FROM products  
UNION  
SELECT testproduct_id, product_name  
FROM testproducts  
ORDER BY product_id;
```
## UNION ALL
+ same values = different row

## GROUP BY
```SQL
SELECT customers.customer_name, COUNT(orders.order_id)  
FROM orders  
LEFT JOIN customers ON orders.customer_id = customers.customer_id  
GROUP BY customer_name;
```

## HAVING
having is for aggregate functions
```sql
SELECT COUNT(customer_id), country  
FROM customers  
GROUP BY country  
HAVING COUNT(customer_id) > 5;
```

```sql
SELECT order_details.order_id, SUM(products.price)  
FROM order_details  
LEFT JOIN products ON order_details.product_id = products.product_id  
GROUP BY order_id  
HAVING SUM(products.price) > 400.00;
```

```sql
SELECT customers.customer_name, SUM(products.price)  
FROM order_details  
LEFT JOIN products ON order_details.product_id = products.product_id  
LEFT JOIN orders ON order_details.order_id = orders.order_id  
LEFT JOIN customers ON orders.customer_id = customers.customer_id  
GROUP BY customer_name  
HAVING SUM(products.price) > 1000.00;
```

## (NOT) EXISTS
checkt of subquery minstens 1 record heeft
```sql
SELECT customers.customer_name  
FROM customers  
WHERE EXISTS (  
  SELECT order_id  
  FROM orders  
  WHERE customer_id = customers.customer_id  
);
```

## ANY
```SQL
SELECT product_name  
FROM products  
WHERE product_id = ANY (  
  SELECT product_id  
  FROM order_details  
  WHERE quantity > 120  
);
```

## ALL
```SQL
SELECT product_name  
FROM products  
WHERE product_id = ALL (  
  SELECT product_id  
  FROM order_details  
  WHERE quantity > 10  
);
```
## CASE
```sql
SELECT product_name,  
CASE  
  WHEN price < 10 THEN 'Low price product'  
  WHEN price > 50 THEN 'High price product'  
ELSE  
  'Normal product'  -- NULL indien ELSE niet aanwezig
END  
FROM products;
```

```sql
SELECT product_name,  
CASE  
  WHEN price < 10 THEN 'Low price product'  
  WHEN price > 50 THEN 'High price product'  
ELSE  
  'Normal product'  
END AS "price category"  
FROM products;
```

## WITH
```sql
SELECT
	per.id,
	per.firstname,
	per.lastname,
	per.location_id,
	loc.street,
	loc.housenumber,
	loc.postalcode,
	loc.municipality,
	pho.id,
	pho.phonenumber	
FROM persons 
	AS per
LEFT JOIN locations 
	AS loc 
	ON per.location_id = loc.id
LEFT JOIN phonenumbers 
	AS pho 
	ON per.id = pho.person_id
;


WITH
	per as (SELECT * FROM persons),
	loc as (SELECT * FROM locations),
	pho as (SELECT * FROM phonenumbers)
SELECT
	per.id,
	per.firstname,
	per.lastname,
	per.location_id,
	loc.street,
	loc.housenumber,
	loc.postalcode,
	loc.municipality,
	pho.id,
	pho.phonenumber	
FROM per
LEFT JOIN loc 
	ON per.location_id = loc.id
LEFT JOIN pho 
	ON per.id = pho.person_id
;

```