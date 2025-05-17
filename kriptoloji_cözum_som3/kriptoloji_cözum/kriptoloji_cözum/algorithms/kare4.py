import math

# --- 1) Tanımlı Kareler (5×6 = 30 hücre)
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
    """Küçük harfe çevir, boşluk at, J→I yap, sıra bigramlara ayır."""
    txt = txt.lower().replace(' ', '')
    # Türk alfabesindeki yalnızca bu 30 karakteri al
    valid = set(flatten(alfabetikSolUst_kare))
    clean = [ch for ch in txt if ch in valid]
    # Tek harf kalırsa 'x' ekle
    if len(clean) % 2 == 1:
        clean.append('x')
    # İkişerli listeler
    return [clean[i:i+2] for i in range(0, len(clean), 2)]

def four_square_decrypt(cipher, cols):
    total = len(flatten(alfabetikSolUst_kare))
    rows = total // cols
    tl = build_rect(flatten(alfabetikSolUst_kare), rows, cols)
    br = build_rect(flatten(alfabetikSagAlt_kare), rows, cols)
    tr = build_rect(flatten(karisikSagUst_kare), rows, cols)
    bl = build_rect(flatten(karisikSolAlt_kare), rows, cols)

    plain = []
    # iki harfli bloklar
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c2 = find_pos(tr, a)
        r2, c1 = find_pos(bl, b)
        plain.append(tl[r1][c1])
        plain.append(br[r2][c2])
    return ''.join(plain)