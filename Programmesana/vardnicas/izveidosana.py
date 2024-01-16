#ar inicializācijas virkni
#key value ir pāris
'''dd = {'četri':(4,'four'), 'divi':(2,'two'), 'trīs':(3,'three')} #izveido jaunu vārdnīcu
print(dd) #izdrukā vārdnīcu
print(len(dd)) #atgriež vārdnīcas garumu
print(', '.join(dd.keys())) #atgriež atslēgas
#join noņem iekavas
print(dd['četri'])'''

#fromkeys metode vārdnīcas izveidošanai
dati = ('viens', 'divi', 'tris')
vertiba = input('Vērtība:')
vardnica = dict.fromkeys(dati, vertiba)
print(vardnica)