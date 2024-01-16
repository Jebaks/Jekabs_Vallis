file_name = 'dzest.txt'
add_me = 'Ēst'

try:
    with open (file_name, 'a', encoding='UTF=8') as data:
        data.write(f'\n{add_me}')

except FileNotFoundError:
    print(f'Kļūda:  Data {file_name} nav atrasts.')
except Exception as e:
    print(f'Kļūda: Neparedzēta kļūda - {e}')