#tiek realizēta decimālskaitļu ievade
#aprēķināts izteiksmes (x+y)*(x-y)//(x-y) rezultāts

print('Ievadiet savu vārdu')
vards = input()
print('Jūsu vārds ir:',vards)
def ievadiet(num1,num2):
    print('Ievadītais skaitlis:', num1, '\nIevadītais skaitlis:', num2 )
    rezultats = (num1+num2)*(num1-num2)//(num1-num2)
    print('Rezultāts: ', rezultats)
ievadiet(float(input('Ievadiet decimālskaitli:')),float(input('Ievadiet decimālskaitli:')))