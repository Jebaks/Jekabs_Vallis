import math
kopeja_cena = []
def linolejs_daudzums(telpa_platums, telpa_garums, linoleja_platums, linoleja_cena_m2):
    izmers = telpa_platums * telpa_garums
    linoleja_garums = math.ceil(izmers) / linoleja_platums
    print('---------------------------------------')
    print('Istabas izmērs ir', round(izmers, 2), 'm2')
    print('Jums nepieciešams',math.ceil(izmers) , 'm2 linoleja, jeb', linoleja_garums, 'm no šī ruļļa')
    cena = round(izmers * linoleja_cena_m2, 2)
    print('Jums paliks pāri', math.ceil(izmers) - round(izmers, 2), 'm2 linoleja')
    print('Tas maksās', cena, 'Eur\n---------------------------------------')
    kopeja_cena.append(cena)

beigt = 1
while beigt != 'n':
    linolejs_daudzums(float(input('Ievadiet telpas platumu (m):')),float(input('Ievadiet telpas garumu (m):')),float(input('Ievadiet linoleja ruļļa platumu(m):')),float(input('Ievadiet linoleja ruļļa cenu uz m2(Eur):')))
    beigt = input('Vai Jūs klāsiet vēl linoleju?(j/n):')
    print('Viss kopā maksā',sum(kopeja_cena),'Eur\n---------------------------------------')
else:
    print('Paldies ka izmantojāt šo programmu!')
    exit()