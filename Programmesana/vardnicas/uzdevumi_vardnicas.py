telefoni = {
    'zīmols': 'Apple',
    'modelis': '14',
    'gads': 2021
}
telefoni.update([('gads', 2022)])
print(telefoni)
skolas = {
    'Nosaukums': 'Gimnazija',
    'Novads': 'Sigulda',
    'skolenu_skaits': 569,
    'gads': 2019
}
print('Oriģinālais:', skolas)
skolas.clear()
print('Pēc dzēšanas:', skolas)
augli = {1: 'anani', 2: 'aboli', 3: 'bumbieri', 4: 'mango'}
print('Oriģinālais:', augli)
augli.pop(1)
augli.pop(3)
print('Pēc dzēšanas:', augli)
skaitli = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
if 200 in skaitli.values():
    print('Skaitlis 200 ir vārdnīcā')