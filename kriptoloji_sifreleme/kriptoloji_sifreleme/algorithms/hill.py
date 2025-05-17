import numpy as np

def hill_sifrele(metin, anahtar):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_boyu = len(turk_alfabe)

    # Türkçeye özel küçük harf dönüşümü
    def kucuk_harf_cevir(harf):
        cevir = {
            'I': 'ı',
            'İ': 'i',
        }
        if harf in cevir:
            return cevir[harf]
        else:
            return harf.lower()

    def harf_to_sayi(harf):
        harf = kucuk_harf_cevir(harf)
        if harf in turk_alfabe:
            return turk_alfabe.index(harf)
        else:
            raise ValueError(f"'{harf}' harfi alfabede bulunamadı.")

    def sayi_to_harf(sayi):
        return turk_alfabe[sayi % alfabe_boyu]

    # Temizleme işlemi
    temiz_metin = ''.join(
        kucuk_harf_cevir(harf)
        for harf in metin
        if kucuk_harf_cevir(harf) in turk_alfabe
    )

    try:
        metin_sayilari = [harf_to_sayi(harf) for harf in temiz_metin]
    except ValueError as e:
        return str(e)

    grup_boyutu = len(anahtar)
    gruplar = [metin_sayilari[i:i + grup_boyutu] for i in range(0, len(metin_sayilari), grup_boyutu)]

    sifreli_metin = ""
    for grup in gruplar:
        if len(grup) < grup_boyutu:
            grup += [0] * (grup_boyutu - len(grup))

        sifreli_grup = np.dot(np.array(anahtar), grup) % alfabe_boyu
        sifreli_metin += ''.join(sayi_to_harf(int(sayi)) for sayi in sifreli_grup)

    return sifreli_metin

