import string

plain_text = input("What string you want to encrypt?" )
shift = int(input("Which key? "))
shift %= 26

alphabet_lower = string.ascii_lowercase
shifted_lower = alphabet_lower[shift:] + alphabet_lower[:shift]

alphabet_upper = string.ascii_uppercase
shifted_upper = alphabet_upper[shift:] + alphabet_upper[:shift]
table = str.maketrans(alphabet_lower + alphabet_upper, shifted_lower + shifted_upper)

encrypted = plain_text.translate(table)

print(encrypted)
