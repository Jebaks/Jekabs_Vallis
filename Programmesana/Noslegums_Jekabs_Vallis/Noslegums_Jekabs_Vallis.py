from datetime import datetime
def pareizs_vards(vards):
    return vards.capitalize().replace(' ', '') #funkcija, kas vārda pirmo burtu padar lielu un izņem atstarpes no vārda

def iziet(x): #funkcija pārbauda vai lietotājs ir ievadījis kādu no vārdiem, kas pārtrauc programmu
    if x == 'exit' or x == 'iziet' or x == 'stop':
        exit()
    else:
        return x
    
def iegut_datus(vards, eksperimenta_nosaukums, vieta, laiks): #funkcija ievadītos datus formatē un apvieno vienā
    return f'Vārds: {vards}, Vieta: {vieta}, Eksperimenta nosaukums: {eksperimenta_nosaukums}, Laiks: {laiks}\n'

def saglabat_datus(text):
    fileName = 'eksperimenta_dati.txt'
    try:
        with open(fileName, 'a', encoding='UTF-8') as fileName:
                fileName.writelines(text)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{fileName}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neparedzēta kļūda - {e}")

def galvena():
    print('Sveiki!\nProgramma Jums palīdzēs saglabāt eksperimentu datus.\n---------')
    while True:
        text = iegut_datus(pareizs_vards(iziet(input('Ievadiet savu vārdu: '))), iziet(input('Ievadiet eksperimenta nosaukumu: ')), iziet(input('Ievadiet eksperimenta veikšanas vietu: ')), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        #Iegūst nepieciešamos ievaddatus, un izmanto funkciju iziet(), kas pārbauda, vai lietotājs nevēlas iziet no programmas
        saglabat_datus(text)
galvena()