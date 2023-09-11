import math
print('Recepte ievārijumam (1L):\n -Āboli 2kg \n -Cukurs 1,25kg \n -Kanēlis 12g \n')
ciklitri = float(input('Cik litrus ievārījuma jūs vēlaties izvārīt?'))

def aboli_aprekins(litri,aboli_ir):  #Funkcija aprēķina ābolu daudzumu
    aboli = litri * 2 - aboli_ir
    return(aboli)

def cukurs_aprekins(litri,cukurs_ir):   #Funkcija aprēķina cukura daudzumu
    cukurs = litri * 1.25 - cukurs_ir
    return(cukurs)

def kanelis_aprekins(litri,kanelis_ir):   #Funkcija aprēķina kanēļa daudzumu
    kanelis = (litri * 0.012 - (kanelis_ir * 0.001)) * 1000
    return(kanelis)

pieejamsaboli = input('Vai Jums ir pieejami āboli? (j/n):')
if pieejamsaboli == 'j':  #Ja lietotājam ir pieejami āboli, tad jautā cik āboli viņam jau ir
    aboli_ir = float(input('Ievadiet ābolu daudzumu (kg):'))
    aboli = float(aboli_aprekins(ciklitri,aboli_ir))
    print('Nepieciešams:', aboli, 'kg ābolu')

elif pieejamsaboli == 'n':
    x=0
    aboli_ir = 0  #Abolu daudzums ir 0, jo lietotājam neesot pieejami aboli
    aboli = float(aboli_aprekins(ciklitri,x))
    print('Nepieciešams:', aboli, 'kg ābolu')
else:
    print('Mēģiniet vēlreiz!')
    exit()

pieejamscukurs = input('Vai Jums ir pieejams cukurs? (j/n):')
if pieejamscukurs == 'j':     #Ja lietotājam ir pieejams cukurs, tad jautā cik kg cukura viņam jau ir
    cukurs_ir = float(input('Ievadiet cukura daudzumu (kg):'))
    cukurs = float(cukurs_aprekins(ciklitri,cukurs_ir))
    print('Nepieciešams:', cukurs, 'kg cukura')

elif pieejamscukurs == 'n':
    x=0
    cukurs_ir = 0   #Cukura daudzums ir 0, jo lietotājam neesot pieejams cukurs
    cukurs = float(cukurs_aprekins(ciklitri,x))
    print('Nepieciešams:', cukurs, 'kg cukura')
else:
    print('Mēģiniet vēlreiz!')
    exit()

pieejamskanelis = input('Vai Jums ir pieejams kanēlis? (j/n):')
if pieejamskanelis == 'j': #Ja lietotājam ir pieejams kanēlis, tad jautā cik grami kanēļa viņam jau ir
    kanelis_ir = float(input('Ievadiet kanēļa daudzumu (g):'))
    kanelis = float(kanelis_aprekins(ciklitri,kanelis_ir))
    print('Nepieciešams:', kanelis, 'g kanēļa')

elif pieejamskanelis == 'n':
    x=0
    kanelis_ir = 0 #Kanēļa daudzums ir 0, jo lietotājam neesot pieejams kanēlis
    kanelis = float(kanelis_aprekins(ciklitri,x))
    print('Nepieciešams:', kanelis, 'g kanēļa')

else:
    print('Mēģiniet vēlreiz!')
    exit()

aboli_cena = 0.69 * aboli
cukurs_cena = 1.35 * cukurs
kanelis_cena = 0.06 * kanelis
kopcena = aboli_cena + cukurs_cena + kanelis_cena

print ('------------------- Čeks -------------------')
print('Jums jau ir:', aboli_ir,'kg ābolu\nJums vēl jāpērk:', aboli, 'kg ābolu:', round(aboli_cena,2), '€')
print('Jums jau ir:', cukurs_ir,'kg cukura\nJums vēl jāpērk:', cukurs, 'kg cukura:', round(cukurs_cena,2), '€')
print('Jums jau ir:', kanelis_ir,'g kanēļa\nJums vēl jāpērk:', kanelis, 'g kanēļa:', round(kanelis_cena,2), '€')
print('Kopā:', round(kopcena,2), '€')
print('---------------------------------------------')