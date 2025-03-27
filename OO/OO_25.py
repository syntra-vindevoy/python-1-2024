def get_db_connection():
    pass

class CostumerExeption(Exception):
    def __init__(self, message):
        super().__init__(message)

class TotoException(Exception):
    def __init__(self, err_no,message):
        def __init__(self, message):
            super().__init__(message)


class CustomerEmailExestion(CostumerExeption):
    def __init__(self, message):
        super().__init__(message)

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        if "@" not in email:
            raise CustomerEmailExestion("Email is not valid")

        self.email = email

    def save(self):
        try:
            db = get_db_Connection
            db.save(self)

        except Exception as e:
            raise CostumerExeption(f"Error saving customer: {e}")

        finally:
            db.close()
def main():
    try:
        c = Customer("John", "john@gmail.com")
        c.save()
    except CostumerExeption as e:
        print(f"Error saving customer: {e}")

if __name__ == "__main__":
    main()
