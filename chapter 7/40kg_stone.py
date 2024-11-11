from math import log

def stone_weighing (kg:int, result = 0):
    result += stone_calc (kg)
    return stone_weighing (kg-result, result)


def stone_calc (result):
    if result == 0: return 0
    if result == 1: return 1
    if result == -1: return -1
    if result > 1 and result <= 5: return 3
    if result <-1 and result >= -5: return -3
    if result > 5 and result <= 13: return 9
    if result < -5 and result >= -13: return -9
    else: return 27



    """if kg == 0: return 0
    if kg == 1: return "stone 1"
    if kg == 2: return "stone 2 - stone 1"
    if kg == 3: return "stone 2"
    if kg == 4: return "stone 2 + stone 1"
    if kg == 5: return "stone 3 - stone 2 - stone 1"
    if kg == 6: return "stone 3 - stone 2"
    if kg == 7: return "stone 3 - stone 2 + stone 1"
    if kg == 8: return "stone 3 - stone 1"
    if kg == 9: return "stone 3"
    """

            
       
print (stone_weighing(38))
