name = 'Anna'
teksts = 'teksts'
skaitlis = 9 #skaitlis ir skaitlis, ja nav pēdiņās
print(name) #rakstīt nosaukumu, kurur grib izdrukāt
print(skaitlis)
kombo = name, teksts #mainīgo apvienošana
print(kombo)
print('teksts var būt ar garumzīmēm','mainīgajiem neliec garumzīmes')

#atrast vārda garumu
varda_garumu = len(name)
print(varda_garumu)

#chained_assingment = kaskādes veida piešķiršana
a = b = c = 300
print(a, b, c)

a, b = 10, 'hello'
print(a)
print(b)

masina = 'Volvo'
print(masina)
x = 50
print(x)
x, y = 5, 10
print(x+y)
z = x+y
print(z)