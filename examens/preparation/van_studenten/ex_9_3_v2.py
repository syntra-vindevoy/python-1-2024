import itertools
import string

# 96425
# qjxzw
# print(words_without(list("qjxzw")))


with open("words.txt", "r") as input_file:
    all_words = input_file.readlines()


def avoids(forbidden, word):
    for letter in forbidden:
        if letter in word:
            return False

    return True


def words_without(forbidden):
    count = 0

    for word in all_words:
        if avoids(forbidden, word):
            count += 1

    return count


def run():
    letter_count = {letter: 0 for letter in string.ascii_lowercase}
    words = [set(word.strip()) for word in all_words]

    for word in all_words:
        for letter in set(word.strip()):
            letter_count[letter] += 1

    print(letter_count)

    letter_count = sorted(letter_count.items(), key=lambda x: x[1])
    print(letter_count)

    start_count = letter_count[:5]
    print(start_count)
    start_count = sum([s[1] for s in start_count])
    print(start_count)

    useless_letters = [letter for letter in letter_count if letter[1] > start_count]
    to_check_letters = [letter for letter in letter_count if letter[1] < start_count]
    print(useless_letters)
    print(to_check_letters)

    to_check_letters = [letter[0] for letter in to_check_letters]
    print(to_check_letters)

    all_combos = list(itertools.combinations(to_check_letters, 5))
    print(len(all_combos))

    best = []
    best_count = -1
    done = 0
    todo = len(all_combos)

    print(all_words)
    for combo in all_combos:
        count = 0
        done += 1

        for word in all_words:
            if avoids(forbidden=combo, word=word.strip()):
                count += 1

        print(f"Tested {''.join(combo)}: {count} times (best remains {''.join(best)}: {best_count}) - {done}/{todo}")

        if count > best_count:
            best_count = count
            best = combo

    print(f"Best combination: {best}: {best_count} times")


if __name__ == "__main__":
    run()
