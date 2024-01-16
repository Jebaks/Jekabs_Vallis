def bubbleSort(array):
    amount = len(array)
    for i in range(amount):
        for j in range(0, amount - i - 1):
            if array[j]>array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
def selectionSort(array):
    amount = len(array)
    for i in range(amount):
        lowestValue = i
        for j in range(i + 1, amount):
            if array[j] < array[lowestValue]:
                array[i], array[j] = array[j], array[i]
def sort():
    amount = int(input('Ievadiet sarakstā vēlamo elementu daudzumu: '))
    array = {}

    for i in range(amount):
        name = str(input(f'Ievadiet {i+1}. studenta vārdu: '))
        score = int(input(f'Ievadiet {i+1}. studenta rezultātu: '))
        array.update({score : name})
    arrayScores = []
    arrayScores.append(array.values())

    bubbleSort(arrayScores)
    print('Sakārtotais saraksts (Bubble Sort): ')
    for i in arrayScores:
        sortedArray = {i: arrayScores[i]}
    for score in sortedArray:
        print(score, sortedArray[score], end='; ')

    """selectionSort(arrayScores)
    print('\nSakārtotais saraksts (Selection Sort): ')
    for i in arrayScores:
        sortedArray = {i: array[i]}
    for score in sortedArray:
        print(score, sortedArray[score], end='; ')"""
sort()