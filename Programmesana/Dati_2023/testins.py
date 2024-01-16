'''fails = open('ziema.txt', 'w', encoding='UTF-8')
#izveido failu
#ieraksta failā datus
saraksts = ['Alūksne\n', 'Sigulda\n', 'Valmiera\n']
fails.writelines(saraksts)
fails.write('Es te braukšu bez kājām')
fails.close()'''

#pārrakstīt faila saturu
fails = open('ziema_copy.txt','w+',encoding='UTF-8')
fails.write('Varētu drīz iet pusdienās!')
fails.close()

fails = open('ziema_copy.txt','a+',encoding='UTF-8')
fails.write('\nceams pusdienas šodien būs garšīgas')
fails.close()