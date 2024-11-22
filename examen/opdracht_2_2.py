import string

def check_password(password:str)->bool:
    """
    Verifies the validity of a password based on the following criteria:

    - Minimum 20 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit (0-9)
    - At least 1 special character (punctuation)

    Args:
        password (str): The password to be verified.

    Returns:
        bool: True if the password meets all the criteria, False otherwise.

    Author:
        Marijn Vandenholen

    Date:
        2024-11-19

    Change:
        2024-11-19
        refactored long code to 5 lines, for longer code, review earlier commits.

    """

    return (
        len(password) >= 20 and
        any(i.isupper() for i in password) and
        any(i.islower() for i in password) and
        any(i.isdigit() for i in password) and
        any(i in string.punctuation for i in password)
        #string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ (all special characters that are not digits or letters)
    )



def main():

    assert check_password("ThisIsAVeryLongPassword123!") == True
    assert check_password("Short1!") == False
    assert check_password("ThisIsAVeryLongPassword") == False
    assert check_password("ThisIsAVeryLongPassword123") == False
    assert check_password("thisisaverylongpassword123!") == False


if __name__ == "__main__":
    main()