from _02_var.chap02_exe import result

name = "Thomas"

print("m" in name)
print("M" in name)

def has_letter(*, word:str, letter:str) -> bool:
    return letter in word

print(has_letter(word="Thomas", letter="M"))

#Will put name in Upper Case, but will NOT change the content of Name
name.upper()

#If I want it to convert the content of Name
name = name.upper()


#Don't do this
if result == "m" or result == "M":
    pass

#But do this
if result.upper() == "M":
    pass