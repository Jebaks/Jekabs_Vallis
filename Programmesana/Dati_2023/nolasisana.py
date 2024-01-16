fileName = 'mana_klase.txt'
try:
    with open(fileName, 'r',encoding='UTF-8') as file:
        for line in file:
            data = line.split() #splits every line in words
            #checks if theres enough data (name, last name, age)
            if len(data) >= 3:
                name = data[0]
                lastName = data[1]
                age = data[2]

                print(f'Name: {name}, Last name: {lastName}, Age: {age}')
            else:
                print('Error: Not enough data in file')
except FileNotFoundError:
    print(f'Error: File "{fileName}" not found')
except Exception as e:
    print(f'Error: Unexpected error - {e}')