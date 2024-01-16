valstis = {'valsts':[], 'iedzivotaji':[]}
valstis['valsts'] = ['Ķīna','Indija','ASV','Indonēzija','Pakistāna','Brazīlija','Nigēria','Bangladeša','Meksika','Japāna']
valstis['iedzivotaji'] = [1439323776, 1380004385, 331002651, 273523615, 220892340, 212559417, 206139589, 164689383, 128932753, 126476461]
karta = -1
izvele = 1
while izvele != 7: #prgramma darbojas līdz lietotājs vēlas no tās iziet
    if izvele < 1 or izvele > 7: #pārbauda vai lietotājs ir ievadījis pareizu atbildi
        print('Nepareizi dati, mēģiniet vēlreiz')
    izvele = int(input('Izvēlieteis darbību:\n1 - Valstis augošā secībā pēc nosaukuma\n2 - Valstis dilstošā secībā pēc nosaukuma\n3 - Valstis augošā secībā pēc iedzīvotāju skaita\n4 - Valstis dilstošā secībā pēc iedzīvotāju skaita\n5 - Pievienot jaunu valsti un iedzīvotāju skaitu\n6 - Apskatīt visas valstis\n7 - Iziet no programmas\n'))
    if izvele == 1:
        karta = -1
        print('Valstu nosaukumi augošā secībā:')
        for i in valstis['valsts']:
            karta += 1
            print(valstis['valsts'][karta],'-', valstis['iedzivotaji'][karta],'iedzīvotāji') #izvada valstis un to iedzīvotāju skaitu stabiņā uz leju
    if izvele == 2:
        karta = -1
        print('Valstu nosaukumi dilstošā secībā:')
        for i in valstis['valsts']:
            karta += 1
            print(valstis['valsts'][karta],'-', valstis['iedzivotaji'][karta],'iedzīvotāji')  #izvada valstis un to iedzīvotāju skaitu stabiņā uz leju
    if izvele == 3:
        karta = -1
        print('Valstu nosaukumi augošā secībā pēc iedzīvotāju skaita:')
        for i in valstis['valsts']:
            karta += 1
            print(valstis['valsts'][karta],'-', valstis['iedzivotaji'][karta],'iedzīvotāji')
    if izvele == 4:
        karta = -1
        print('Valstu nosaukumi dilstošā secībā pēc iedzīvotāju skaita:')
        for i in valstis['valsts']:
            karta += 1
            print(valstis['valsts'][karta],'-', valstis['iedzivotaji'][karta],'iedzīvotāji')
    if izvele == 5:
        karta = -1
        jauna_valsts, jauns_iedz = input('Ievadiet jaunās valsts nosaukumu: '), int(input('Ievadiet jaunās valsts iedzīvotāju skaitu: '))
        valstis['valsts'].append(jauna_valsts) #pievieno jaunās valsts nosaukumu sarakstā
        valstis['iedzivotaji'].append(jauns_iedz) #pievieno jaunās valsts iedzīvotāju skaitu sarakstā
        for i in valstis['valsts']:
            karta += 1
            print(valstis['valsts'][karta],'-', valstis['iedzivotaji'][karta],'iedzīvotāji') #izvada valstis un to iedzīvotāju skaitu stabiņā uz leju
    if izvele == 6:
        karta = -1
        for i in valstis['valsts']:
            karta += 1
            print(valstis['valsts'][karta],'-', valstis['iedzivotaji'][karta],'iedzīvotāji') #izvada valstis un to iedzīvotāju skaitu stabiņā uz leju pēc kārtas
else: #ja lietotājs ieraksta 7, programma beidzas
    print('Paldies ka lietojāt šo programmu!')
    exit()