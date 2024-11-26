def is_palindrom(str):
    return ''.join(reversed(str)) == str

print(is_palindrom("meetsysteem"))
print(is_palindrom("kachel"))
print(is_palindrom("level"))