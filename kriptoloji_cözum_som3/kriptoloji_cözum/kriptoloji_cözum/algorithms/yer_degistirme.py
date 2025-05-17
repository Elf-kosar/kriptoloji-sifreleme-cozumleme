import math

def turkce_kucult(yazi: str) -> str:
    """Türkçeye özel küçültme: I→ı, İ→i, diğerleri .lower()."""
    out = []
    for ch in yazi:
        if ch == 'I':
            out.append('ı')
        elif ch == 'İ':
            out.append('i')
        else:
            out.append(ch.lower())
    return ''.join(out)

def yer_degistirme_coz(sifreli: str, sutun_sayisi: int) -> str:
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    # 1) Küçült, filtrele (x'ler dahil)
    temiz = ''.join(ch for ch in turkce_kucult(sifreli) 
                    if ch in turk_alfabe + 'x')
    # 2) Satır sayısı
    satir = math.ceil(len(temiz) / sutun_sayisi)
    # 3) Boş tablo
    matris = [['']*sutun_sayisi for _ in range(satir)]
    # 4) Sütun sütun doldur
    idx = 0
    for c in range(sutun_sayisi):
        for r in range(satir):
            if idx < len(temiz):
                matris[r][c] = temiz[idx]
                idx += 1
    # 5) Satır satır oku + sondaki x'leri at
    orj = ''.join(matris[r][c] for r in range(satir) for c in range(sutun_sayisi))
    return orj.rstrip('x')

