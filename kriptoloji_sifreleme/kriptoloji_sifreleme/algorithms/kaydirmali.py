def kaydirma_sifrele(metin, anahtar):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_boyu = len(turk_alfabe)

    def harf_to_sayi(harf):
        return turk_alfabe.index(harf)

    def sayi_to_harf(sayi):
        return turk_alfabe[sayi % alfabe_boyu]

    # Büyük 'I' harfini küçük 'ı' yap, diğer harfleri normal küçült
    duzeltilmis_metin = ''
    for ch in metin:
        if ch == 'I':
            duzeltilmis_metin += 'ı'
        else:
            duzeltilmis_metin += ch.lower()

    # Boşlukları kaldır
    duzeltilmis_metin = duzeltilmis_metin.replace(" ", "")

    sifreli_metin = ""
    for harf in duzeltilmis_metin:
        if harf in turk_alfabe:
            sayi = harf_to_sayi(harf)
            sifreli_metin += sayi_to_harf(sayi + anahtar)
        else:
            # Alfabe dışı karakterler (ör. noktalama) olduğu gibi kalır
            sifreli_metin += harf

    return sifreli_metin
