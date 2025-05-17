import math

def rota_cozum(sifreli_metin, sutun):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

    # 1) Küçült, boşlukları at, sadece alfabe harfleri al
    temiz = ''.join(
        ch for ch in
        ('ı' if c == 'I' else c.lower() for c in sifreli_metin)
        if ch in turk_alfabe
    )
    toplam_harf = len(temiz)

    # 2) Satır sayısını hesapla
    satir = math.ceil(toplam_harf / sutun)

    # 3) Boş matrisi oluştur
    matris = [[None] * sutun for _ in range(satir)]

    # 4) Şifreleme kodundaki spiral adımlarıyla (sol alt → yukarı → sağ → aşağı → sol)
    top, bottom = 0, satir - 1
    left, right = 0, sutun - 1
    idx = 0

    while top <= bottom and left <= right:
        # a) Sol sütundan yukarı
        for i in range(bottom, top-1, -1):
            if idx < toplam_harf:
                matris[i][left] = temiz[idx]
                idx += 1
        left += 1

        # b) Üst satırdan sağa
        for j in range(left, right+1):
            if idx < toplam_harf:
                matris[top][j] = temiz[idx]
                idx += 1
        top += 1

        # c) Sağ sütundan aşağı
        if left <= right:
            for i in range(top, bottom+1):
                if idx < toplam_harf:
                    matris[i][right] = temiz[idx]
                    idx += 1
            right -= 1

        # d) Alt satırdan sola
        if top <= bottom:
            for j in range(right, left-1, -1):
                if idx < toplam_harf:
                    matris[bottom][j] = temiz[idx]
                    idx += 1
            bottom -= 1

    # 5) Matrisi satır satır oku, tüm None'ları at, sondaki 'x'leri sil
    cozulmus = ''.join(
        ch for row in matris for ch in row
        if ch is not None
    ).rstrip('x')

    return cozulmus

