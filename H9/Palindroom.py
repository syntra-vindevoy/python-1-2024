def is_palindroom(str):
    return ''.join(reversed(str.lower())) == str.lower()

print(is_palindroom("meetsysteem"))
print(is_palindroom("kachel"))
print(is_palindroom("Level"))