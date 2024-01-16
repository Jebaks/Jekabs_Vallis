def materialuAprekins(garums_fn, platums_fn, augstums_fn, skaits_fn, biezums_fn):
    izmers = (garums_fn * platums_fn * augstums_fn)/1000000 #izrēķina podesta izmēru kubikmetros
    materiali = (garums_fn * augstums_fn * 2 + platums_fn * augstums_fn * 2 + garums_fn * platums_fn * 2) * skaits_fn #aprēķina cik kvadrātcentimetrus finiera vajadzēs lai izveidotu pasūtītos podestus
    profili_gar = (garums_fn*4+platums_fn*4+augstums_fn*4)*skaits_fn
    savienojumi = 8 * skaits_fn
    if biezums_fn == 12:
        cena = 18.36
    if biezums_fn == 15:
        cena = 20.84
    if biezums_fn == 18:
        cena = 23.92
    if biezums_fn == 21:
        cena = 27.52
    cena_finierim = round((materiali / 10000) * cena,2) #finiera cena uz kvadrātmetriem
    cena_profiliem = round(profili_gar / 100 * 0.9,2)
    cena_savienojumiem = round(savienojumi * 0.8,2)
    cena_kopa = cena_finierim + cena_profiliem + cena_savienojumiem
    if skaits == 1:
        print(izmers,'m3 lielam podestam, Jums nepieciešms:\n', materiali, 'cm2 finiera\n', profili_gar, 'cm profilu\n', savienojumi, 'stūra savienojumi')
    else:
        print(skaits,'x',izmers,'m3 lieliem podestiem, Jums nepieciešms:\n', materiali, 'cm2 finiera\n', profili_gar, 'profili\n', savienojumi, 'stūra savienojumi')
    print('Izmaksas:\n', materiali, 'cm2 finiera maksā:', cena_finierim,'Eur\n', profili_gar, 'cm profili maksā:',cena_profiliem,'Eur\n', savienojumi, 'stūra savienojumi maksā:',cena_savienojumiem,'Eur\nKopā:',cena_kopa,'Eur')
print('Ievadiet podesta garumu(cm), platumu(cm), augstumu(cm), skaitu un finiera biezumu(12mm, 15mm, 18mm, 21mm), tādā secībā, kā norādīts, pēc katra nospiežot Enter taustiņu:')
garums, platums, augstums, skaits, biezums = float(input()), float(input()), float(input()), int(input()), int(input()) #lietotājs ievada katru mērījumu, kas nepieciešams lai izrēķinātu nepieciešamo materiālu daudzumu
materialuAprekins(garums, platums, augstums, skaits, biezums) #lietotājs ievada katru mērījumu, kas nepieciešams lai izrēķinātu nepieciešamo materiālu daudzumu