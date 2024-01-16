#uzrakstīt programmu, kurā ir 2 saraksti + abus apvienot
mans_saraksts = ['svece',2,'sāls']#pirmais elements ir ar indeksu 0
otrs_saraksts = ['karstmaizes','brauniji','kafija']

saraksts = mans_saraksts + otrs_saraksts
print(saraksts)

#nokopēt saraksta vērtības un ielikt tās jaunā sarakstā
milzis = ['zupa','dzervene','tastatūra']
jauns = list(milzis)
print(milzis)
print(jauns)

#izveidot sarakstu ar 4 krasu nosaukumiem. Atrast katra elementa garumu
krasas = ['zils','zaļš','dzeltens','sarkans']
jauns_saraksts = [] #tukšs saraksts
for krasa in krasas:
    burti = 0 #katru reizi palaizot sarakstu, atgriežas uz 0
    for burts in krasa:
        burti +=1 #katru reizi pieskaita 1
    pagaidu_saraksts = [krasa, burti]
    jauns_saraksts.append(pagaidu_saraksts)
print(jauns_saraksts)

#Kā šo kodu var uzrakstit ar mazāk rindiņām, vai ir vienkāršāks veids kā atrast katra vārda garumu
for krasa in krasas:
    print(krasa, len(krasa))