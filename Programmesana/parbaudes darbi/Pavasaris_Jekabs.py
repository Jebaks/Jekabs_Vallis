import math
def faktorials(n): #funkcija faktoriāla aprēķināšanai
    return math.factorial(int(n))
def zvaigznites(x): #funkcija zvaigznīšu izvadei
    print(x * '*')
def rindas(): #funkcija tukšo rindiņu izvadei
    print(' \n',' ')
def viss(): #funkcija, kurā apvienotas iepriekšējās 3 funkcijas
    print('Faktoriāla aprēķināšana')
    zvaigznites(55) #izmanto iepriekš izveidoto funkciju, lai izvadītu zvaigznīšu rindu
    while True: #rindiņa, kur atgriesties, ja lietotājs vēlas turpināt darbu
        skaitlis = int(input('Ievadiet veselu, pozitīvu skaitli(mazāku par 13):\n'))
        if skaitlis < 13 and skaitlis > 0: #pārbauda vai skaitlis ir mazāks par 13, un vai tas ir pozitīvs
            print('Faktoriāls:',faktorials(skaitlis)) #izvada faktoriāla aprēķina funkcijas rezultātu
        else:
            print('Ievadītais skaitlis ir nepareizs!')
        atbilde = input('Vai vēlaties turpināt darbu(j - jā, citi taustiņi - nē):\n')
        rindas() #izmanto funkciju, kas izvada 2 tukšas rindiņas
        if atbilde == 'j':
            continue #ja lietotājs vēlas turpināt darbu, šī rindiņa atgriež lietotāju 11. rindiņā(while True:)
        else:
            print('Paldies!')
            exit()
viss() #izsauc funkciju, kurā ir apvienotas pārējās 3 funkcijas