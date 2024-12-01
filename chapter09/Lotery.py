def check_number_lotery(lotery_number, total):
    steps = 0
    max_number = total
    min_number = 0
    search_number = total

    while search_number != lotery_number:
        steps += 1
        if lotery_number > search_number:
            min_number = search_number
        else:
            max_number = search_number  #100

        search_number = ((max_number - min_number) // 2) + min_number  # 50
        print(lotery_number, steps, search_number)

check_number_lotery(12651, 100000)

#getal ingeven: pc moet raden of het nr juist is.
#Hoeveel st appen zijn hiervoor nodig, voor hij het vind.
#dan dat programma laten lopen voor 1 tot 10 000
#Voor welk getal is het langste de stappen nodig om tot het getal te komen.
