#programma ļauj lietotājam ievadīt skaitļus, pēc tam tos sakārto ar bubbleSort
#izaicinājums, tajā pašā programmā uztaisīt funkciju quickSort un selectionSort
#noformēt pēc saviem ieskatiem
def bubbleSort(array):
    amount = len (array)
    for i in range(amount):
        for j in range(0, amount - i - 1):
            if array[j]>array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def sort():
    amount = int(input('Ievadiet sarakstā vēlamo elementu daudzumu: '))
    array = []

    for i in range(amount):
        number = int(input(f'Ievadiet {i+1}. skaitli: '))
        array.append(number)

    bubbleSort(array)
    print('Sakārtotais saraksts: ')
    for number in array:
        print(number, end='; ')
sort()