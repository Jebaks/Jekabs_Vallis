import math
viss_ir = 'n'
preces = []
while viss_ir == 'n':
    prece = input('Ievadiet preces nosaukumu:')
    cena = float(input('Ievadiet preces cenu:'))
    if cena < 0:
        exit()
    daudzums = int(input('Ievadiet preces daudzumu:'))
    if daudzums < 0:
        exit()
    karte = input('Vai jums ir karte? j/n ')
    atl1 = cena * daudzums - cena * daudzums * 0.3
    if karte == 'j':
        atl2 = cena * daudzums - cena * daudzums * 0.4
        atl3 = cena * daudzums * 0.5
    else:
        atl2 = cena * daudzums
        atl3 = cena * daudzums - cena * daudzums * 0.2
    if daudzums >= 3:
        atl4 = cena * daudzums - cena * daudzums * 0.3
    else:
        atl4 = cena * daudzums
    atl5 = cena * daudzums - daudzums //2 * cena
    ko_perk = daudzums, prece, 'maksā'
    ceks = ko_perk, '{:.2f}'.format(atl1),'{:.2f}'.format(atl2),'{:.2f}'.format(atl3),'{:.2f}'.format(atl4),'{:.2f}'.format(atl5)
    preces.append(ceks)
    viss_ir = input('Vai ir nopirkts viss, kas sarakstā? j/n ')
    if viss_ir == 'j':
        num = 0
        while num < 6: #čekā ir 6 sastāvdaļas
            final = [i[num] for i in preces]
            print(*final,sep=' ') #izprintē katru čeka sastāvdaļu
            num = num +1
        exit()