


from crud import *

    

def main():

    #SETUP

    create_table()
    
    #CRUD
    
    create(5, 'john')
    create(6, 'Jane')
    create(7, 'Joe')

    update(5, 'John Doe')
    
    delete(6)

    #READ
    read_all(Person)
    read_all(Address)
    change_obsolete_status(Person, 7, True)


if __name__ == '__main__':
    main()