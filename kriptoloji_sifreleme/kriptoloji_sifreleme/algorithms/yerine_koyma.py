# Türk alfabesi
TURK_ALFABESI = list("abcçdefgğhıijklmnoöprsştuüvyz")

# Sabit şifreli alfabe (anahtar)
SIFRELI_ALFABE = list("yçöelşğhıaznvübgtjmpsdkorfciu")

# Anahtar sözlüğü oluştur
ANAHTAR = dict(zip(TURK_ALFABESI, SIFRELI_ALFABE))

# Türkçeye uygun küçük harfe çevirme fonksiyonu
def turkce_kucult(yazi):
    return ''.join('ı' if ch == 'I' else 'i' if ch == 'İ' else ch.lower() for ch in yazi)

def yerine_koyma_sifrele(metin):
    metin = turkce_kucult(metin).replace(" ", "")  # Türkçe küçük harfe çevir ve boşlukları kaldır
    sifreli = ""
    for harf in metin:
        if harf in ANAHTAR:  # Eğer harf alfabede varsa, şifrele
            sifreli += ANAHTAR[harf]
        else:
            sifreli += harf  # Alfabe dışı karakterleri olduğu gibi bırak
    return sifreli
