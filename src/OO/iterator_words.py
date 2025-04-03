def words(text):
    for word in text.split():
        yield word


def main():
    for word in words('hello world'):
        print(word)


class Book:
    def __init__(self, title):
        """
        Initialize the Book with a title and an empty list of sentences.
        """
        self.title = title
        self.sentences = []
        self._current_index = 0  # Used for iteration

    def add_sentence(self, sentence):
        """
        Add a sentence to the book.
        :param sentence: A string representing one sentence.
        """
        if isinstance(sentence, str):
            self.sentences.append(sentence)
        else:
            raise ValueError("Sentence must be a string.")

    def get_sentence(self, index):
        """
        Get a sentence by its index.
        :param index: The index of the sentence in the list.
        :return: The requested sentence.
        """
        if 0 <= index < len(self.sentences):
            return self.sentences[index]
        else:
            raise IndexError("Sentence index out of range.")

    def show_all_sentences(self):
        """
        Display all sentences in the book.
        """
        return "\n".join(self.sentences)

    def __iter__(self):
        """
        Make the Book class iterable.
        Resets the current index to the beginning of the sentences list.
        """
        self._current_index = 0
        return self

    def __next__(self):
        """
        Return the next sentence in the list.
        StopIteration is raised when the end of the list is reached.
        """
        if self._current_index < len(self.sentences):
            sentence = self.sentences[self._current_index]
            self._current_index += 1
            return sentence
        else:
            raise StopIteration


# Example usage:
if __name__ == "__main__":
    my_book = Book("My Iterable Book")
    my_book.add_sentence("This is the first sentence.")
    my_book.add_sentence("Here comes another sentence.")
    my_book.add_sentence("Iteration is powerful!")

    print("Title:", my_book.title)
    print("\nAll sentences:")
    for sentence in my_book:
        print(sentence)

    print("\nFetching sentence at index 2:")
    print(my_book.get_sentence(2))

if __name__ == '__main__':
    main()
