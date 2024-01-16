kontakti = {'vards': [], 'numurs': []}
kontakti['vards'] = ['Anna', 'Zane', 'Jānis', 'Gustavs']
kontakti['numurs'] = ['12547865', '45697456', '26588965', '12365445']
darbiba = 0
karta = -1
while darbiba != 4:
    darbiba = int(input('Izvēlieties darbību:\n1 - drukāt kontaktus uz ekrāna\n2 - pievienot kontaktus\n3 - izdzēst kontaktus\n4 - iziet\n'))
    if darbiba == 1:
        karta = -1
        print('Jūs uzspiedāt taustiņu 1: Jūsu kontakti uz ekrāna')
        for i in kontakti['vards']: #parāda katru kontaktu
            karta += 1
            print(kontakti['vards'][karta], kontakti['numurs'][karta])
    if darbiba == 2:
        print('Jūs uzspiedāt taustiņu 2: pievienojiet jaunu kontaktu')
        jauns_vards = input('Ievadiet vārdu:')
        jauns_numurs = input('Ievadiet numuru:')
        kontakti['vards'].append(jauns_vards)
        kontakti['numurs'].append(jauns_numurs)
    if darbiba == 3:
        print('Jūs uzspiedāt taustiņu 3: izdzēsiet kontaktu')
        print('Jūs uzspiedāt taustiņu 3 :izdzēst kontaktu:')
        vards = input('Ievadi vārdu: ')
        index = kontakti['vards'].index(vards)
        kontakti['vards'].pop(index)
        kontakti['numurs'].pop(index)
print('Jūs uzspiedāt taustiņu 4: Paldies ka izmantojāt šo programmu!')
exit()