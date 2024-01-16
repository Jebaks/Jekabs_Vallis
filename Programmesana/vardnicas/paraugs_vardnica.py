#izveidot vārdnīcu ar skaitļa tipa atslēgu
dict1 = {
    1:'Tev', 
    2:'garšo', 
    3:'āboli'
}
print('Vārdnīca ar skaitļa tip atslēgām:')
print(dict1[1])
print(dict1[2])
print(dict1[3])
#izveido vārdnīcu ar non-numeric keys
dict2 = {
    'Auglis':'Ābols',
    'Augļu_karalis':'Mango',
    'Sezonas_auglis':'Apelsīns'
}
print('Vārdnīca ar non-numeric keys')
print(dict2['Auglis'])
print(dict2['Augļu_karalis'])
print(dict2['Sezonas_auglis'])
