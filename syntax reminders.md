```python
# GENERAL
## filepath
### solution 1
	path = Path(__file__).parent.joinpath("lorem.txt").resolve()
	
	def get_wordlist_from_file(file: str):
	    script_dir = os.path.dirname(__file__)
	    file_name = "words.txt"
	    file_path = os.path.join(script_dir, file_name)
    
### solution 2
	import os
	cwd = os.getcwd() 
	# waar zit ik op systeem
	# cwd = current working directory
	
	from pathlib import Path
	current_dir = Path(__file__).parent.absolute() # locatie van draaiend script
	config_dir = current_dir.parent.jointpath("config","settings.ini")
	# OS ONAFHANKELIJK
	
	windows_path = "c:\\test\\folder" # escape char nodig in windows...
	window_path = r"c:\test\folder"
	windows_path = r"c:/test/folder" #can in 
	
	# os.path.pathsep #uitperoberen

### bestaat file
	with open(f"{current_dir}/output.txt","w") as file:
		os.path.abspath 
		os.path.exists 
			#bestaat file?

# TRY EXCEPT
try:
	with open("words.txt","r") as f:
		lines = f.readlines()
except Exception as err:
	print(f"An Error occurred: \n {err}") 
	# exception is algemene foutmelding
	# process finished with exit code 0


try:
	with open("words.txt","r") as f:
		lines = f.readlines()
except FileNotFoundError:
	print(f"Could not find file") 
	# exception is algemene foutmelding
	# process finished with exit code 0

try:
	...
except:
	...
finally:
	print('fout of geen fout, dit wordt altijd uitgevoerd')
	if f:
		if not f.closed:
			f.close()

# lezen van file nog toevoegen
with open(file_path, "r") as f:
   words = f.read().split("\n")
return words

# schrijven naar files
with open("words.txt", "r") as file:
	lines = file.readlines()

with open("words.txt","w") as file:
	
	file.write("marijn\n")
	file.write("yves\n")

	lines = ['yves\n','vindevogel']
	file.writelines()


# strings
[stringmethods_w3_schools](https://www.w3schools.com/python/python_ref_string.asp)

"txt".encode
"txt".endswith # extansies
"txt".expandtabs # aantal spaties bij tab
"txt".isidentifier # geldig als naam van klasse?
"txt".isprintable # asci char 7 kan niet afgedrukt worden


# LISTS
t1 = [1, 2]
t2 = [3, 4]
t1+t2

return [word for word in words]

['spam'] * 4 # repeats items in list
sum(t1)
min(t1)
max(t1)
letters.append('e') # lijst uitbreiden met item
letters.extend(['a','b']) # lijst samenvoegen met andere lijst
verwijderde_item = t.pop(1) # removes item by index
t.remove('b') # removes by value, error if not in list
l.copy() # shallow copy, geen deep copy

# lists and strings
t = s.split('-') # splitten volgens -, default is spatie
s = delimiter.join(t) # joinen volgens delimiter
for word in s.split():
	print(word)

list.sort() # opletten dit geeft geen return!!!

sorted() # sorteert zonder wijziging van de originele lijst
a is b #zelfde object
b = a #aliasing
a == b #zelfde waarde

from copy import copy
list2 = copy(list1)
list2 = list(list1)


# DICTS een keer doorlopen = dict
numbers = dict()
numbers['one'] = 1
numbers = {}
numbers_copy = dict(numbers)
numbers 
len(numbers)

'one' in numbers
1 in numbers.values()

variable = counter.get(letter,0) # waarde opvragen met default

for key in counter:
	value = counter[key]
	print(key, value)
	
for value in counter.values():
	print(value)

dc = {word: len(word) for word in words}

# memo
def fibo(n):
	if n in known
		return known[n]
	res = fibo(n-1) + fibo(n-2)
	known[n] = res
	return 



# TUPLES
t = (1, 2, 3)
t = 1,
t = tuple()
tuple('tup')+('l','e')
sorted(t)

tuple(reversed(t))

# immutable!!!
d = dict()
d[1, 2] = 4
a,b = b,a

email = 'monty@python.org'
username, domain = email.split('@')

for key, value in d.items():
	print(key,'->',value)

# argument packing / unpacking
def mean(*args):
	return sum(args)/len(args)
divmod(t)

def trimmed_mean(*args):
    low, high = min_max(args)
    trimmed = list(args)
    trimmed.remove(low)
    trimmed.remove(high)
    return mean(*trimmed)

def trimmed_mean(*args):
    low, high = min_max(args)
    trimmed = [value for value in args if value != low and value != high]
    return mean(*trimmed)

# zip
zip(scores1, scores2) #resultaat is een iterator!!!
t = list(zip(scores1, scores2))

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

enumerate('abc')


# counter
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

counter = value_counts('bananas')
items = counter.items()

def second_element(t):
	return t(1)

sorted_items = sorted(items, key=second_element)

# invert_dict
def invert_dict(d):
    new = {}
    for key, value in d.items():
        if value not in new:
            new[value] = [key]
        else:
            new[value].append(key)
    return new

# repeat function
def do_twice(f)
	f()
	f()

# timer
import datetime
start = datetime.now()
#code
end = datetime.now()
print(end-start)

#print
print(tekst,end = ".")

# walrus
if (length := len(...)) > 10

# falsy and true-ish values
-1 = true
0 = false
+1 = true

vartype = type(variable)
reversed(t) #reversed object




```