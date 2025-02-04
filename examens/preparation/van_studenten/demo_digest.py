import hashlib


def md5_hash(string):
    """
    Generate the MD5 hash of a given string.

    :param string: Input string to be hashed
    :return: MD5 hash of the input string
    """
    # Create MD5 hash object
    md5 = hashlib.md5()

    # Encode the string and generate the hash
    md5.update(string.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return md5.hexdigest()


def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest


# print(md5_digest("words.txt"))
# print(md5_digest("words2.txt"))

print(md5_hash("aa"))
