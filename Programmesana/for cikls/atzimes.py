#izveidot sarakstu 'atzīmes' ar punktiem (testā iegūtie)(10 no 60 - 99)
#ar for ciklu 'iziet cauri' sarakstam
#ar elif nosacījumu uz ekrāna parādīt punktus un atzīmi
#>=90 - A  >=80 - B  70 - 80 - C 60 - 70 - D ja zem 60 - F
#grūtāk - var pielikt datu ievadi, atkarībā no ievadītā skaitļa parādīt burtu
punkti_visi = [82,61,90,99,96,75,79,68,87]
atzime_punkti = []
for punkti in punkti_visi:
    if punkti >= 90:
        atzime = 'A'
    elif punkti >=80:
        atzime = 'B'
    elif punkti >=70:
        atzime = 'C'
    elif punkti >=60:
        atzime = 'D'
    else:
        atzime = 'F'
    atzime_punkti.append([punkti,atzime])
print(atzime_punkti)