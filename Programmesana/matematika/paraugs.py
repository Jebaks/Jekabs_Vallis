import math #raksta programmas sakuma tikai 1 reizi
skaitlis = 21.6
print('Noapaļots uz leju:',math.floor(skaitlis)) #noapaļo uz leju
print('Noapaļots uz augsu:',math.ceil(skaitlis)) #noapaļo uz augsu

print('PI vērtība:',math.pi) #atgriež pi vertibu
print(math.pow(skaitlis,3)) #kāpina pirmo skaitli ar otro(skaitlis kaapina 3.pakape)

#skaitļu formatēšana
x = 239562/202
print('Bez formatēšanas:',x)
print('Ar formatēšanu:' '%.4f'%x)
print('Ar formatēšanu:' '{:.2f}'.format(x))