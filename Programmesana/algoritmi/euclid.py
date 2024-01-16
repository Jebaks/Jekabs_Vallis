x, y = int(input('Ievadiet pirmā skaitļa vērtību: ')), int(input('Ievadiet otrā skaitļa vērtību: '))
if x > y:
    a, b = x, y
else:
    a, b = y, x
while a % b != 0:
    a, b = b, a % b
else:
    print(f'Lielākais skaitļu {x} un {y} kopīgais dalītājs ir {b}')