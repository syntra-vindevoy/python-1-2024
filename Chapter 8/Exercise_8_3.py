# Exercise 8.3. A string slice can take a third index that specifies the “step size”; that is,
# the number of spaces between successive characters.
# A step size of 2 means every other character; 3 means every third, etc.
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.

def main():
    word = "pop"
    def is_palindrome():
        return word == word[::-1]

    print(is_palindrome())


if __name__ == "__main__":
    main()