import math

alfabetikSolUst_kare = [
    ['a','b','c','ç','d','e'],
    ['f','g','ğ','h','ı','i'],
    ['j','k','l','m','n','o'],
    ['ö','p','r','s','ş','t'],
    ['u','ü','v','y','z','x']
]
alfabetikSagAlt_kare = [
    ['a','b','c','ç','d','e'],
    ['f','g','ğ','h','ı','i'],
    ['j','k','l','m','n','o'],
    ['ö','p','r','s','ş','t'],
    ['u','ü','v','y','z','x']
]
karisikSagUst_kare = [
    ['j','ö','x','t','y','z'],
    ['v','d','o','l','ş','ç'],
    ['g','ü','b','i','k','r'],
    ['u','f','h','s','a','ğ'],
    ['c','p','m','ı','n','e']
]
karisikSolAlt_kare = [
    ['d','g','o','e','t','n'],
    ['j','p','ç','l','ü','ı'],
    ['a','ş','v','f','s','c'],
    ['u','h','x','z','ğ','m'],
    ['r','i','ö','b','y','k']
]

# --- 2) Yardımcı Fonksiyonlar

def flatten(mat):
    """Matrisi satır-satır dümdüz listeye dönüştür."""
    return [ch for row in mat for ch in row]

def build_rect(flat_list, rows, cols):
    """Düz listeyi rows×cols matrisine çevir."""
    if len(flat_list) != rows * cols:
        raise ValueError(f"Alfabe boyu {len(flat_list)} ≠ rows*cols ({rows}×{cols})")
    return [flat_list[i*cols:(i+1)*cols] for i in range(rows)]

def find_pos(mat, ch):
    """mat içindeki karakterin (satır,sütun) koordinatını döner."""
    for r, row in enumerate(mat):
        for c, v in enumerate(row):
            if v == ch:
                return r, c
    raise ValueError(f"Karakter bulunamadı: {ch}")

def prepare_text(txt):
    """Küçük harfe çevir, boşluk at, J→I yapma, I→ı yap, sıra bigramlara ayır."""
    txt = txt.replace(' ', '')  # boşlukları kaldır
    new_txt = ''
    for ch in txt:
        if ch == 'I':
            new_txt += 'ı'  # Türkçe 'I' harfi küçük 'ı' olmalı
        else:
            new_txt += ch.lower()

    valid = set(flatten(alfabetikSolUst_kare))
    clean = [ch for ch in new_txt if ch in valid]

    if len(clean) % 2 == 1:
        clean.append('x')

    return [clean[i:i+2] for i in range(0, len(clean), 2)]



def kare_cozum(plain, cols):
    # otomatik satır sayısı
    total = len(flatten(alfabetikSolUst_kare))
    rows = total // cols
    # matrisleri yeniden boyutla
    tl = build_rect(flatten(alfabetikSolUst_kare), rows, cols)
    br = build_rect(flatten(alfabetikSagAlt_kare), rows, cols)
    tr = build_rect(flatten(karisikSagUst_kare), rows, cols)
    bl = build_rect(flatten(karisikSolAlt_kare), rows, cols)

    cipher = []
    for a, b in prepare_text(plain):
        r1, c1 = find_pos(tl, a)
        r2, c2 = find_pos(br, b)
        cipher.append(tr[r1][c2])
        cipher.append(bl[r2][c1])
    return ''.join(cipher)
