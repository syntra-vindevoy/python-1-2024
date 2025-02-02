class Student:
    last_name = ""
    first_name = ""
    date_of_birth = ""
    national_id = ""
    nationality = ""
    gender = ""

tom = Student()
tom.last_name = "Van de Vyver"
tom.first_name = "Tom"
tom.date_of_birth = "1985-10-14"
tom.gender = "M"
tom.national_id = "123456789"
tom.nationality = "B"

chiel = Student()
chiel.first_name = "Chiel"
chiel.last_name = "Vansompel"

print(f"Name: {tom.first_name} {tom.last_name.upper()} ")
print(f"Name: {chiel.first_name} {chiel.last_name.upper()} ")

# stel dat we nu tom.height gebruiken
tom.height = 185
#dit is een extra property die de .. Tom krijgt, Chiel gaat dit niet bijkrijgen.
print(tom.height)
# print(chiel.height)
#dit gaan we niet doen, want onderhoudswerk zou veel te veel zijn.
