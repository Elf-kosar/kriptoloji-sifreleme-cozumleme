import tkinter as tk
from tkinter import simpledialog, messagebox

# Şifreleme algoritmalarının tanımlandığı dosyalar
from algorithms.kaydirmali import kaydirma_coz
from algorithms.dogrusal import affine_cozme
from algorithms.yerine_koyma import yerine_koyma_cozme
from algorithms.permutasyon import permutasyon_cozme
from algorithms.rota import rota_cozum
from algorithms.zigzag import zigzag_cozme
from algorithms.vigenere import vigenere_cozme
from algorithms.kare4 import four_square_decrypt
from algorithms.hill import hill_cozme
from algorithms.yer_degistirme import yer_degistirme_coz



def algoritma_butonu_olustur(algoritma_adi, fonksiyon, renk):
    """Her algoritma için bir buton oluşturur"""
    button = tk.Button(pencere, text=algoritma_adi,  width=30,height=2, command=fonksiyon, bg=renk)
    button.pack(pady=2)
    


def kaydirma_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar (Sayı):")
    if metin is not None and anahtar is not None:
        sonuc = kaydirma_coz(metin, anahtar)
        goster_sonuc(sonuc)

def yer_degistirme_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar (Sayı):")
    if metin is not None and anahtar is not None:
        sonuc = yer_degistirme_coz(metin, anahtar)
        goster_sonuc(sonuc)


def affine_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar (örnek: 5,8):")
    if metin and anahtar:
        try:
            a_str, b_str = anahtar.split(',')
            a = int(a_str.strip())
            b = int(b_str.strip())
            sonuc = affine_cozme(metin, a, b)
            goster_sonuc(sonuc)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen anahtarı doğru formatta girin. Örnek: 5,8")



def yerine_koyma_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    if metin:
        sonuc = yerine_koyma_cozme(metin)
        goster_sonuc(sonuc)


def permutasyon_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar ([2 4 1 3]):")
    if metin and anahtar:
        sonuc = permutasyon_cozme(metin, anahtar)
        goster_sonuc(sonuc)


def rota_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    if not metin:
        return

    try:
        sutun = int(simpledialog.askstring("Giriş", "Matris sütun sayısı:"))
    except (ValueError, TypeError):
        messagebox.showerror("Hata", "Satır ve sütun sayıları geçerli birer sayı olmalıdır.")
        return

    sonuc = rota_cozum(metin, sutun)
    goster_sonuc(sonuc)



def zigzag_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar (Sayı):")
    if metin and anahtar is not None:
        sonuc = zigzag_cozme(metin, anahtar)
        goster_sonuc(sonuc)


def vigenere_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar (Metin):")
    if metin and anahtar:
        sonuc = vigenere_cozme(metin, anahtar)
        goster_sonuc(sonuc)

def kare4_btn():
    metin = simpledialog.askstring("Giriş", "Şifreli metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar(sütun sayısı):")
    
    if metin and anahtar:
        sonuc = four_square_decrypt(metin , anahtar)
        goster_sonuc(sonuc)



def hill_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar matrisi:")
    if metin and anahtar:
        try:
            # Anahtar matrisini uygun şekilde parçalayıp int türüne çeviriyoruz
            matrix = [[int(x) for x in row.split()] for row in anahtar.split(',')]
            sonuc = hill_cozme(metin, matrix)  # Hill çözme fonksiyonunu çağırıyoruz
            goster_sonuc(sonuc)
        except Exception as e:
            messagebox.showerror("Hata", f"Anahtar matrisi hatalı: {e}")


def goster_sonuc(sifreli_metin):
    sonuc_label.config(text=f"çözülmüş Metin: {sifreli_metin}")


# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Çözüm Uygulaması")
pencere.geometry("400x650")

# Başlık
baslik_label = tk.Label(pencere, text="Bir Çözüm Algoritması Seçin:", font=("Arial", 14, "bold"))
baslik_label.pack(pady=20)

# Her algoritma için butonlar
# Her algoritma için butonlar ve farklı renkler
algoritma_butonu_olustur("Kaydırmalı Şifreleme", kaydirma_btn, "#b0e2ff")
algoritma_butonu_olustur("Doğrusal Affine", affine_btn, "#b4eeb4")
algoritma_butonu_olustur("Yerine Koyma", yerine_koyma_btn, "#ffc000")
algoritma_butonu_olustur("Permütasyon", permutasyon_btn, "#F7D1D1")
algoritma_butonu_olustur("Rota", rota_btn, "#B497BD")
algoritma_butonu_olustur("Zigzag", zigzag_btn, "#FF4040")
algoritma_butonu_olustur("Vigenère", vigenere_btn, "#FFB5C5")
algoritma_butonu_olustur("4 Kare", kare4_btn, "#EEAEEE")
algoritma_butonu_olustur("Hill", hill_btn, "#FFE1FF")
algoritma_butonu_olustur("Yer Değiştirme", yer_degistirme_btn, "#FF7F24")

# Sonuç etiketi
sonuc_label = tk.Label(pencere, text="Çözülmüş Metin: ", font=("Arial", 12), bg="#F7D1D1")
sonuc_label.pack(pady=20)

# Pencereyi başlat
pencere.mainloop()
