import numpy as np
from tkinter import simpledialog, messagebox

def hill_cozme(sifreli, anahtar):
    turk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    alfabe_boyu = len(turk_alfabe)

    def kucuk_harf_cevir(harf):
        cevir = {'I': 'ı', 'İ': 'i'}
        return cevir.get(harf, harf.lower())

    def harf_to_sayi(harf):
        harf = kucuk_harf_cevir(harf)
        if harf in turk_alfabe:
            return turk_alfabe.index(harf)
        else:
            raise ValueError(f"'{harf}' harfi alfabede yok.")

    def sayi_to_harf(sayi):
        return turk_alfabe[sayi % alfabe_boyu]

    def mod_inverse(a, m):
        # Modüler tersini bulan fonksiyon
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError(f"{a} mod {m} tersini bulamıyorum.")

    def matris_ters_mod(matrix, mod):
        # Anahtar matrisinin tersi modüler hesaplanır
        det = int(round(np.linalg.det(matrix)))  # Determinan hesaplanıyor
        det_mod = det % mod  # Determinan mod alınarak 0-25 arası dönüştürülür
        if det_mod == 0:
            raise ValueError("Anahtar matrisinin determinanı 0 olamaz.")
        det_inv = mod_inverse(det_mod, mod)  # Determinanın modüler tersi bulunur

        matrix_mod = np.array(matrix)
        adjugate = np.round(det * np.linalg.inv(matrix_mod)).astype(int) % mod  # Adjugate matrisini buluyoruz

        return (det_inv * adjugate) % mod  # Anahtar matrisinin tersini döndürüyoruz

    # Metni sayılara çevir
    temiz = ''.join(
        kucuk_harf_cevir(harf)
        for harf in sifreli
        if kucuk_harf_cevir(harf) in turk_alfabe
    )

    try:
        sayilar = [harf_to_sayi(h) for h in temiz]
    except ValueError as e:
        print(str(e))
        return

    # Gruplama ve ters anahtar
    boyut = len(anahtar)
    gruplar = [sayilar[i:i+boyut] for i in range(0, len(sayilar), boyut)]

    # Anahtar matrisinin tersini al
    try:
        anahtar_ters = matris_ters_mod(anahtar, alfabe_boyu)
    except ValueError as e:
        print(f"Anahtar hatalı: {e}")
        return

    cozum = ""
    for grup in gruplar:
        if len(grup) < boyut:
            grup += [0] * (boyut - len(grup))  # Eğer son grup eksikse sıfırlarla tamamlanır
        sonuc = np.dot(anahtar_ters, grup) % alfabe_boyu  # Ters anahtar ile şifre çözme
        sonuc = np.array(sonuc).flatten()  # Yalnızca tek bir satır haline getirilir
        cozum += ''.join(sayi_to_harf(int(s)) for s in sonuc)

    return cozum





