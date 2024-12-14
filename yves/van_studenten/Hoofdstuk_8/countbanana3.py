def count(w, l):
    return len(w) - len(w.replace(l,''))

print(count('banana', 'a'))