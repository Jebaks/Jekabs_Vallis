import random
import math
print('Ievadiet riņķa līnijas rādiusu:')
r = input()
r = int(r)
print(float(r))
print('Riņķa līnijas garums: ' '{:.2f}'.format(2*math.pi*r))
print('Riņķa līnijas laukums:' '{:.2f}'.format(math.pi*math.pow(r,2)))
print('Ievadiet taisnleņķa trijstūra pirmās katetes garumu:')
k1 = int(input())
print('Ievadiet taisnleņķa trijstūra otrās katetes garumu:')
k2 = int(input())
print('Taisnleņķa trijstūra hipotenūzas garums:', '{:.2f}'.format(math.sqrt(math.pow(k1,2)+math.pow(k2,2))))
ran_sk = random.random()
print('Gadījuma skaitlis no 0 - 1: ', ran_sk)
a, b = input(), input()
print(a, b)