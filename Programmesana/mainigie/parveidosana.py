#int pārveidosana par str(a un b saskaita)
#a un b kā teksts tiek konkatenēti(concat)
a, b = 5, 7
print('skaitlis',a+b) #int tipa mainīgie tiek saskaitīti
print('teksts',str(a)+str(b))
a = str(a)
b = str(b)
print('teksts', a+b)

#str pārveidošana par int
s = '123'
t = '456'
print(s+t, type(s+t))
a = int(s) #virkni s pārveido par int tipa mainīgo
b = int(t) #virkni t pārveido par int tipa mainīgo
print(a+b, type(a+b))

#pārveidot no par float un atpakaļ
a = 5
print(a, type(a))
a = float(a)
print(a, type(a))
a = int(a)
print(a, type(a))
a = 123.56
a = int(a)
print(a, type(a))