def vigenere_sifrele(metin, anahtar):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_uzunluk = len(turk_alfabe)

    # Türkçe'ye özel küçük harfe dönüştürme
    def turkce_kucult(yazi):
        return ''.join('ı' if ch == 'I' else 'i' if ch == 'İ' else ch.lower() for ch in yazi)

    metin = turkce_kucult(metin).replace(" ", "")
    anahtar = turkce_kucult(anahtar).replace(" ", "")

    sifreli_metin = ""
    anahtar_index = 0

    for harf in metin:
        if harf in turk_alfabe:
            metin_index = turk_alfabe.index(harf)
            anahtar_harf = anahtar[anahtar_index % len(anahtar)]
            anahtar_indexi = turk_alfabe.index(anahtar_harf)

            yeni_index = (metin_index + anahtar_indexi) % alfabe_uzunluk
            sifreli_metin += turk_alfabe[yeni_index]

            anahtar_index += 1
        else:
            sifreli_metin += harf  # alfabe dışı karakterleri değiştirme

    return sifreli_metin
