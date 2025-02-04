-- *** SELECT *** 
--SELECT col_name_1 as new_name_1
--     , col_name_2 as new_name_2
--FROM schema.tabel
--WHERE conditie_is_waar
--ORDER BY kolom ASC/DESC

-- Toon alle gegevens uit de tabel person.person
Select *
From adventureworks.person.person;

-- Toon enkel PersonType, Title, FirstName, LastName
Select PersonType, Title, FirstName, LastName
From adventureworks.person.person;

-- Geef de volledig inhoud v/d tabel CountryRegion
Select * From person.CountryRegion;

-- Uit de tabel Product, geef de naam van het product, het productnummer, de kleur,
-- de voorraaddrempel en de aanduiding of het product geproduceerd of aangekocht is.
Select name, productnumber, color, safetystocklevel, makeflag
From Production.Product;


-- *** WHERE ***
-- Toon alle gegevens uit de tabel persoon voor de persoon met id 123
Select *
From person.person
Where BusinessEntityID = 123;

-- Selecteer alle staten van de U.S.
Select *
From person.stateProvince
Where CountryRegioncode = 'US';

-- Selecteer alle staten, behalve die in de U.S.
Select *
From person.stateProvince
Where CountryRegioncode <> 'US';

-- Selecteer alle adressen uit New York & Los Angeles op twee verschillende manieren
Select *
From person.Address
Where city = 'New York' Or city = 'Los Angeles';

Select *
From person.Address
Where city in ('New York', 'Los Angeles');

-- Selecteer alle producten waarvan de voorraaddrempel tussen 10 en 100 ligt 
-- Doe dit op twee verschillende manieren
Select *
From production.product
Where SafetyStockLevel >= 10 and SafetyStockLevel <= 100;

Select *
From production.product
Where SafetyStockLevel between 10 and 100;

-- Selecteer alle producten, sorteer ze op kost in aflopende volgorde
-- en op naam in oplopende volgorde (alfabetisch)
Select *
From production.product
Order By StandardCost Desc, Name Asc;

-- Tel het aantal producten
Select count(*) as aantal_producten
From production.product;

-- Zoek alle staten waarvan de naam begint met "New".
Select *
From person.StateProvince
Where name Like 'New%';

-- Is dit case sensitief ?
Select *
From person.StateProvince
Where name Like 'new%';

-- Hoe kleine en grote letters mee hebben?
Select *
From person.StateProvince
Where lower(name) Like 'new%';

Select *
From person.StateProvince
Where upper(name) Like 'NEW%';


-- *** GROUP BY & HAVING ***
-- *
--FROM schema.tabel
--WHERE conditie_is_waar
--GROUP BY kolom_om_te_groeperen
--HAVING conditie_welke_overhouden
--ORDER BY kolom ASC/DESC

-- Wat is het min- & maximum uurloon dat de winkel ooit uitbetaalde aan een werknemer?
Select min(Rate) as min_rate
     , max(Rate) as max_rate
From HumanResources.EmployeePayHistory;

-- Tel, per achternaam, het aantal personen in de Person tabel. 
-- Sorteer aflopend op aantal en vervolgens alfabetisch op naam?
Select LastName
     , Count(*) as Nb_person
From person.person
Group By LastName
Order By Nb_person Desc, LastName;

-- Tel het aantal producten op basis v/d eerste letter van hun naam. Sorteer alfabetisch.
Select Substring(Name, 1, 1) As first_letter
     , Count(*) as Nb_products
From Production.Product
Group By Substring(Name, 1, 1) -- first_letter
Order By first_letter;

Select lower(Substring(Name,1,1)) As first_letter
     , Count(*) as Nb_products
From Production.Product
Group By lower(Substring(Name,1,1)) -- first_letter
Order By first_letter;

-- Lijst het aantal adressen op per postcode. 
-- Geef enkel de postcodes weer met meer dan 5 adressen. 
-- Sorteer aflopend op basis van aantal adressen.
Select PostalCode
     , Count(AddressLine1) as Nb_address
From Person.Address
Group By PostalCode
Having Count(AddressLine1) > 5
Order By nb_Address DESC;

-- Tel het aantal productbeschrijvingen op basis v/d lengte. 
-- Neem enkel producten mee met een productbeschrijving die langer is dan 10 tekens. 
-- Toon enkel de rijen met meer dan 5 beschrijvingen. 
-- Sorteer oplopend op basis van lengte v/d beschrijving.
Select length(Description) As len_description
     , Count(ProductDescriptionId) as Nb_description
From Production.ProductDescription
Where length(Description) > 10
Group By length(Description)
Having Count(ProductDescriptionId) > 5 -- Nb_description
Order By len_description DESC;

-- Maak een lijst van alle adressen. Het resultaat bevat twee kolommen:
-- addressID en full_address. Deze laatste bevat zowel de straatnaam, postcode en stad.
Select AddressId
     , concat(AddressLine1, ' ', PostalCode, ' ', City) As FullAddress
From Person.Address;

Select AddressId
     , AddressLine1 || ' ' || PostalCode || ' ' || City As FullAddress
From Person.Address;

-- *** JOINS *** --
-- Maak een lijst van producten (zowel productnaam als –nummer), 
-- waar ze in de stock terug te vinden zijn (compartiment en container)
-- en hoeveel er nog in stock zijn. 
Select Product.Name
     , Product.ProductNumber
     , ProductInventory.Shelf
     , ProductInventory.Bin
     , ProductInventory.Quantity
From Production.Product
Join Production.ProductInventory
On ProductInventory.ProductId = Product.ProductId;

Select P.Name
     , P.ProductNumber
     , I.Shelf
     , I.Bin
     , I.Quantity
From Production.Product P
Join Production.ProductInventory I
On I.ProductId = P.ProductId;

Select P.Name
     , P.ProductNumber
     , I.Shelf
     , I.Bin
     , I.Quantity
From Production.Product P
   , Production.ProductInventory I
Where I.ProductId = P.ProductId;

-- Van welke producten is er geen stock meer: geef het productID, -naam en nummer en de hoeveelheid in stock mee. 
Select P.Name
     , P.ProductNumber
     , I.Shelf
     , I.Bin
     , I.Quantity
From Production.Product P
Join Production.ProductInventory I
On I.ProductId = P.ProductId
Where I.Quantity = 0

Select P.Name
     , P.ProductNumber
     , I.Shelf
     , I.Bin
     , I.Quantity
From Production.Product P
Left Join Production.ProductInventory I
On I.ProductId = P.ProductId
Where I.Quantity = 0 Or I.Quantity IS NULL

Select pers.FirstName
     , pers.LastName
     , empl.MaritalStatus
     , empl.Gender
     , empl.birthDate
     , empl.JobTitle
From HumanResources.Employee as empl
Left Join Person.Person as pers
On pers.BusinessEntityId = empl.BusinessEntityId

Select pers.FirstName
     , pers.LastName
     , empl.MaritalStatus
     , empl.Gender
     , empl.birthDate
     , empl.JobTitle
From HumanResources.Employee as empl
Right Join Person.Person as pers
On pers.BusinessEntityId = empl.BusinessEntityId
Where empl.BusinessEntityId IS NULL

Select pers.FirstName
     , pers.LastName
     , empl.MaritalStatus
     , empl.Gender
     , empl.birthDate
     , empl.JobTitle
From HumanResources.Employee as empl
Right Join Person.Person as pers
On pers.BusinessEntityId = empl.BusinessEntityId
Where pers.BusinessEntityId IS NULL

Select pers.FirstName
     , pers.LastName
     , empl.MaritalStatus
     , empl.Gender
     , empl.birthDate
     , empl.JobTitle
	 , dept.Name
From HumanResources.Employee as empl
Left Join Person.Person as pers On pers.BusinessEntityId = empl.BusinessEntityId
Left Join HumanResources.EmployeeDepartmentHistory as hist On hist.BusinessEntityId = empl.BusinessEntityId
Left Join HumanResources.Department as dept On dept.DepartmentId = hist.DepartmentId
Where hist.EndDate IS NULL
  And lower(dept.Name) IN ('finance', 'sales', 'purchasing')

Select cr.CountryRegionCode As Country_Region_Code
     , cr.Name              As Country_Name
	 , sp.StateProvinceCode As State_Province_Code
	 , sp.Name              As Province_Name
	 , Count(distinct C.CustomerId) as Nb_Customers
	 , Count(distinct p.BusinessEntityId) as Nb_Persons
From Sales.Customer as c
LEFT JOIN Person.Person As p On p.BusinessEntityId = c.PersonId
LEFT JOIN Person.BusinessEntity As be On be.BusinessEntityId = c.PersonId
LEFT JOIN Person.BusinessEntityAddress As bea On bea.BusinessEntityId = be.BusinessEntityId
LEFT JOIN Person.Address As a On a.AddressId = bea.AddressId
LEFT JOIN Person.StateProvince As sp On sp.StateProvinceId = a.StateProvinceId
LEFT JOIN Person.CountryRegion As cr On cr.CountryRegionCode = sp.CountryRegionCode
Group By cr.CountryRegionCode
       , cr.Name              -- CountryName
       , sp.StateProvinceCode -- State_Province_Code
	   , sp.Name              -- Province_Name
Order By Country_Name
       , Province_Name

Select Name As Country
     , Case Name When 'United States' Then 'US' Else 'Not US' End As US
From Person.CountryRegion


-- ALL vs ANY
https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-any/
