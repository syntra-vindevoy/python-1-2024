
def facu (x):
    y = 1
    while x > 1:
        y = y * x
        x = x - 1
    print(y)
facu(3)

def hallo ():
    print ("Hallo")
print(type(hallo))

def print_t(text):
    print(text)
print_t("hallokes")

def repeat (word, n):
    print(word * n)
repeat("what ", 10)

for i in range(10):
    print(i)
for i in range(1, 24, 3):
    print(i)
for i in range(50, -1, -5):
    print(i)

def add(x, y):
    a = x + y

a = 10
print(a)

add(2, 3)

print(a)  # geeft steeds de uitkomst van 10 omdat a = x + y uit een functie komt.

assert (add(2, 3) == 5)

if __name__ == "__main__":
    print (__name__)


