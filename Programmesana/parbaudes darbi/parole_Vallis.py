username = 'Admin'
password = 'Password'
meginajumi = 1
while meginajumi <=5:
        print('Palikuši',6 - meginajumi,'mēģinājumi/ums')
        username_meg = input('Ievadiet lietotājvārdu:')
        if username_meg == 'stop':
                print('Programmas beigas!')
                exit()
        password_meg = input('Ievadiet paroli:')
        if password_meg == 'stop':
            print('Programmas beigas!')
            exit()
        if username_meg != username or password_meg != password:
            print('Nepareizi dati')
            meginajumi = meginajumi + 1
            if meginajumi > 5:
                print('Atļauts mēģināt pieslēgties 5 reizes!')
                exit()
        continue
if username_meg == username and password_meg == password:
        print('Pieslēgšanās veiksmīga')
        exit()