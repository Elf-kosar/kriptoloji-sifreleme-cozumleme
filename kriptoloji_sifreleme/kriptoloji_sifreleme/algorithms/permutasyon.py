def permutasyon_sifrele(metin, anahtar_str):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_seti = set(turk_alfabe)

    # Büyük 'I' harfini küçük 'ı' yap, diğer harfleri normal küçült
    duzeltilmis_metin = ''
    for ch in metin:
        if ch == 'I':
            duzeltilmis_metin += 'ı'
        else:
            duzeltilmis_metin += ch.lower()

    # Anahtarı string'den integer listeye çevir
    try:
        anahtar = [int(x) for x in anahtar_str.strip().split()]
    except ValueError:
        raise ValueError("Anahtar yalnızca sayılardan oluşmalıdır. Örnek: 3 1 2")

    blok_boyu = len(anahtar)

    # Anahtar değerlerinin geçerli olup olmadığını kontrol et
    if any(i < 1 or i > blok_boyu for i in anahtar):
        raise ValueError(f"Anahtar değerleri 1 ile {blok_boyu} arasında olmalıdır.")

    anahtar_indeksli = [i - 1 for i in anahtar]  # 1-based to 0-based

    # Metni filtrele
    temiz_metin = ''.join([harf for harf in duzeltilmis_metin if harf in alfabe_seti])

    # Metni bloklara böl
    bloklar = [temiz_metin[i:i+blok_boyu] for i in range(0, len(temiz_metin), blok_boyu)]

    sifreli = ""
    for blok in bloklar:
        if len(blok) < blok_boyu:
            blok += "x" * (blok_boyu - len(blok))  # Eksik blokları tamamla
        yeni_blok = [''] * blok_boyu
        for i, pozisyon in enumerate(anahtar_indeksli):
            yeni_blok[i] = blok[pozisyon]
        sifreli += ''.join(yeni_blok)

    return sifreli
