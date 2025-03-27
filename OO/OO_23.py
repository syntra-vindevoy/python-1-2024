def guess_number(number: int) -> None:
    if type(number) != int:
        raise TypeError("The number must be an integer")

    if number < 0 or number > 10:
        raise ValueError("The number must be between 0 and 10")

    print("The number is", number)

def save_customer(customer: dict) -> None:
    db = None
    try:
        db = getdatabase_connection()
        db.insert(customer)
        db.close()
    except Exception as e:
        print("error:",e)
    finally:
        if db is not None or db == []:
            db.close()
            print("database closed")
def main():
    try:
        guess_number("e")
    except Exception as e:
        print("error:",e)


if __name__ == "__main__":
    main()
