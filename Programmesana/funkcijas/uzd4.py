'''''def summa(num1):
    kopsumma = 0
    for i in num1:
        kopsumma += i
    return kopsumma
saraksts = [1,4,8,21,404,3985,1,0]
print(summa(saraksts))'''''
#C -> F graadi
#(0°C × 9/5) + 32 = 32°F
def gradi(celsijs):
    farenheits = round(celsijs*9/5 +32,1)
    print('Grādi farenheitā:', farenheits)
gradi(float(input('Ierakstiet grādus celsijā:')))