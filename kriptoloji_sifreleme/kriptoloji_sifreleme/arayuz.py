import tkinter as tk
from tkinter import simpledialog, messagebox

# Şifreleme algoritmalarının tanımlandığı dosyalar
from algorithms.kaydirmali import kaydirma_sifrele
from algorithms.dogrusal import affine_sifrele
from algorithms.yerine_koyma import yerine_koyma_sifrele
from algorithms.permutasyon import permutasyon_sifrele
from algorithms.rota import rota_sifrele
from algorithms.zigzag import zigzag_sifrele
from algorithms.vigenere import vigenere_sifrele
from algorithms.kare4 import kare_cozum
from algorithms.hill import hill_sifrele
from algorithms.yer_degistirme import yer_degistirme_sifrele
import mail

# Şifreli metni geçici olarak saklayacak değişken
temp_sifreli_metin = ""


def algoritma_butonu_olustur(algoritma_adi, fonksiyon, renk):
    """Her algoritma için bir buton oluşturur"""
    button = tk.Button(pencere, text=algoritma_adi, width=30,height=2, command=fonksiyon, bg=renk)
    button.pack(pady=2)

def kaydirma_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar (Sayı):")
    if metin is not None and anahtar is not None:
        sonuc = kaydirma_sifrele(metin, anahtar)
        goster_sonuc(sonuc)

def yer_degistirme_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar (Sayı):")
    if metin is not None and anahtar is not None:
        sonuc = yer_degistirme_sifrele(metin, anahtar)
        goster_sonuc(sonuc)

def affine_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar (örnek: 5,8):")
    if metin and anahtar:
        try:
            a_str, b_str = anahtar.split(',')
            a = int(a_str.strip())
            b = int(b_str.strip())
            sonuc = affine_sifrele(metin, a, b)
            goster_sonuc(sonuc)
        except ValueError:
            messagebox.showerror("Hata", "Lütfen anahtarı doğru formatta girin. Örnek: 5,8")

def yerine_koyma_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    if metin:
        sonuc = yerine_koyma_sifrele(metin)
        goster_sonuc(sonuc)

def permutasyon_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar (sayı, örn: 312):")
    if metin and anahtar:
        try:
            sonuc = permutasyon_sifrele(metin, anahtar)
            goster_sonuc(sonuc)
        except ValueError as e:
            messagebox.showerror("Hata", str(e))

def rota_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    if not metin:
        return
    try:
        sutun = int(simpledialog.askstring("Giriş", "Matris sütun sayısı:"))
    except (ValueError, TypeError):
        messagebox.showerror("Hata", "Sütun sayısı geçerli bir sayı olmalıdır.")
        return
    sonuc = rota_sifrele(metin, sutun)
    goster_sonuc(sonuc)

def zigzag_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askinteger("Giriş", "Anahtar (Sayı):")
    if metin and anahtar is not None:
        sonuc = zigzag_sifrele(metin, anahtar)
        goster_sonuc(sonuc)

def vigenere_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar (Metin):")
    if metin and anahtar:
        sonuc = vigenere_sifrele(metin, anahtar)
        goster_sonuc(sonuc)

def kare4_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    if metin:
        anahtar = simpledialog.askinteger("Giriş", "anahtar:")
        sonuc = kare_cozum(metin, anahtar)
        goster_sonuc(sonuc)

def hill_btn():
    metin = simpledialog.askstring("Giriş", "Metni girin:")
    anahtar = simpledialog.askstring("Giriş", "Anahtar matrisi (örnek: 2 4,5 7):")
    if metin and anahtar:
        try:
            matrix = [[int(x) for x in row.split()] for row in anahtar.split(',')]
            sonuc = hill_sifrele(metin, matrix)
            goster_sonuc(sonuc)
        except Exception as e:
            messagebox.showerror("Hata", f"Anahtar matrisi hatalı: {e}")

def goster_sonuc(sifreli_metin):
    global temp_sifreli_metin
    temp_sifreli_metin = sifreli_metin
    sonuc_label.config(text=f"Şifreli Metin: {sifreli_metin}")

def mail_btn():
    global temp_sifreli_metin
    if not temp_sifreli_metin:
        messagebox.showwarning("Uyarı", "Önce bir şifreleme yapmalısınız.")
        return
    try:
        mail.send_email(subject="Şifreli Metniniz", body=temp_sifreli_metin)
        messagebox.showinfo("Başarılı", "Şifreli metin başarıyla e-posta ile gönderildi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Mail gönderilemedi: {e}")


# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Şifreleme Uygulaması")
pencere.geometry("400x650")  

# Başlık
baslik_label = tk.Label(pencere, text="Bir Şifreleme Algoritması Seçin:", font=("Arial", 14, "bold"))
baslik_label.pack(pady=20)

# Algoritma butonları
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

# Şifreli metin etiketi
sonuc_label = tk.Label(pencere, text="Şifreli Metin: ", font=("Arial", 12), bg="#F7D1D1")
sonuc_label.pack(pady=20)

# Mail Gönder butonu
mail_gonder_btn = tk.Button(pencere, text="Mail Gönder", width=15, command=mail_btn, bg="#00f5ff")
mail_gonder_btn.pack(pady=10)

# Uygulamayı başlat
pencere.mainloop()
