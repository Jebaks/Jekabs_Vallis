print('Divciparu skaitļa ciparu summas aprēķins')
print('Ievadiet divciparu skaitli!')
skaitlis = int(input())#jakonvertē jo input() datus sniedz kā tekstu
pirmais_cipars = skaitlis//10#iegūst pirmo ciparu
otrais_cipars = skaitlis%10#iegūst otro ciparu
print('Divciparu skaitlis =', skaitlis)
print('Pirmais cipars:', pirmais_cipars)
print('Otrais cipars:', otrais_cipars)
print(pirmais_cipars+otrais_cipars)