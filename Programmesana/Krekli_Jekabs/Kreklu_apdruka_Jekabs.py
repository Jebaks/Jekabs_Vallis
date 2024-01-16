apdruka_d = {'TEKSTS':5,'ZIME':7,'FOTO':20} #Vārdnīca ar apdrukas izvēles veidiem
def pasuti_tkreklus(skaits, apdruka, piegade): #funkcija, kurā tiek aprēķinātas pasūtījuma izmaksas
  izmaksa_krekli = int(skaits) * int(apdruka_d[apdruka])
  if izmaksa_krekli > 100: #pārbauda vai pircējam var piemērot atlaidi
    izmaksa_kopa = round(izmaksa_krekli - izmaksa_krekli/20,2)
  elif izmaksa_krekli > 50:
    izmaksa_kopa = izmaksa_krekli
  else: #pārbauda vai pircējam var piemērot bezmaksas piegādi
    if piegade == 'j': #pārbauda vai pircējs vēlas piegādi
      izmaksa_kopa = izmaksa_krekli + 15
    else:
      izmaksa_kopa = izmaksa_krekli
  print('Par',skaits,'krekliem ar',apdruka,'apdruku Jums jāmaksā',izmaksa_kopa,'Eur')
while True: #cikls, kur atgriezties, kad ievadīti nepareizi dati
  skaits = input('Ievadiet kreklu daudzumu:\n')
  if skaits.isdigit():
    break #pārtrauc ciklu, jo lietotājs ievadījis vēlamos datus
  else:
    print('Jūs ievadījāt nepareizus datus. Mēģiniet vēlreiz!\n')
    continue #atgriež uz cikla sākumu, ja lietotājs ir ievadījis nepareizus datus
while True: #cikls, kur atgriezties, kad ievadīti nepareizi dati
  apdruka_izveleta = input('Ievadiet apdrukas veidu(TEKSTS, ZIME, FOTO):\n')
  if apdruka_izveleta.upper() in apdruka_d:
    break #pārtrauc ciklu, jo lietotājs ievadījis vēlamos datus
  else:
    print('Jūs ievadījāt nepareizus datus. Mēģiniet vēlreiz!\n')
    continue #atgriež uz cikla sākumu, ja lietotājs ir ievadījis nepareizus datus
if int(skaits) * int(apdruka_d[apdruka_izveleta.upper()]) < 50:
  while True: #cikls, kur atgriezties, kad ievadīti nepareizi dati
    piegade = input('Vai Jūs vēlaties lai kreklus jums piegādā uz mājām?(j/n)\n').lower()
    if piegade == 'j':
      break #pārtrauc ciklu, jo lietotājs ievadījis vēlamos datus
    elif piegade == 'n':
      break #pārtrauc ciklu, jo lietotājs ievadījis vēlamos datus
    else:
      print('Jūs ievadījāt nepareizus datus. Mēģiniet vēlreiz!\n')
      continue #pārtrauc ciklu, jo lietotājs ievadījis vēlamos datus
else:
  piegade = 'n'
pasuti_tkreklus(skaits, apdruka_izveleta.upper(), piegade) #izsauc funkciju, kurā ievieto no lietotāja iegūtos datus