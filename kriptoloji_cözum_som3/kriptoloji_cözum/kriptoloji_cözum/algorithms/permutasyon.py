def permutasyon_cozme(sifreli_metin, anahtar_str):
    """
    Permütasyon şifrelemesi ile elde edilmiş metni çözer.
    - sifreli_metin: şifrelenmiş metin (sadece Türk alfabesinden harfler + 'x' dolgu)
    - anahtar_str: kullanıcıdan alınan "3 1 2" gibi boşluklu permütasyon anahtarı
    """
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_seti = set(turk_alfabe)

    # 1) Anahtarı parse et
    try:
        anahtar = [int(x) for x in anahtar_str.strip().split()]
    except ValueError:
        raise ValueError("Anahtar yalnızca sayılardan oluşmalıdır. Örnek: 3 1 2")

    blok_boyu = len(anahtar)
    # Geçerli aralıkta mı?
    if any(i < 1 or i > blok_boyu for i in anahtar):
        raise ValueError(f"Anahtar değerleri 1 ile {blok_boyu} arasında olmalıdır.")

    # 0-based permütasyon indeksi
    anahtar_idx = [k-1 for k in anahtar]

    # 2) İnvers permütasyonu hesapla
    #    anahtar_idx[i] = j  =>  inv_perm[j] = i
    inv_perm = [0] * blok_boyu
    for i, j in enumerate(anahtar_idx):
        inv_perm[j] = i

    # 3) Şifreli metni filtrele (yalnızca alfabe ve 'x')
    metin = sifreli_metin.lower()
    temiz = [ch for ch in metin if ch in alfabe_seti or ch == 'x']

    # 4) Blok blok çöz
    cozulmus = []
    for i in range(0, len(temiz), blok_boyu):
        blok = temiz[i:i+blok_boyu]
        # eksik blok olması pek beklenmez, ama doldurma karakteriyle
        if len(blok) < blok_boyu:
            blok += ['x'] * (blok_boyu - len(blok))

        # her orijinal pozisyona, şifreli bloktaki inv_perm[pos] karakteri gelir
        orig = [''] * blok_boyu
        for pos in range(blok_boyu):
            orig[pos] = blok[inv_perm[pos]]
        cozulmus.extend(orig)

    # İstersen sondaki dolgu 'x'leri kırpmak mümkün:
    # while cozulmus and cozulmus[-1] == 'x':
    #     cozulmus.pop()

    return ''.join(cozulmus)
