def avoids(word):
    forbidden = input('What letters you would like to forbid?\n')
    for char in word.lower().replace(' ',''):
        if char in forbidden:
            return False
    return True

print(avoids('hallooooooo dat was haar droom'))