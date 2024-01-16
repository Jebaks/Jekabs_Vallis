a = 7
for i in range(1,13):
    print('Cik ir',a,'x',i,'?')
    min = input()
    if min == 'stop':
        break
    if min == 'izlaist':
        print('tiek izlaists')
        continue
    atb = i*a #glabā pareizās atbildes
    if int(min) == atb:
        print('Pareizi!')
    else:
        print('Nē, tas ir', atb)