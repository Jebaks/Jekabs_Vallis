valstis = {
    'Somija':['Helsinki','Rovaniemi','Tampere','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bergena','Arendāla','Trumse','Molde'],
    'Dānija':['Kopenhāgena','Odense','Esbjerga','Aarhus','Ronne']
}
#1. variants ar for ciklu
print('---------------------')
for atslega, vertiba in valstis.items():
    for i in vertiba:
        print(atslega, ':',i)
    print('---------------------')
#2. variants ar for ciklu vienai atslēgu grupai
for i in valstis['Dānija']:
    print(i)
#iegūt konkrētas pilsētas no vārdnīcas
print(valstis['Somija'][:3])
#iegūt pēdējās divas pilsētas
print(valstis['Norvēģija'][3:])
#iegūt 2. - 5.
print(valstis['Dānija'][1:5])