#je hebt muntjes en briefjes
#schrijf iets dat gaat opzoeken hoe je een bepaald bedrag kan hebben in het minste aantal briefjes en muntjes
#bvb 105 = 1 x 100 & 1 x 5
#The greedy method gaat zeggen ik heb 100 dus er schiet nog 5 over...
#probeer zowel de greedy method te proberen, maar probeer hier ook een betere manier voor te bedenken met recursiviteit
munten_en_briefjes = [100, 50, 20, 10, 5, 2, 1]  # Muntjes en briefjes
bedrag = 105

def greedy_method(bedrag, munten_en_briefjes):
    resultaat = {}
    for waarde in sorted(munten_en_briefjes, reverse=True):  # Sorteer van groot naar klein
        aantal = bedrag // waarde
        if aantal > 0:
            resultaat[waarde] = aantal
            bedrag -= aantal * waarde
        if bedrag == 0:
            break
    return resultaat

print(greedy_method(bedrag, munten_en_briefjes))

munten_en_briefjes = [100, 50, 20, 10, 5, 2, 1]  # Muntjes en briefjes
bedrag = 105


def recursive_method(bedrag, munten_en_briefjes, index=0):
    if bedrag == 0:  # Base case: if the amount is 0, return an empty dictionary
        return {}

    if index >= len(munten_en_briefjes):  # If we run out of denominations, return empty (edge case)
        return {}

    waarde = munten_en_briefjes[index]
    aantal = bedrag // waarde  # Calculate the number of coins/notes for the current denomination

    # Compute the remaining solution recursively for the rest of the amount
    resultaat = recursive_method(bedrag - aantal * waarde, munten_en_briefjes, index + 1)

    if aantal > 0:  # Only add the current denomination if it contributes to the solution
        resultaat[waarde] = aantal

    return resultaat


print(recursive_method(bedrag, munten_en_briefjes))
