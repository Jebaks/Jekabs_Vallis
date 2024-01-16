import math
aboli_majas = float(input('Cik kg ābolu jums ir?: '))
if aboli_majas < 0: #Pārbauda vai ābolu svars nav negatīvs
    exit()
vel_aboli = input('Vai jūs pirksiet vēl ābolu?(j/n): ')
if vel_aboli == 'j': #Vai omīte vēlas pirkt vēl ābolus?
    pirkt_aboli = float(input('Cik kg ābolu jūs vēl pirksiet?: '))
    if pirkt_aboli < 0: #Pārbauda vai ābolu svars nav negatīvs
        exit()
    abolu_cena = round(pirkt_aboli * 0.65,2)
    aboli = aboli_majas + pirkt_aboli #cik kg ābolu būs omītei kopā
else:
    aboli = aboli_majas #cik kg ābolu ir omītei

cik_cukurs = float(input('Cik jums mājās jau ir kg cukura: '))
cik_citrons = float(input('Cik jums mājās jau ir gb citrona: '))
cik_ekstrakts = float(input('Cik jums mājās jau ir ml mandeļu ekstrakta: '))
cik_kanelis = float(input('Cik jums mājās jau ir g kanēļa: '))

cukurs_vajag = round(aboli/3 - cik_cukurs,1) #izrēķina nepieciešamo cukura daudzumu(1kg)
cukurs = round(aboli/3,1)
if cukurs_vajag < 0:
    cukurs_vajag  = 0
cukurs_cena = round(math.ceil(cukurs_vajag/1)*1.25,2) #izrēķina cukura cenu uz 1kg

udens = round(aboli/3,1) #izrēķina nepieciešamo ūdens daudzumu(1 = 500ml)
udens_cena = round(udens * 0.16,2) #izrēķina ūdens cenu uz 500ml

citrons_vajag = round(aboli/3 - cik_citrons,0) #izrēķina nepieciešamo citrona daudzumu(1 = 1gb)
citrons = round(aboli/3,1)
if citrons_vajag < 0:
    citrons_vajag  = 0
citrons_cena = round(citrons_vajag * 0.4,2) #izrēķina citrona cenu uz 1gb

mandelu_ekstrakts_vajag = round(aboli/3*5 - cik_ekstrakts,1) #izrēķina nepieciešamo mandeļu ekstrakta daudzumu(1 = 1ml)
mandelu_ekstrakts = round(aboli/3*5,1)
if mandelu_ekstrakts_vajag < 0:
    mandelu_ekstrakts_vajag  = 0
mandelu_ekstrakts_cena = round(math.ceil(mandelu_ekstrakts_vajag/118)*6.78,2) #izrēķina mandeļu ekstrakta cenu pudelītei/ēm

kanelis_vajag = round(aboli/3*10 - cik_kanelis,1) #izrēķina nepieciešamo kanēļa daudzumu(1 = 1g)
kanelis = round(aboli/3*10,1)
if kanelis_vajag < 0:
    kanelis_vajag  = 0
kanelis_cena = round(math.ceil(kanelis_vajag/15)*0.93,2) #izrēķina kanēļa cenu paciņai/ām

ievarijums = aboli*1000 + cukurs*1000 + round(citrons*0.06,1)*1000 + mandelu_ekstrakts_vajag + kanelis_vajag
if vel_aboli == 'j' :
    kopa_cena = abolu_cena + cukurs_cena + citrons_cena + mandelu_ekstrakts_cena + kanelis_cena
else:
    kopa_cena = cukurs_cena + citrons_cena + mandelu_ekstrakts_cena + kanelis_cena

print('Jums',aboli,'kilogramiem ābolu vēl nepieciešams:\n',pirkt_aboli, 'kg ābolu - ', abolu_cena,'Eur\n', cukurs_vajag,'kg cukura - ', cukurs_cena,'Eur\n', udens*500,'ml ūdens - ',udens_cena,'Eur\n',citrons,'citrons/i - ',citrons_cena,'Eur\n',mandelu_ekstrakts,'ml mandeļu ekstrakta - ',mandelu_ekstrakts_cena,'Eur\n',kanelis,'g kanēļa - ',kanelis_cena,'Eur')
print('Kopā - ', round(kopa_cena,2),'Eur')
print('No ', aboli,'kilogramiem āboliem jūs iegūsiet ',ievarijums,'ml ievārījuma!')