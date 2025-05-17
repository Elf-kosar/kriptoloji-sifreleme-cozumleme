def affine_cozme(sifreli_metin, a, b):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

    m = len(alfabe)
    a_inverse = mod_inverse(a, m)
    if a_inverse is None:
        return "Geçersiz anahtar: a ve alfabe boyutu aralarında asal değil."

    cozulmus_metin = ""

    for harf in sifreli_metin:
        if harf in alfabe:
            x = alfabe.index(harf)
            yeni_indeks = (a_inverse * (x - b)) % m
            cozulmus_metin += alfabe[yeni_indeks]
        else:
            # Alfabe dışındaki karakterleri at
            pass

    return cozulmus_metin