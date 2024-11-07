def main ():
    t = 'l', 'u', 'p', 'i', 'n'
    print (type (t))
    t = tuple ("masker from zorro")
    for i in t:
        print (i)
    print (sorted (t))
    print (tuple (reversed (t)))
    email = 'monty@python.org'
    username, domain = email.split ('@')
    print (username, domain)
    print (domain)

    d = {'one': 1, 'two': 2}

    for item in d.items ():
        key, value = item
        print (key, '->', value)

    for key, value in d.items ():
        print (key, '->', value)

    a, b = 1, 2
    a, b = b, a

    print (a, b)

    print (divmod (7, 3))

    def min_max (t):
        return min (t), max (t)

    print (min_max ([2, 4, 1, 3]))

    def mean (*args):
        return sum (args) / len (args)

    print (mean (1, 2, 3, 10))

    def trimmed_mean (*args):
        low, high = min_max (args)
        trimmed = list (args)
        trimmed.remove (low)
        trimmed.remove (high)
        return mean (*trimmed)

    print (trimmed_mean (1, 2, 3, 10))

    scores1 = [1, 2, 4, 5, 1, 5, 2]
    scores2 = [5, 5, 2, 2, 5, 2, 3]
    for pair in zip (scores1, scores2):
        print (pair)

    wins = 0
    for team1, team2 in zip (scores1, scores2):
        if team1 > team2:
            wins += 1

    letters = 'abcdefghijklmnopqrstuvwxyz'
    numbers = range (len (letters))
    letter_map = dict (zip (letters, numbers))

    def value_counts (string):
        counter = {}
        for letter in string:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
        return counter

    counter = value_counts ('banana')
    print (counter)
    items = counter.items ()

    def second_element (t):
        return t[1]

    sorted_items = sorted (items, key=second_element)
    sorted_items
    print (sorted_items)
    print (max (items, key=second_element))

    print (wins)

    def invert_dict (d):
        new = {}
        for key, value in d.items ():
            if value not in new:
                new[value] = [key]
            else:
                new[value].append (key)
        return new

    print (invert_dict (counter))


if __name__ == '__main__':
    main ()
