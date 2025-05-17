def kaydirma_coz(sifreli_metin, anahtar):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_boyu = len(turk_alfabe)
    
    # 1) Tüm harfleri küçült ve boşlukları kaldır
    sifreli_metin = sifreli_metin.lower().replace(" ", "")
    
    cozum = ""
    for harf in sifreli_metin:
        if harf in turk_alfabe:
            index = turk_alfabe.index(harf)
            yeni_index = (index - anahtar) % alfabe_boyu
            cozum += turk_alfabe[yeni_index]
        else:
            cozum += harf  # Alfabe dışı karakterler (nokta, virgül vb.) olduğu gibi kalır

    return cozum
