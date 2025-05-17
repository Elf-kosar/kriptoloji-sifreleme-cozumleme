def turkce_kucult(yazi):
    return ''.join('ı' if ch == 'I' else 'i' if ch == 'İ' else ch.lower() for ch in yazi)

def zigzag_sifrele(metin, anahtar):
    # Türk alfabesi
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

    # Metni Türkçeye uygun şekilde küçük harfe çevir ve sadece alfabe harflerini al
    metin = ''.join([harf for harf in turkce_kucult(metin) if harf in turk_alfabe])
    
    if anahtar == 1:  # Anahtar 1 ise metin değişmez
        return metin
    
    # Zigzag dizisi için gerekli satırları oluştur
    satirlar = ['' for _ in range(anahtar)]
    satir = 0
    yon = 1  # 1: aşağı, -1: yukarı
    
    # Metni zigzag desenine yerleştir
    for harf in metin:
        satirlar[satir] += harf
        if satir == 0:
            yon = 1
        elif satir == anahtar - 1:
            yon = -1
        satir += yon
    
    # Zigzag düzenindeki harfleri satır satır birleştir
    sifreli_metin = ''.join(satirlar)
    return sifreli_metin
