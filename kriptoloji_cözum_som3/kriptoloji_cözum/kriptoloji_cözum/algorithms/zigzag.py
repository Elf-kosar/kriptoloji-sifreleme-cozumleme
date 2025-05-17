def zigzag_cozme(sifreli_metin, anahtar):

    # Anahtar 1 ise şifreli metin olduğu gibi döner
    if anahtar <= 1:
        return sifreli_metin

    # 1) Her pozisyonun hangi raile ait olduğunu belirleyecek pattern
    pattern = []
    rail = 0
    direction = 1  # 1: aşağı, -1: yukarı
    for _ in range(len(sifreli_metin)):
        pattern.append(rail)
        rail += direction
        if rail == 0 or rail == anahtar - 1:
            direction *= -1

    # 2) Her rail'de kaç karakter var, bunu pattern'den say
    counts = [pattern.count(r) for r in range(anahtar)]

    # 3) Şifreli metni bu sayılara göre rail dizilerine böl
    rails_list = []
    idx = 0
    for c in counts:
        rails_list.append(list(sifreli_metin[idx: idx + c]))
        idx += c

    # 4) pattern sırasına göre sırayla rail'lerden karakterleri çekerek
    #    orijinal metni yeniden oluştur
    rail_indices = [0] * anahtar
    sonuc = []
    for r in pattern:
        sonuc.append(rails_list[r][rail_indices[r]])
        rail_indices[r] += 1

    return "".join(sonuc)