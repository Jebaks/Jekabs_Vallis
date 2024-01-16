namesInput = input('Ievadiet vārdu virkni: ')
splitNames = namesInput.split()
dataDict = {'names' : 'usernames'}
dataDict['names'] = []
dataDict['usernames'] = []
for i in splitNames:
    usernameInput = input(f"Lūdzu, ievadiet lietotājvārdu priekš vārda '{i}':")
    dataDict['names'].append(i)
    dataDict['usernames'].append(usernameInput)
fileName = input('Ievadiet faila nosaukumu, kurā eksportēt datus: ')
try:
    karta = -1
    for i in dataDict['names']:
        karta += 1
        with open(fileName, 'w', encoding='UTF-8') as file:
            for name in dataDict:
                file.write(dataDict['names'][karta], dataDict['usernames'][karta])
except FileNotFoundError:
    print(f'Error: File "{fileName}" not found')
except Exception as e:
    print(f'Error: Unexpected error - {e}')