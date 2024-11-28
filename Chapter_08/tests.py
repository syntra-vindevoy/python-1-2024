#
# naam = 'Geoffrey'
# letter = naam[-1]
# print(letter)
# print(len(letter))

import os
import subprocess
import requests

# if not os.path.exists('pg345.txt'):
#     subprocess.run(['wget', 'https://www.gutenberg.org/cache/epub/345/pg345.txt'])

if not os.path.exists('pg345.txt'):
    url = 'https://www.gutenberg.org/cache/epub/345/pg345.txt'
    response = requests.get(url)
    with open('pg345.txt', 'wb') as f:
        f.write(response.content)

with open("pg345.txt", "r") as file:    # de manier voor het openen van een file
    words = file.read().split("\n")

print (words)
print(type(words))

