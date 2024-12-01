

## test


print("Eindopdracht Python 1")

import random
turn=0
first_name=""
last_name=""
#Declare the variable outside of any function to make it global.
#Use the global keyword inside each function where you want to modify the global variable.

def escape_room():
    
    global turn
    global first_name
    global last_name
    
    riddles=[
        ("Wat is de naam van de groep criminelen die tussen 1730 en 1742 het Zuiden van Limburg overspoelde met diefstallen en roofovervallen,?", "Bokkenrijders"),
        ("Wat is de naam van de Brits natuurkundige, kosmoloog en wiskundige die verantwoordelijk was voor de uitgave van het boek A Brief History of Time ?", "Stephen William Hawking"),
        ("Wie was de eerste koning van Nederland?", "Willem van Oranje"),
        ("Wat is de naam van de laatste Romeinse keizer die behoorde tot de Vijf Goede keizers en die daarnaast ook een stoïcist was?", "Marcus Aurelius"),
        ("Wat is de naam van het Amerikaanse herstelplan voor de wederopbouw van Europa na Wereldoorlog II?", "Marshallplan"),
        ("Wie was de Sovjet-piloot en kosmonaut die op 12 april 1961 als eerste mens ter wereld een ruimtereis maakte?", "Yuri Gagarin"),
        ("Wie veroverde in het jaar 1453 Constantinopel?", "Mehmet II"),
        ("In welk jaar viel Bagdad in handen van de Mongolen?", "1258"),
        ("Wat is de naam van het burgerlijk wetboek dat Napoleon Bonaparte op 21 maart 1804 invoerde?", "Code Napoleon"),
        ("Wie heeft de Body Mass Index of kortweg BMI uitgevonden?", "Adolphe Quetelet")
    ]
    print("\nWelkom bij de mini escape room! Los de raadsels op om te ontsnappen. U moet minstens 5 raadsels juist oplossen om buiten te geraken.\n")
#The 'if not' statement in Python checks if a condition is not true.
#It helps you make decisions and execute specific code when a condition is false.
#In a nutshell, you want to take action only when something doesn't happen, like checking if a list is empty or a value is not present.   
#De functie is_valid_name() controleert of de naam alleen letters bevat met behulp van de ingebouwde stringmethode .isalpha().
#Namen zoals "Bob123" en "Marie-Louise" worden afgekeurd omdat ze respectievelijk cijfers en een streepje bevatten.
#We gebruiken strip() om eventuele voor- en achterliggende spaties te verwijderen.
    
    if not first_name and not last_name:
        while not first_name.isalpha() or not last_name.isalpha():
            first_name=input("Voer uw voornaam in: ").strip()
            last_name=input("Voer uw achternaam in: ").strip()
            if not first_name.isalpha() or not last_name.isalpha(): 
                print("Uw naam mag enkel letters bevatten. Probeer nogmaals.")
    else:
        first_name==first_name and last_name==last_name
        
    number_riddles=0
    while number_riddles==0 or number_riddles<1 or number_riddles>10:
        try:
            number_riddles=int(input("\nU kan maximaal 10 raadsels oplossen. Indien u 0 ingeeft, stopt het spel. Hoeveel raadsels wil u oplossen? "))
            if number_riddles==0:
                print("Het spel is gestopt.")
                return
            if number_riddles<1 or number_riddles>10:
                    print("Uw aantal gekozen raadsels moet minstens 1 zijn en hoogstens 10. Probeer nogmaals.")
        except ValueError:
                    print("Uw aantal gekozen raadsels mag enkel cijfers bevatten. Probeer nogmaals.")

    selected_riddles=random.sample(riddles, number_riddles)
    correct_answers=0
    results=[]

    for i, (riddle, answer) in enumerate(selected_riddles):
        print(f"Raadsel {i+1}: {riddle}")
        user_answer=input("Jouw antwoord: ")
        if user_answer==answer:
            print("De oplossing was correct!")
            correct_answers+=1
            results.append((riddle, "De oplossing was correct!"))
        else:
            print("De oplossing was fout!")
            results.append((riddle, "De oplossing was fout!"))
    
    if correct_answers>=4:
        print("\nGefeliciteerd, u hebt voldoende raadsels juist opgelost en u bent ontsnapt!\n")
    else:
        print("\nHelaas, u hebt niet voldoende raadsels juist opgelost en u zit nog vast in de mini escape room!\n")
    
#https://community.dataquest.io/t/using-the-append-method-with-two-arguments/515619
#The error message explains all, .append() method takes exactly one argument.
#since you want to append both created_at,num_comments it would be great if you append them as a tuple or list
#The append() method in python adds a single item to the existing list.
#The error says that append() takes exactly one argument. That’s the reason you got the error in the first code: you passed two arguments.
#In the second code, you put these two items into a list and passed the list as the only argument. Therefore, you passed only one argument as append() requires.

    total_riddles=len(selected_riddles)
    wrong_answers=total_riddles-correct_answers
    average_score=(correct_answers/total_riddles)*100
    turn+=1
    with open(f"{first_name}{last_name}_resultaten_spel{turn}.txt", "w") as file:
        file.write(f"Naam: {first_name} {last_name}\n")
        file.write(f"Totaal aantal opgeloste raadsels: {total_riddles}\n")
        for riddle, result in results:
            file.write(f"{riddle} - {result}\n")
        file.write(f"Totaal aantal goede opgeloste raadsels: {correct_answers}\n")
        file.write(f"Totaal aantal fout opgeloste raadsels: {wrong_answers}\n")
        file.write(f"Gemiddelde score: {average_score:.2f}%\n")
    print(f"\nDe resultaten van het spel zijn opgeslagen in '{first_name}{last_name}_resultaten_spel{turn}.txt'.\n")

#In Python wordt :.2f vaak gebruikt in formattering om een getal met twee cijfers achter de komma weer te geven.
#Dit is handig voor het weergeven van decimale waarden met een gewenste precisie.
    
    replay=""
    while not replay=="ja" or replay=="nee":
        replay=input("Wil u nog een keer spelen? (ja/nee): ")
        if replay=="ja":
            escape_room()
        elif replay=="nee":
            print("Bedankt voor het spelen!")
            return
        else:
            print("U hebt geen ja of nee geantwoord.") 
    
escape_room()

"""Opdracht Python. 
Je maakt een mini escape room waarbij de gebruiker een aantal raadsels moet oplossen om te winnen en 
dus buiten te geraken. We voorzien 10 raadsels zoek hiervoor op het internet naar raadsels die je kan 
gebruiken je mag zelf kiezen of je bv meer richting taal, rekenen,... gaat of combinaties maakt.  
Bij aanvang van het spel vraag je aan de gebruiker zijn naam en hoeveel raadsels hij wenst op te lossen. 
Dit is een getal van 1 tot 10. Geeft de gebruiker 0 in dan stopt het spel. De gebruiker kan zelf niet kiezen 
welk van de raadsels hij moet oplossen want op basis van het aantal raadsels dat hij wenst op te lossen 
worden random de getallen van de raadsels die hij moet oplossen gegenereerd.  
Vervolgens gaat hij elk van die raadsels krijgen en moet hij er dus zoveel mogelijk juist oplossen. Je geeft 
ook telkens aan of de oplossing van dat raadsel goed of fout was maar het mag de gebruiker niet 
tegenhouden om naar een volgend raadsel te gaan.  
Op het einde van het spel krijgt de speler wel een printje (output dus naar tekstbestand) met zijn naam. 
Het aantal raadsels dat hij heeft opgelost, of ze goed of fout zijn opgelost en het totaal aantal goede en 
het totaal aantal fout opgeloste raadsels en zijn gemiddelde score in % 
De speler moet ook kunnen aangeven of hij nog eens wenst te spelen of wenst te stoppen.  
Werk zo efficiënt mogelijk, bouw de nodige controles in en vang indien nodig ook fouten op die je kan 
voorzien."""
