

def bottle_verse(n):
    print(f'{n} bottles of beer on the wall\n'
          f'{n} bottles of beer\n'
          f'Take one down, pass it around\n'
          f'{n - 1} bottles of beer on the wall')

def full_bottle_verse(n):
    for i in range(n, 0, -1):
        bottle_verse(i)
        print()

def main():
    full_bottle_verse(99)

if __name__ == '__main__':
    main()