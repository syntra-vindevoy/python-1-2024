def is_voodoo(str):
    return ''.join(reversed(str[1:] + str[0])) == str

print(is_voodoo("voodoo"))
print(is_voodoo("hello"))
print(is_voodoo("lepe"))
