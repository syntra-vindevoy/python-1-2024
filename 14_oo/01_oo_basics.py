class Student:      #Class name = Capital letter
    last_name = ""
    first_name = ""
    date_of_birth = ""
    national_id = ""
    nationality = ""
    gender = ""

thomas = Student()
print(thomas)

thomas.last_name = "Meersschaut"
thomas.first_name = "Thomas"
thomas.date_of_birth = "1988-02-16"
thomas.national_id = "1234567890"
thomas.nationality = "B"
thomas.gender = "M"
print(f"Name: {thomas.first_name} {thomas.last_name.upper()}")

pol = Student()
pol.last_name = "Pot"
pol.first_name = "Pol"
pol.date_of_birth = "1993-01-06"
pol.national_id = "1234567890"
pol.nationality = "PH"
pol.gender = "F"
print(f"Name: {pol.first_name} {pol.last_name.upper()}")

thomas.height = 170     #It's possible to add a property to the class, without changing the actual class, but it's not considered a good practice
print(thomas.height)





