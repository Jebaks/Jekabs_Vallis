fails = open('dati.txt','a',encoding='utf-8') #izveidos failu
fails.write('Ingvera sula garšo pēc suši!!\n')
#katru reizi palaižot programmu, teksts tiek pievienots klāt

fails = open('dati.txt','r',encoding='utf-8')
print(fails.read())

fails = open('dati.txt','w',encoding='utf-8')
fails.write('Mācos rakstīt failā\n')

fails = open('dati.txt','a',encoding='utf-8')
fails.write('Ērces jau moduās!Kazas!!!')

fails.close()