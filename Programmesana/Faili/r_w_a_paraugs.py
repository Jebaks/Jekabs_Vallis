fails = open('dati2.txt','a',encoding='utf-8')
'''pilsētas = ['Daugavpils\n','Rīga\n','Liepāja\n']
fails.writelines(pilsētas) #raksta vairākas rindiņas, bet .write tikai vienu'''

ffails=open('dati2.txt','w',encoding='utf-8')
valstis={
    'Daugavpils':'Latvija',
    'Čitagonga':'Bangladeša',
    'Vladivostoka':'Krievija'
}
for object in valstis:
    fails.write(valstis[object]+'\n')