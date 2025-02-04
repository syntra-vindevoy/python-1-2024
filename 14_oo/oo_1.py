class Student:
    last_name = ""
    first_name = ""
    date_of_birth = ""
    national_id = ""
    nationality = ""
    gender = ""

tom = Student()

tom.first_name = "Tom"
tom.last_name = "Van De Vyver"
tom.gender = "M"
tom.national_id = "123456789"
tom.date_of_birth = "1985-10-14"
tom.nationality = "B"

chiel = Student()
chiel.first_name = "Chiel"
chiel.last_name = "Vansompel"

print(tom.first_name)

print(f"Name: {tom.first_name} {tom.last_name.upper()}")
print(f"Name: {chiel.first_name} {chiel.last_name.upper()}")

tom.height = 185

print(tom.height)
print(chiel.height)
