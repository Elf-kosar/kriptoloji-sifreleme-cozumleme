# Türk alfabesi
TURK_ALFABESI = list("abcçdefgğhıijklmnoöprsştuüvyz")

# Sabit şifreli alfabe (anahtar)
SIFRELI_ALFABE = list("yçöelşğhıaznvübgtjmpsdkorfciu")

# Ters anahtar (çözüm için)
TERS_ANAHTAR = dict(zip(SIFRELI_ALFABE, TURK_ALFABESI))

def yerine_koyma_cozme(sifreli_metin):
    sifreli_metin = sifreli_metin.lower().replace(" ", "")
    cozum = ""
    for harf in sifreli_metin:
        if harf in TERS_ANAHTAR:
            cozum += TERS_ANAHTAR[harf]
        else:
            cozum += harf
    return cozum