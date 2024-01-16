skaitli= [100,200,45,2,0.5,77,100,55,400]
zoo = ['zebra','lūsis','lama','kamielis','briedis']

print('Nesakārtots saraksts: ', skaitli, '\nSakārtots saraksts: ', sorted(skaitli), '\n--------------------------')
print('Nesakārtots saraksts: ', zoo, '\nSakārtots saraksts: ', sorted(zoo), '\n--------------------------')
print('Dilstošā secībā: ', sorted(zoo, reverse=True), '\nDilstošā secībā: ', sorted(skaitli, reverse=True))