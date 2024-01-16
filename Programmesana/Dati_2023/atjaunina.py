import csv

# Faila nosaukumi
sakotnejie_dati_fails = 'sakotnejie_dati.csv'
jaunie_dati_fails = 'jaunie_dati.csv'

# Mēģina atvērt sākotnējo failu un lasa datus
try:
    with open(sakotnejie_dati_fails, 'r', newline='') as sakotnejie_fails:
        lasitajs = csv.DictReader(sakotnejie_fails)
        sakotnejie_dati = list(lasitajs)

        # Atjauno datus
        for persona in sakotnejie_dati:
            persona['Age'] = int(persona['Age']) + 1  # Piemēram, palielinam vecumu par 1

    # Ieraksta jaunus datus jaunā failā
    with open(jaunie_dati_fails, 'w', newline='') as jaunie_fails:
        rakstitajs = csv.DictWriter(jaunie_fails, fieldnames=['Name', 'Lastname', 'Age'])
        rakstitajs.writeheader()
        rakstitajs.writerows(sakotnejie_dati)

    print(f"Dati ir atjaunināti un saglabāti failā '{jaunie_dati_fails}'.")

except FileNotFoundError:
    print(f"Kļūda: Fails '{sakotnejie_dati_fails}' nav atrasts.")
except Exception as e:
    print(f"Kļūda: Neparedzēta kļūda - {e}")