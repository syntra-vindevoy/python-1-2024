import hashlib


def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

print(md5_digest('words.txt'))
print(md5_digest('words2.txt'))
