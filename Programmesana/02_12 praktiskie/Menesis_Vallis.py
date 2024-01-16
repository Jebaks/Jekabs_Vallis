menesis = input('Ievadi kādu no mēnešiem:Jan,Feb,Mar,Apr,Mai,Jūn,Jūl,Aug,Sep,Okt,Nov,Dec:')
dienas_31 = ['Jan','Mar','Mai','Jūl','Aug','Okt','Dec']#sarakst ar menesiem ar 31 dienām
if menesis == 'Feb':
    print('Mēnesī ir 28/29 dienas')
elif menesis in dienas_31:#pārbauda vai menesis ir 31 dienu menesu saraksta
    print('Mēnesī ir 31 diena')
else:
    print('Mēnesī ir 30 dienas')
