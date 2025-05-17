def vigenere_cozme(sifreli_metin, anahtar):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_uzunluk = len(turk_alfabe)

    sifreli_metin = sifreli_metin.lower().replace(" ", "")
    anahtar = anahtar.lower().replace(" ", "")

    cozulmus_metin = ""
    anahtar_index = 0

    for harf in sifreli_metin:
        if harf in turk_alfabe:
            sifreli_index = turk_alfabe.index(harf)
            anahtar_harf = anahtar[anahtar_index % len(anahtar)]
            anahtar_indexi = turk_alfabe.index(anahtar_harf)

            orijinal_index = (sifreli_index - anahtar_indexi) % alfabe_uzunluk
            cozulmus_metin += turk_alfabe[orijinal_index]

            anahtar_index += 1
        else:
            cozulmus_metin += harf

    return cozulmus_metin
