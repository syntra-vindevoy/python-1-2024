# exercise 5.1 from thinkpython V2 - made by AI

import time
from datetime import datetime

from numpy.f2py.crackfortran import beginpattern

# Huidige tijd verkrijgen
current_time = time.time()

# Tijd van de dag verkrijgen in uren, minuten en seconden
time_of_day = time.strftime("%H:%M:%S", time.localtime(current_time))

# Huidige datum en tijd
now = datetime.now()

# Aantal dagen sinds de epoch (1 januari 1970)
days_since_epoch = (now - datetime(1970, 1, 1)).days

print(f"Tijd van de dag: {time_of_day}")
print(f"Aantal dagen sinds de epoch: {days_since_epoch}")

#Exercise 5.2 from thinkpython V2 - made by GC & AI

def check_fermat (a, b, c, n):
    if n > 2 and ((a ** n) + (b ** n)) == (c ** n):
        return "holy smokes fermat was wrong!"
    else:
        return "no, that doesn't work"

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Gelieve een geldig geheel getal in te voeren.")
def prompt_fermat():
    try:
        a = get_integer_input("Voer de waarde in voor a: ")
        b = get_integer_input("Voer de waarde in voor b: ")
        c = get_integer_input("Voer de waarde in voor c: ")
        n = get_integer_input("Voer de waarde in voor n: ")
        check_fermat(a, b, c, n)
        print(check_fermat(a, b, c, n))
    except ValueError:
        print("Gelieve geldige gehele getallen in te voeren.")


# Call the function to prompt the user and check Fermat's theorem
prompt_fermat()
