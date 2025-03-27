def guess_number(number:int) -> None:
    if type(number) != int:
        raise TypeError("number must be an integer")

    if number < 0 or number > 10:
        raise ValueError("number must be between 0 and 10")

    print("You guessed it!", number)



def save_customer(customer:dict) -> None:
    try:
        db = get_database_connection()

        db.insert(customer)

        db.close()

    except Exception as err:
        print("Error:", err)

    finally:
        db.close()




def main():
    try:
        guess_number(5)
    except TypeError as err:
        print("TypeError:", err)
    except ValueError as err:
        print("ValueError:", err)
    except Exception as err:
        print("Error:", err)

    try:
        guess_number(11)
    except TypeError as err:
        print("TypeError:", err)
    except ValueError as err:
        print("ValueError:", err)
    except Exception as err:
        print("Error:", err)

    try:
        guess_number("a")
    except TypeError as err:
        print("TypeError:", err)
    except ValueError as err:
        print("ValueError:", err)
    except Exception as err:
        print("Error:", err)

if __name__ == "__main__":
    main()