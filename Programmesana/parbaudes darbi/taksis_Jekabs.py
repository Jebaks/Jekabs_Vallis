print('Ievadiet pasazieru skaitu:')
pasazieri = input()
if int(pasazieri) in [1,2,3,4]:
    print('Ievadiet laiku:')
    laiks = int(input())
    if laiks in [22,23,24] or laiks < 6:
        print('Nakts tarifs')
    elif laiks not in range(0,25,1):
        print('Ievadiet pareizus datus')
        exit()
    else:
        print('Dienas tarifs')
    print('Vai taksis ir stāvvietā?(j/n):')
    stavvieta = input()
    if stavvieta == 'j':
        print('Nav jāmaksā izsaukuma cena')
    elif stavvieta == 'n':
        print('Jāmaksā izsaukuma cena')
    else:
        print('Ievadiet pareizus datus')
        exit()
    print('Vai jums vajag gaidīšanas laiku?(j/n):')
    gaidisana_vajag = input()
    if gaidisana_vajag == 'j':
        print('Ievadiet gaidīšanas laiku min:')
        gaidisana = int(input())
    print('Ievadiet brauciena attālumu km:')
    attalums = int(input())
    print('Nolīgšana = 1,25 Eur')
    if laiks in [22,23,24] or laiks < 6:
        maksa_nakts = 0.67*attalums
        print('Nakts tarifs =', round(maksa_nakts), 'Eur')
    else:
        maksa_diena = 0.57*attalums
        print('Dienas tarifs =', round(maksa_diena), 'Eur')
    if stavvieta == 'j':
        print('Nav jāmaksā izsaukuma cena')
    elif stavvieta == 'n':
        print('Jāmaksā izsaukuma cena = 2.20 Eur')
    if gaidisana_vajag == 'j':
        maksa_gaidisana = gaidisana*0.13
        print('Gaidīšanas laiks =', round(maksa_gaidisana), 'Eur')
        if laiks in [22,23,24] or laiks < 6:
            if stavvieta == 'n':
                print('Kopā:', round(maksa_nakts + 2.20 + maksa_gaidisana + 1,25))
            else:
                print('Kopā:', round(maksa_nakts + maksa_gaidisana + 1,25))
        else:
            if stavvieta == 'n':
                print('Kopā:', round(maksa_diena + 2.20 + maksa_gaidisana + 1,25))
            else:
                print('Kopā:', round(maksa_diena + maksa_gaidisana + 1,25))
    else:
        if laiks in [22,23,24] or laiks < 6:
            if stavvieta == 'n':
                print('Kopā:', round(maksa_nakts + 2.20 + 1.25))
            else:
                print('Kopā:', round(maksa_nakts + 1.25))
        else:
            if stavvieta == 'n':
                print('Kopā:', round(maksa_diena + 2.20 + 1.25))
            else:
                print('Kopā:', round(maksa_diena + 1,25))
elif int(pasazieri) > 4:
    print('Nepietiek vietas')
else:
    print('Ievadiet pareizus datus')
    exit()