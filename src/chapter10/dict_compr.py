person_info = {
    "1234567890": {  # National number as the key

            "name": "John",
            "age": 30,
            "city": "New York",
            "occupation": "Engineer",
            "address": "123 Main Street",
            "zip_code": "10001"

    },
    "9876543210": {

            "name": "Alice",
            "age": 25,
            "city": "Los Angeles",
            "occupation": "Designer",
            "address": "456 Sunset Blvd",
            "zip_code": "90028"

    },
    "1122334455": {

            "name": "Bob",
            "age": 40,
            "city": "Chicago",
            "occupation": "Manager",
            "address": "789 Lincoln Ave",
            "zip_code": "60614"

    },
    "5566778899": {

            "name": "Emma",
            "age": 28,
            "city": "Dallas",
            "occupation": "Teacher",
            "address": "321 Oak Street",
            "zip_code": "75201"

    },
    "1029384756": {

            "name": "Liam",
            "age": 35,
            "city": "San Francisco",
            "occupation": "Software Developer",
            "address": "333 Mission St",
            "zip_code": "94105"

    },
    "5647382910": {

            "name": "Sophia",
            "age": 30,
            "city": "Seattle",
            "occupation": "Architect",
            "address": "888 Pine Street",
            "zip_code": "98101"

    },
    "2040608090": {

            "name": "Noah",
            "age": 27,
            "city": "Austin",
            "occupation": "Photographer",
            "address": "444 Main Avenue",
            "zip_code": "73301"

    },
    "6677889900": {

            "name": "Isabella",
            "age": 29,
            "city": "San Diego",
            "occupation": "Writer",
            "address": "555 Pacific Blvd",
            "zip_code": "92037"

    },
    "1123581321": {

            "name": "Mason",
            "age": 33,
            "city": "Denver",
            "occupation": "Data Scientist",
            "address": "666 Mountain Road",
            "zip_code": "80202"

    },
    "1919191919": {

            "name": "Olivia",
            "age": 31,
            "city": "Houston",
            "occupation": "Doctor",
            "address": "777 Elm Street",
            "zip_code": "77001"

    },
    "2020202020": {

            "name": "James",
            "age": 45,
            "city": "Phoenix",
            "occupation": "Pilot",
            "address": "999 Sky Lane",
            "zip_code": "85001"

    },
    "5151515151": {
            "name": "Ava",
            "age": 38,
            "city": "Philadelphia",
            "occupation": "Journalist",
            "address": "101 Liberty Street",
            "zip_code": "19107"
    },
    "8080808080": {

            "name": "William",
            "age": 36,
            "city": "San Jose",
            "occupation": "Civil Engineer",
            "address": "121 Silicon Ave",
            "zip_code": "95110"
        }

}

def print_details(description,filter_p):
    print(f"People who {description}")
    for k,v in filter_p.items():
        print_details_person(v)

def print_details_person(person):
    print(f"id :{person['name']}")
    print("-"*(len(person['name'])+4))
    for k,v in person.items():
        print(f"{k}: {v}")
    print("")


if __name__ == "__main__":
    print_details("age >30",{k:p for k,p in person_info.items() if p["age"] > 30})
    print_details("age >30 and zipcode start ith 9",{k:p for k,p in person_info.items() if p["age"] > 30 and p['zip_code'].startswith('9')})
