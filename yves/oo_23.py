def guess_number(number: int) -> None:
    if type(number) != int:
        raise TypeError("Number should be an integer")

    if number < 0 or number > 10:
        raise ValueError("Number should be between 0 and 10")

    print("You guessed number!", number)



def save_customer(customer: dict) -> None:
    db = None

    try:
        db = get_database_connection()

        db.insert(customer)

    except Exception as err:
        print("Error:", err)

    finally:
        if db is not None or db == []:
            db.close()


def main():
    try:
        guess_number("a")
    except TypeError as err:
        print("You entered something that is not a number between 0 and 10.", err)
    except ValueError as err:
        print("ValueError:", err)
    except Exception as err:
        print("Error:", err)





if __name__ == "__main__":
    main()