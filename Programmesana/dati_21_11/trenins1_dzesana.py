file_name = 'dzest.txt'
delete_me = 'Drīz būs Ziemassvētku brīvdienas'

try:
    with open(file_name, 'r', encoding='UTF=8') as data:
        #r opens file for reading and saves in variable 'data'
    #readlines reads all lines from file and saves them in a list
        rows = data.readlines()

    with open(file_name, 'w', encoding='UTF=8') as data: #opens for writing
        for row in rows:
            if delete_me not in row:
                data.write(row)
    # if word is not found, this writes it back in the file ignoring or erasing lines which don't match
    print(f'Rindas ar vārdu {delete_me} ir veiksmīgi izdzēstas no faila {file_name}')
except FileNotFoundError:
    print(f'Kļūda:  Data {file_name} nav atrasts.')
except Exception as e:
    print(f'Kļūda: Neparedzēta kļūda - {e}')