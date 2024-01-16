darzeni = ['zirņi','burkāni','kartupeļi','batātes','gurķi']
print('Oriģinālais saraksts: ', darzeni)
darzeni.sort()
print('sakārtots ar sort: ', darzeni)

viens = [7,3,5.4,-5,4,6.495,0,48,746]
print(sorted(viens)) #atgriež jaunu sarakstu nemainot oriģinālo
print('Oriģinālais: ',viens)

darzeni_kartots = sorted(darzeni,reverse=True)
print('Apgriezts: ',darzeni_kartots)

saraksts = ['divi','trīs','pieci','viens','septiņi','deviņi']
saraksts_augosi = print(sorted(saraksts,key=len)) #pēc garuma augoši
saraksts_dilstosi = print(sorted(saraksts,key=len,reverse=True)) #pēc garuma dilstoši

strs = ['rīts', 'Vakars', 'pusdienas', 'KOMPLEKSIŅŠ','ZEMENES']
strs.sort() #nevar likt print f-jā
print('Kārtots: ',strs)
print('Kārtots ar str.lower: ',sorted(strs, key=str.lower)) #ignorē upercase
print('Kārtots ar str.upper: ',sorted(strs, key=str.upper)) #ignorē lowercase
print('Kārtots ar str.lower: ',sorted(strs, key=str.lower, reverse=True))

