def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

content = read_file("words.txt")
print(content)

#zelfde resultaat met pathlib

from pathlib import Path

content = Path("words.txt").read_text()
print(content)

import os

# Pad samenstellen met os
base_path = "/home/user"
filename = "document.txt"
full_path = os.path.join(base_path, filename)

print(full_path)  # Output: /home/user/document.txt

from pathlib import Path

# Pad samenstellen met pathlib
base_path = Path("/home/user")
full_path = base_path / "document.txt"

print(full_path)  # Output: /home/user/document.txt



from pathlib import Path

file_path = Path("words.txt")

if file_path.exists():
    content = file_path.read_text()
    print(content)
else:
    print("Bestand bestaat niet!")

file_path = Path("output.txt")
file_path.write_text("Dit is een voorbeeldtekst.")
print(f"Geschreven naar: {file_path}")

from pathlib import Path

file = Path("subfolder") / "myfile.txt"
print(file.name)       # "myfile.txt"
print(file.suffix)     # ".txt"
print(file.parent)     # "subfolder"
print(file.is_file())  # Controleert of het een bestaand bestand is


from pathlib import Path

base_path = Path("folder")
filename = "file.txt"
full_path = base_path / filename  # Gebruik van "/" ongeacht platform
print(full_path)  # Linux/macOS: "folder/file.txt", Windows: "folder\file.txt"

from pathlib import Path

# Stel je voor dat de huidige werkdirectory is C:/Users/username/Documents/Projects/
current_dir = Path.cwd()

# Om de bovenliggende directory van de huidige directory te krijgen
parent_dir = current_dir.parent
print("Bovenliggende directory:", parent_dir)

# Dit blijft doorgaan voor meerdere niveaus:
grandparent_dir = parent_dir.parent
print("Oudere bovenliggende directory:", grandparent_dir)


from pathlib import Path

current_dir = Path.cwd()  # Dit is een Path object
print(current_dir.parent)  # Werkt omdat current_dir een Path object is

from pathlib import Path

# Stel je hebt een string (een pad als string)
current_dir_str = str(Path.cwd())

# Zet het terug naar een Path object
current_dir = Path(current_dir_str)

# Nu kun je wel de .parent eigenschap gebruiken
print(current_dir.parent)

import hashlib

data = "Dit is een voorbeeld."

# Converteer de string naar bytes met utf-8 encoding
md5_hash = hashlib.md5()
md5_hash.update(data.encode('utf-8'))  # De tekst moet eerst naar bytes worden geconverteerd
hashed_data = md5_hash.hexdigest()

print("MD5 Hash:", hashed_data)


import hashlib

# Aangenomen dat je al met bytes werkt (bijvoorbeeld gegevens uit een bestand)
data = b"Dit is een voorbeeld."  # Dit is al in bytes

md5_hash = hashlib.md5()
md5_hash.update(data)  # Dit werkt omdat data al bytes is
hashed_data = md5_hash.hexdigest()

print("MD5 Hash:", hashed_data)
