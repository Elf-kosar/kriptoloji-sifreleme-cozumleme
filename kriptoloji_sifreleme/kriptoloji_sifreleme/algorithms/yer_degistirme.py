import math

def yer_degistirme_sifrele(metin, sutun_sayisi):
    # Türkçe küçük harfe dönüştürürken I harfini i'ye çevirmeden yap
    def turkce_kucult(yazi):
        return ''.join('ı' if ch == 'I' else 'i' if ch == 'İ' else ch.lower() for ch in yazi)

    # Sadece Türk alfabesindeki harfleri al
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    metin = ''.join([harf for harf in turkce_kucult(metin) if harf in turk_alfabe])

    # Gerekli satır sayısını hesapla
    toplam_harf = len(metin)
    satir_sayisi = math.ceil(toplam_harf / sutun_sayisi)

    # Eksikse 'x' ile tamamla
    while len(metin) < satir_sayisi * sutun_sayisi:
        metin += 'x'

    # Metni tabloya yerleştir (satır satır)
    tablo = []
    index = 0
    for _ in range(satir_sayisi):
        satir = []
        for _ in range(sutun_sayisi):
            satir.append(metin[index])
            index += 1
        tablo.append(satir)

    # Sütun sütun oku ve şifreli metni oluştur
    sifreli_metin = ''
    for sutun in range(sutun_sayisi):
        for satir in range(satir_sayisi):
            sifreli_metin += tablo[satir][sutun]

    return sifreli_metin

