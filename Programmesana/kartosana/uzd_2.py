gramatas = {}


for i in range(5):
    nosaukums = input('Ieraksti nosaukumu:')
    lappuses = int(input('Ieraksti lappušu skaitu:'))
    print('---------------------')
    gramatas[nosaukums] = lappuses
print("Lietotāja izveidotā vārdnīca:", gramatas)

#ievadītos datus sakārtot pēc atlsēgas
gramatas_kartot = sorted(gramatas,reverse=True)
print('Atslēgas dilstošā secībā:', gramatas_kartot)
print('---------------------')


#ievadītos datus sakārtot pēc vērtības
gramatas_vertiba = sorted(gramatas,key=gramatas.get)
kartota_vardnica = {}

for key in gramatas_vertiba:
    kartota_vardnica[key] = gramatas[key]
print("Vārdnīca kārtota pēc vērtībām:",kartota_vardnica)