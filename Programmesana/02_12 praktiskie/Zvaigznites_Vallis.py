for i in range(8):
    for j in range(i):#izvada pirmajā rindiņā vienu, otrajā divas zvaigznites utt augošā secībā līdz 7
        print('* ',end='')
    print('')
for i in range(6,0,-1):
    for j in range(i):
        print('* ',end='')#izvada zvaigznītes dilstošā secībā, līdz sasniedz 0
    print('')