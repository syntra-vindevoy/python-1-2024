#https://www.youtube.com/watch?v=QLTdOEn79Rc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2

mylst:[]= [1, 2, 3, 4, "test", True]


print(mylst)
print(mylst[-1])

for i in mylst:
    print(i, end=" ")
    print(type(i))


if "test" in mylst:
    print("test is in mylst")


priths = [1991, 1993, 1997, 2001, 2003]
print(priths[0:3])

print(len(priths))

priths.append(2009)
print(priths)

priths.remove(2001)
print(priths)

priths.insert(1, 2005)
print(priths)

priths.sort()
print(priths)

item = priths.pop()
print(item)
print(priths)

priths.reverse()
print(priths)

priths.extend([2011, 2013, 2017])
print(priths)

priths.remove(2013)
print(priths)

priths.clear()
print(priths)

newlst = [1, 10,2,9 ,0,3, 4, 5]
newlst2 = sorted(newlst)
print(newlst2)

newlst3 = sorted(newlst, reverse=True)
print(newlst3)

newlst4 = newlst + ([0] * 10) + ["hello"]
print(newlst4)

l = newlst4[3:5]
print(l)

rest = newlst4[::-1]
print(rest)

print(newlst4.index(10))

lst_cpy = newlst4.copy()

print(lst_cpy)

lst_cpy.remove(10)
print(lst_cpy)
print(newlst4)


comp = [t for t in lst_cpy if type(t) is str ]
print(comp)



import re


def split_on_upper_and_space_re(s):
    # Use a regex to split on uppercase letters or spaces
    return re.findall(r'[A-Z][a-z0-9]*|[a-z0-9]+', s)

def split_on_upper_and_space(s):
    words = []
    current_word = ""

    for char in s:
        # Check for uppercase letter (except for the first character in the word)
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char
        # Check for spaces
        elif char.isspace() and current_word:
            words.append(current_word)
            current_word = ""
        else:
            current_word += char

    # Append the final collected word (if any)
    if current_word:
        words.append(current_word)

    return words


def split_on_upper_and_space_c(s):
    # Step through indexes of the string to identify start of new words
    words = [
        s[start:end]
        for start, end in zip(
            [0] + [i for i in range(1, len(s)) if s[i].isupper() or s[i].isspace()],
            [i for i in range(1, len(s)) if s[i].isupper() or s[i].isspace()] + [len(s)]
        )
    ]
    # Filter out empty words and strip spaces
    return [word for word in words if word.strip()]

# Example string
str_exampl = "hello WorldFromWorld123OfHorror"

# Split the string
result = split_on_upper_and_space(str_exampl)
print(result)












