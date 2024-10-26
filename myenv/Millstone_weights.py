def can_make_all_weights(pieces):

    possible_weights = set([0])


    for piece in pieces:
        new_weights = set()
        for weight in possible_weights:
            new_weights.add(weight + piece)
        possible_weights.update(new_weights)


    for weight in range(1, 41):
        if weight not in possible_weights:
            return False
    return True


def find_millstone_pieces():

    for a in range(1, 38):
        for b in range(a, 39 - a):
            for c in range(b, 40 - a - b):
                d = 40 - (a + b + c)
                if d < c:
                    continue

                pieces = [a, b, c, d]
                if can_make_all_weights(pieces):
                    return pieces

    return None


def test_solution():

    pieces = find_millstone_pieces()
    if pieces:
        print(f"The four pieces weigh: {pieces[0]}, {pieces[1]}, {pieces[2]}, and {pieces[3]} kg")
        print("\nVerification:")
        possible_weights = set([0])


        for piece in pieces:
            new_weights = set()
            for weight in possible_weights:
                new_weights.add(weight + piece)
            possible_weights.update(new_weights)


        possible_weights.remove(0)
        missing_weights = []
        for i in range(1, 41):
            if i not in possible_weights:
                missing_weights.append(i)

        if missing_weights:
            print(f"Cannot make the following weights: {missing_weights}")
        else:
            print("Success! All weights from 1 to 40 kg can be made.")


if __name__ == "__main__":
    test_solution()


    #########################################################################


def verify_specific_weight(target_weight, pieces=[1, 3, 9, 27]):


    def find_combination(target, pieces, used=[], start=0):
        if target == 0:
            return used
        if start >= len(pieces):
            return None

        # Try adding the piece
        result = find_combination(target - pieces[start],
                                  pieces,
                                  used + [(pieces[start], '+')],
                                  start + 1)
        if result:
            return result


        result = find_combination(target + pieces[start],
                                  pieces,
                                  used + [(pieces[start], '-')],
                                  start + 1)
        return result

    combination = find_combination(target_weight, sorted(pieces, reverse=True))
    if combination:
        equation = f"{target_weight} = "
        terms = []
        for piece, op in combination:
            terms.append(f"{op}{piece}")
        equation += " ".join(terms)
        return equation
    return f"Cannot make {target_weight} kg"


if __name__ == "__main__":

    for weight in [5, 12, 23, 37]:
        print(verify_specific_weight(weight))