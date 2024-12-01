import random

with open("words.txt", "r") as f:
    words = f.read().split("\n")

def nested_sum(numbers):
    sums = 0
    for n in numbers: sums += sum (n)
    return sums

#print (nested_sum([[1, 2], [3], [4, 5, 6]]))

def cum_sum(numbers):
    t = list(numbers[:1])
    for i in range(1, len(numbers)):
        t.append(t[i - 1] + numbers[i])
    return t

#print (cum_sum ([1,3,4,5]))


def middle (numbers):
    t = numbers[1:-1]
    return t

#print (middle ([1,2,3,4,5,6]))

def chop(numbers):
    numbers.remove(numbers[0])
    numbers.remove(numbers[-1])
    return None
#print (chop ([1,2,3,4,5]))


def is_sorted(numbers):
    return sorted(numbers) == numbers

#print (is_sorted([1,3,4,5]))
#print (is_sorted(["a", "d", "c"]))

def has_duplicates(n):
    test = False
    for i in range (len(n)):
        if n[i] in n[:i:]: return True
    return test
#print (has_duplicates([1, 2, 3, "g", 4, 5, "a", "g" ]))


def in_bisect (n, words):
    words.sort()
    lenght = len(words)
    if lenght == 1 and n != words[0]: return False
    middle = words[lenght//2]
    if middle == n: return True
    elif n < middle:
        lenght += 1 #verlies bij afronding opvangen
        return in_bisect(n, words[:lenght//2])
    elif n > middle:
        return in_bisect(n, words[lenght//2:])

#print(in_bisect("insect" ,words))

def reverse_pair():
    rev_pair =[]
    for word in words:
        if word[::-1] in words:
            rev_pair.append([word,word[::-1]])
    return rev_pair
#print (reverse_pair())

def birthday_generator (students):
    return [random.randint(1,366) for _ in range(students)]

def birthday_duplicates (students):
    return has_duplicates(birthday_generator (students))

def test_birthday_paradox(tries, number_of_students):
    duplicates = []
    for i in range (tries):
        if birthday_duplicates(number_of_students): duplicates.append(i)
    percentage = len (duplicates) / tries * 100
    print( f"Doing {tries} tries with {number_of_students} students, {percentage} % of classes have at least 2 same bithdays")

#test_birthday_paradox(1000,23)

def interlock():
    interlocked_words = []
    for word in words: #oude code vereenvoudigd door slicing
        # new_word_1 = []
        # new_word_2 = []
        # count = 1
        # for letter in word:
        #     if count % 2 == 0: new_word_2.append(letter)
        #     else: new_word_1.append(letter)
        #     count += 1
        # new_word_1 = ("".join(new_word_1))
        # new_word_2 = ("".join(new_word_2))
        new_word_1 = word[::2]
        new_word_2 = word[1::2]
        if in_bisect(new_word_1, words) and in_bisect(new_word_2, words):
            interlocked_words.append([new_word_1, new_word_2, word])
            print(len(interlocked_words))
    print (interlocked_words)
#interlock()

def interlock_more():
    interlocked_words = []
    count = 0
    total_words = len(words)
    for word in words:
        if len(word) < 5: continue
        count += 1
        new_word_1 = word[::5]
        new_word_2 = word[1::5]
        new_word_3 = word[2::5]
        new_word_4 = word[3::5]
        new_word_5 = word[4::5]
        if (in_bisect(new_word_1, words) and in_bisect(new_word_2, words) and in_bisect(new_word_3, words) and
                in_bisect(new_word_4, words) and in_bisect(new_word_5, words)):
            interlocked_words.append([word, new_word_1, new_word_2, new_word_3, new_word_4, new_word_5])
        if count % 100 == 0 or count == total_words: #print progress every x words
            print (f"progress: {count/total_words*100:.2f}% and {len(interlocked_words)} interlocks found")
    print (interlocked_words)
interlock_more()
