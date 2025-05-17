import math

def rota_sifrele(metin, sutun):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

    # Büyük 'I' harfini küçük 'ı' yap, diğerlerini küçült
    duzeltilmis_metin = ''
    for ch in metin:
        if ch == 'I':
            duzeltilmis_metin += 'ı'
        else:
            duzeltilmis_metin += ch.lower()

    # Boşlukları ve alfabe dışı karakterleri kaldır
    duzeltilmis_metin = ''.join([ch for ch in duzeltilmis_metin if ch in turk_alfabe])

    toplam_harf = len(duzeltilmis_metin)
    satir = math.ceil(toplam_harf / sutun)
    gerekli_karakter_sayisi = satir * sutun

    # Eksik karakterleri 'x' ile tamamla
    while len(duzeltilmis_metin) < gerekli_karakter_sayisi:
        duzeltilmis_metin += 'x'

    # Matrisi oluştur (satır satır doldur)
    matris = []
    index = 0
    for _ in range(satir):
        satir_verisi = []
        for _ in range(sutun):
            satir_verisi.append(duzeltilmis_metin[index])
            index += 1
        matris.append(satir_verisi)

    # Spiral sırayla oku (sol alt köşeden başlayarak yukarı → sağ → aşağı → sol)
    spiral = []
    top, bottom = 0, satir - 1
    left, right = 0, sutun - 1

    while top <= bottom and left <= right:
        for i in range(bottom, top - 1, -1):
            spiral.append(matris[i][left])
        left += 1

        for i in range(left, right + 1):
            spiral.append(matris[top][i])
        top += 1

        if left <= right:
            for i in range(top, bottom + 1):
                spiral.append(matris[i][right])
            right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral.append(matris[bottom][i])
            bottom -= 1

    return ''.join(spiral)