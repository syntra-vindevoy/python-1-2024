


def get_db_connection():
    pass




class CustomerException(Exception):
    def __init__(self, message):
        super().__init__(message)



class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        db = None

        try:
            db = get_db_connection()

            db.save(self)

        except Exception as e:
            raise CustomerException(f"Error saving customer: {e}")

        finally:
            db.close()



def main():
    try:
        c = Customer("Thomas", "<EMAIL>")
        c.save()
    except CustomerException as e:
        print(f"Error saving customer: {e}")


if __name__ == "__main__":
    main()