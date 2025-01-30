class Student:
    last_name = ""
    first_name = ""
    date_of_birth = ""
    national_id = ""
    nationality = ""
    gender = ""

tom = Student()
tom.last_name = "Thompson"
tom.first_name = "Tom"
tom.date_of_birth = "1999-01-01"
tom.national_id = "123456789"
tom.nationality = "India"
tom.gender = "Male"

jean = Student()
jean.last_name = "Jacques"
jean.first_name = "Jean"
jean.date_of_birth = "1997-05-01"
jean.national_id = "123465789"
jean.nationality = "French"
jean.gender = "Female"

tom.height = 185  #het kan, maar niet doen!!! niets achteraf bijvoegen!!!
print (tom.height)
#print(jean.height)
print (f"Name: {tom.first_name} {tom.last_name}")

