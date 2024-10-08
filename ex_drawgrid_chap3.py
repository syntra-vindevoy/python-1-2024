def print_grid():
    def print_row():
        print('+ - - - - + - - - - +')
    def print_column():
        print('|         +         |')

    print_row()
    for _ in range (5):
        print_column()
    print_row()
    for _ in range (5):
        print_column()
    print_row()

print_grid()