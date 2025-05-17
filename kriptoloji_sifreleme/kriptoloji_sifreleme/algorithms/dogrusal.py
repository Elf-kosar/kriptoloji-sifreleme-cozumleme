kucuk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
alfabe_uzunlugu = len(kucuk_alfabe)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def affine_sifrele(metin, a, b):
    if gcd(a, alfabe_uzunlugu) != 1:
        raise ValueError("a anahtarı ile alfabe uzunluğu ({}) aralarında asal olmalı.".format(alfabe_uzunlugu))

    sifreli_metin = ""

    for harf in metin:
        # 'I' harfi büyükse küçük 'ı' yap (çünkü Türkçede 'I' → 'ı')
        if harf == 'I':
            harf = 'ı'
        else:
            harf = harf.lower()

        if harf in kucuk_alfabe:
            index = kucuk_alfabe.index(harf)
            yeni_index = (a * index + b) % alfabe_uzunlugu
            sifreli_metin += kucuk_alfabe[yeni_index]
        else:
            pass  # Alfabe dışındaki karakterleri at

    return sifreli_metin
