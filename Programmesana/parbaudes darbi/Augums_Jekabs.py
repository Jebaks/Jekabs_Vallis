skolena_augums = {'vards': [], 'augums':[]}
skolena_augums['vards'] = ['Jānis', 'Pēteris', 'Artūrs', 'Vilnis', 'Juris', 'Anna', 'Emīlija', 'Paula', 'Elza', 'Reinis', 'Hugo', 'Ieva']
skolena_augums['augums'] = [172, 185, 164, 184, 162, 164, 165, 167, 177, 184, 165, 180]
darbiba = 0
karta = -1
for i in skolena_augums['vards']:
        karta += 1
        print(skolena_augums['vards'][karta],'-', skolena_augums['augums'][karta],'cm') #izvada visus skolēnu vārdus un augumus stabiņā pēc kārtas
while darbiba != 4: #atkārto programmu, līdz lietotājs vēlas no tās iziet
    
    darbiba = int(input('Izvēlieties darbību:\n1 - pievienot datus\n2 - izdzēst datus\n3 - parādīt skolēnu vidējo augumu\n4 - iziet no programmas\n'))
    if darbiba > 4 or darbiba < 1:
        print('Nepareizi dati, mēģiniet vēlreiz')

    if darbiba == 1:
        print('Jūs uzspiedāt taustiņu 1, pievienojiet jaunā skolēna datus:')
        jauns_vards, jauns_augums = input('Ievadiet jaunā skolēna vārdu: '), int(input('Ievadiet jaunā skolēna augumu: '))
        skolena_augums['vards'].append(jauns_vards) #ievieto jaunā skolēna vārdu sarakstā
        skolena_augums['augums'].append(jauns_augums) #ievieto jaunā skolēna augumu sarakstā
        karta = -1
        for i in skolena_augums['vards']:
            karta += 1
            print(skolena_augums['vards'][karta],'-', skolena_augums['augums'][karta],'cm') #izvada visu sarakstā jau esošo skolēnu datus un pievienotā skolēna datus
        print('Jūs pievienojāt:', jauns_vards, ', un šis skolēns ir', jauns_augums, 'cm garš/a') #parāda kuru skolēnu un kādu augumu pievienoja sarakstam

    if darbiba == 2:
        print('Jūs uzspiedāt taustiņu 2, ievadiet skolēna vārdu, kura datus vēlaties izdzēst:')
        izdzest_vards = input('Ievadiet vārdu: ')
        index = skolena_augums['vards'].index(izdzest_vards) #nosaka ievadītā vārda kārtas nr. sarakstā
        skolena_augums['vards'].pop(index) #izmantojot iegūto kārtas nr. no saraksta izņem tā skolēna vārdu no saraksta
        skolena_augums['augums'].pop(index) #izmantojot iegūto kārtas nr. no saraksta izņem tā skolēna augumu no saraksta

        karta = -1
        for i in skolena_augums['vards']:
            karta += 1
            print(skolena_augums['vards'][karta],'-', skolena_augums['augums'][karta],'cm') #izvada jauno sarakstu
        print('Jūs izdzēsāt skolēna', izdzest_vards, 'datus') #parāda kuru skolēnu izdzēsa no saraksta
    
    if darbiba == 3:
        vid_augums = sum(skolena_augums['augums']) / len(skolena_augums['augums']) #aprēķina visu sarakstā esošo augumu summu un to izdala ar sarakstā esošo datu skaitu
        print('Jūs uzspiedāt taustiņu 3, skolēnu vidējais augums:', round(vid_augums, 2), 'cm') #izvada noapaļotu vidējo augumu
else:
    print('Paldies ka izmantojāt šo programmu!')
    exit()