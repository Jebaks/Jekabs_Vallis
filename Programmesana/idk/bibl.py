nenodots = input('Vai Jums ir laikā nenodots izdevums? j/n:')
if nenodots == 'j': #pārbauda vai personai ir laikā nenodots izdevums
    print('izdevumu nesaņem')
else:
    pieprasits = input('Vai izdevums ir pieprasīto izdevumu sarakstā? j/n:')
    if pieprasits == 'j':
        print('izdevumu saņem uz 3 dienām')
    else: #pārbauda vai izdevums ir pieprasīto izdevumu sarakstā
        zurnals = input('Vai publikācija ir žurnāls? j/n:')
        if zurnals == 'j':
            print('izdevumu saņem uz 10 dienām')
        else:
            persona = input('Vai Jūs esat students? j/n:')
            if persona == 'j': #pārbauda vai persona ir students
                print('izdevumu saņem uz 15 dienām')
            else:
                print('izdevumu saņem uz 30 dienām')