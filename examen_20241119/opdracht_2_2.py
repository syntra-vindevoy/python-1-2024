from string import ascii_lowercase, ascii_uppercase

def pass_check(password:str) -> bool:
    """
       Check if the given password is valid based on the following criteria:

       - It must be at least 20 characters long.
       - It must contain at least 1 uppercase letter.
       - It must contain at least 1 lowercase letter.
       - It must contain at least 1 digit.
       - It must contain at least 1 special character.

       Parameters
       ----------
       password : str
           The password string to be checked.

       Returns
       -------
       bool
           True if the password meets all the criteria, False otherwise.

       Examples
       --------
       >>> pass_check("IkBenThomasMeersschaut1%")
       True
       >>> pass_check("ThomasMeersschaut1%")
       False

       Notes
       -----
       This function checks for strong passwords by ensuring they have a minimum of 20 characters
       and include uppercase letters, lowercase letters, digits, and special characters.

       Author
       ------
       Thomas Meersschaut

       Date
       ----
       2024-11-19

       Version
       -------
       1.0.0
       """

    count = len(password)
    #print(count)

    if count >= 20:
        upper = 0
        lower = 0
        digit = 0
        special = 0

        for letter in password:
            if letter in ascii_uppercase:
                upper += 1
            if letter in ascii_lowercase:
                lower += 1
            if letter.isdigit():
                digit += 1
            if not letter.isalnum():
                special += 1

        #print(upper, lower, digit, special)
        return (upper >= 1) and (lower >= 1) and (digit >= 1) and (special >= 1)
    else:
        return False

if __name__ == "__main__":
    assert pass_check("thomasmeersschaut") == False
    assert pass_check("ThomasMeersschaut") == False
    assert pass_check("ThomasMeersschaut1") == False
    assert pass_check("ThomasMeersschaut1%") == False
    assert pass_check("ikbenthomasmeersschaut") == False
    assert pass_check("IkBenThomasMeersschaut") == False
    assert pass_check("IkBenThomasMeersschaut1") == False
    assert pass_check("IkBenThomasMeersschaut1%") == True

