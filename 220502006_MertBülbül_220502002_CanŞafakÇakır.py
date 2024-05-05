#Bu kod Mert Bülbül ve Can Şafak Çakır tarafından hazırlanmıştır
import tkinter as tk
from tkinter import messagebox
import sqlite3

class GemiVeritabani:
    def __init__(self):
        self.baglanti = sqlite3.connect("gemiler.db")
        self.cursor = self.baglanti.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS gemiler (
                                id INTEGER PRIMARY KEY,
                                tip TEXT,
                                seri_no TEXT,
                                ad TEXT,
                                agirlik REAL,
                                yapim_yili INTEGER,
                                yolcu_kapasitesi INTEGER,
                                petrol_kapasitesi REAL,
                                konteyner_sayisi INTEGER,
                                maks_agirlik REAL
                            )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS limanlar (
                                id INTEGER PRIMARY KEY,
                                liman_adi TEXT,
                                ulke TEXT,
                                nufus INTEGER,
                                pasaport_gerekli TEXT,
                                demirleme_ucreti_gereksinimi TEXT,
                                demirleme_ucreti REAL
                            )""")
        self.baglanti.commit()

    def gemi_ekle(self, gemi_tipi, seri_no, ad, agirlik, yapim_yili, ekstra_deger):
        if gemi_tipi == "Yolcu Gemi":
            self.cursor.execute(
                "INSERT INTO gemiler (tip, seri_no, ad, agirlik, yapim_yili, yolcu_kapasitesi) VALUES (?, ?, ?, ?, ?, ?)",
                (gemi_tipi, seri_no, ad, agirlik, yapim_yili, ekstra_deger))
        elif gemi_tipi == "Petrol Tankeri":
            self.cursor.execute(
                "INSERT INTO gemiler (tip, seri_no, ad, agirlik, yapim_yili, petrol_kapasitesi) VALUES (?, ?, ?, ?, ?, ?)",
                (gemi_tipi, seri_no, ad, agirlik, yapim_yili, ekstra_deger))
        elif gemi_tipi == "Konteyner Gemi":
            self.cursor.execute(
                "INSERT INTO gemiler (tip, seri_no, ad, agirlik, yapim_yili, konteyner_sayisi, maks_agirlik) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (gemi_tipi, seri_no, ad, agirlik, yapim_yili, ekstra_deger, ekstra_deger))
        self.baglanti.commit()
        messagebox.showinfo("Bilgi", "Yeni gemi eklendi.")

    def liman_ekle(self, liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti_gereksinimi, demirleme_ucreti=None):
        self.cursor.execute(
            "INSERT INTO limanlar (liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti_gereksinimi, demirleme_ucreti) VALUES (?, ?, ?, ?, ?, ?)",
            (liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti_gereksinimi, demirleme_ucreti))
        self.baglanti.commit()
        messagebox.showinfo("Bilgi", "Yeni liman eklendi.")


class GemiEklemeFormu:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Yeni Gemi Ekle")
        self.veritabani = db

        self.frame_gemi_bilgileri = tk.Frame(root)
        self.frame_gemi_bilgileri.pack(padx=10, pady=10)


        self.label_gemi_tipi = tk.Label(self.frame_gemi_bilgileri, text="Gemi Tipi:")
        self.label_gemi_tipi.grid(row=0, column=0, padx=10, pady=10)
        self.gemi_tipleri = ["Yolcu Gemi", "Petrol Tankeri", "Konteyner Gemi"]
        self.secilen_gemi_tipi = tk.StringVar(root)
        self.secilen_gemi_tipi.set(self.gemi_tipleri[0])
        self.dropdown_gemi_tipi = tk.OptionMenu(self.frame_gemi_bilgileri, self.secilen_gemi_tipi, *self.gemi_tipleri,
                                                command=self.gemi_tipi_degisti)
        self.dropdown_gemi_tipi.grid(row=0, column=1, padx=10, pady=10)


        self.label_seri_no = tk.Label(self.frame_gemi_bilgileri, text="Seri No:")
        self.label_seri_no.grid(row=1, column=0, padx=10, pady=10)
        self.entry_seri_no = tk.Entry(self.frame_gemi_bilgileri)
        self.entry_seri_no.grid(row=1, column=1, padx=10, pady=10)

        self.label_ad = tk.Label(self.frame_gemi_bilgileri, text="Ad:")
        self.label_ad.grid(row=2, column=0, padx=10, pady=10)
        self.entry_ad = tk.Entry(self.frame_gemi_bilgileri)
        self.entry_ad.grid(row=2, column=1, padx=10, pady=10)

        self.label_agirlik = tk.Label(self.frame_gemi_bilgileri, text="Ağırlık:")
        self.label_agirlik.grid(row=3, column=0, padx=10, pady=10)
        self.entry_agirlik = tk.Entry(self.frame_gemi_bilgileri)
        self.entry_agirlik.grid(row=3, column=1, padx=10, pady=10)

        self.label_yapim_yili = tk.Label(self.frame_gemi_bilgileri, text="Yapım Yılı:")
        self.label_yapim_yili.grid(row=4, column=0, padx=10, pady=10)
        self.entry_yapim_yili = tk.Entry(self.frame_gemi_bilgileri)
        self.entry_yapim_yili.grid(row=4, column=1, padx=10, pady=10)

        self.label_petrol_kapasitesi = tk.Label(self.frame_gemi_bilgileri, text="Petrol Kapasitesi (Litre):")
        self.entry_petrol_kapasitesi = tk.Entry(self.frame_gemi_bilgileri)

        self.label_yolcu_kapasitesi = tk.Label(self.frame_gemi_bilgileri, text="Yolcu Kapasitesi:")
        self.entry_yolcu_kapasitesi = tk.Entry(self.frame_gemi_bilgileri)

        self.label_konteyner_sayisi = tk.Label(self.frame_gemi_bilgileri, text="Konteyner Sayısı:")
        self.entry_konteyner_sayisi = tk.Entry(self.frame_gemi_bilgileri)

        self.label_maks_agirlik = tk.Label(self.frame_gemi_bilgileri, text="Maksimum Ağırlık:")
        self.entry_maks_agirlik = tk.Entry(self.frame_gemi_bilgileri)


        self.btn_ileri = tk.Button(root, text="İleri", command=self.sefer_ayrintilari_formunu_ac)
        self.btn_ileri.pack(side="bottom", padx=10, pady=10)


        self.gemi_tipi_degisti()

        self.sefer_ayrintilari_formu = None

    def gemi_tipi_degisti(self, *args):
        gemi_tipi = self.secilen_gemi_tipi.get()

        if gemi_tipi == "Yolcu Gemi":

            self.label_yolcu_kapasitesi.grid(row=5, column=0, padx=10, pady=10)
            self.entry_yolcu_kapasitesi.grid(row=5, column=1, padx=10, pady=10)


            self.label_petrol_kapasitesi.grid_forget()
            self.entry_petrol_kapasitesi.grid_forget()
            self.label_konteyner_sayisi.grid_forget()
            self.entry_konteyner_sayisi.grid_forget()
            self.label_maks_agirlik.grid_forget()
            self.entry_maks_agirlik.grid_forget()

        elif gemi_tipi == "Petrol Tankeri":

            self.label_petrol_kapasitesi.grid(row=5, column=0, padx=10, pady=10)
            self.entry_petrol_kapasitesi.grid(row=5, column=1, padx=10, pady=10)


            self.label_yolcu_kapasitesi.grid_forget()
            self.entry_yolcu_kapasitesi.grid_forget()
            self.label_konteyner_sayisi.grid_forget()
            self.entry_konteyner_sayisi.grid_forget()
            self.label_maks_agirlik.grid_forget()
            self.entry_maks_agirlik.grid_forget()

        elif gemi_tipi == "Konteyner Gemi":

            self.label_konteyner_sayisi.grid(row=5, column=0, padx=10, pady=10)
            self.entry_konteyner_sayisi.grid(row=5, column=1, padx=10, pady=10)

            self.label_maks_agirlik.grid(row=6, column=0, padx=10, pady=10)
            self.entry_maks_agirlik.grid(row=6, column=1, padx=10, pady=10)


            self.label_yolcu_kapasitesi.grid_forget()
            self.entry_yolcu_kapasitesi.grid_forget()
            self.label_petrol_kapasitesi.grid_forget()
            self.entry_petrol_kapasitesi.grid_forget()

    def sefer_ayrintilari_formunu_ac(self):

        if self.sefer_ayrintilari_formu is None:
            self.sefer_ayrintilari_formu = SeferAyrintilariFormu(self.root, self.veritabani)
            self.sefer_ayrintilari_formu.on_closing = self.sefer_ayrintilari_formu_kapaniyor
        else:
            messagebox.showerror("Hata", "Zaten bir sefer ayrıntıları formu açılmış.")


        self.root.wait_window(self.sefer_ayrintilari_formu.root)
        self.gemi_bilgilerini_ekle()

    def gemi_bilgilerini_ekle(self):
        gemi_tipi = self.secilen_gemi_tipi.get()
        seri_no = self.entry_seri_no.get()
        ad = self.entry_ad.get()
        agirlik = float(self.entry_agirlik.get())
        yapim_yili = int(self.entry_yapim_yili.get())


        if gemi_tipi == "Yolcu Gemi":
            ekstra_deger = int(self.entry_yolcu_kapasitesi.get())
        elif gemi_tipi == "Petrol Tankeri":
            ekstra_deger = float(self.entry_petrol_kapasitesi.get())
        elif gemi_tipi == "Konteyner Gemi":
            ekstra_deger = int(self.entry_konteyner_sayisi.get())


        self.veritabani.gemi_ekle(gemi_tipi, seri_no, ad, agirlik, yapim_yili, ekstra_deger)

    def sefer_ayrintilari_formu_kapaniyor(self):
        self.sefer_ayrintilari_formu = None


class SeferAyrintilariFormu:
    def __init__(self, root, db):
        self.root = tk.Toplevel(root)
        self.root.title("Yeni Sefer Ayrıntıları Ekle")
        self.veritabani = db


        self.label_liman_adi = tk.Label(self.root, text="Liman Adı:")
        self.label_liman_adi.grid(row=0, column=0, padx=10, pady=10)
        self.entry_liman_adi = tk.Entry(self.root)
        self.entry_liman_adi.grid(row=0, column=1, padx=10, pady=10)

        self.label_ulke = tk.Label(self.root, text="Ülke:")
        self.label_ulke.grid(row=1, column=0, padx=10, pady=10)
        self.entry_ulke = tk.Entry(self.root)
        self.entry_ulke.grid(row=1, column=1, padx=10, pady=10)

        self.label_nufus = tk.Label(self.root, text="Nüfus:")
        self.label_nufus.grid(row=2, column=0, padx=10, pady=10)
        self.entry_nufus = tk.Entry(self.root)
        self.entry_nufus.grid(row=2, column=1, padx=10, pady=10)

        self.label_pasaport_gerekli = tk.Label(self.root, text="Pasaport Gerekli mi?:")
        self.label_pasaport_gerekli.grid(row=3, column=0, padx=10, pady=10)
        self.var_pasaport_gerekli = tk.StringVar(root)
        self.var_pasaport_gerekli.set("Evet")  # Varsayılan olarak Evet seçili olsun
        self.radio_pasaport_gerekli_ev = tk.Radiobutton(self.root, text="Evet", variable=self.var_pasaport_gerekli, value="Evet")
        self.radio_pasaport_gerekli_ev.grid(row=3, column=1, padx=10, pady=10)
        self.radio_pasaport_gerekli_hayir = tk.Radiobutton(self.root, text="Hayır", variable=self.var_pasaport_gerekli, value="Hayır")
        self.radio_pasaport_gerekli_hayir.grid(row=3, column=2, padx=10, pady=10)

        self.label_demirleme_ucreti_gereksinimi = tk.Label(self.root, text="Demirleme Ücreti Gerekiyor mu?:")
        self.label_demirleme_ucreti_gereksinimi.grid(row=4, column=0, padx=10, pady=10)
        self.var_demirleme_ucreti_gereksinimi = tk.StringVar(root)
        self.var_demirleme_ucreti_gereksinimi.set("Evet")  # Varsayılan olarak Evet seçili olsun
        self.radio_demirleme_ucreti_gereksinimi_ev = tk.Radiobutton(self.root, text="Evet", variable=self.var_demirleme_ucreti_gereksinimi,
                                                                    value="Evet", command=self.demirleme_ucreti_sor)
        self.radio_demirleme_ucreti_gereksinimi_ev.grid(row=4, column=1, padx=10, pady=10)
        self.radio_demirleme_ucreti_gereksinimi_hayir = tk.Radiobutton(self.root, text="Hayır", variable=self.var_demirleme_ucreti_gereksinimi,
                                                                        value="Hayır", command=self.demirleme_ucreti_sor)
        self.radio_demirleme_ucreti_gereksinimi_hayir.grid(row=4, column=2, padx=10, pady=10)

        self.label_demirleme_ucreti = tk.Label(self.root, text="Demirleme Ücreti (TL):")
        self.entry_demirleme_ucreti = tk.Entry(self.root)
        self.label_demirleme_ucreti.grid(row=5, column=0, padx=10, pady=10)
        self.entry_demirleme_ucreti.grid(row=5, column=1, padx=10, pady=10)


        self.btn_tamam = tk.Button(self.root, text="Tamam", command=self.sefer_ayrintilarini_ekle)
        self.btn_tamam.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


        self.root.protocol("WM_DELETE_WINDOW", self.kapat)

        self.on_closing = None

    def demirleme_ucreti_sor(self):
        if self.var_demirleme_ucreti_gereksinimi.get() == "Evet":
            self.label_demirleme_ucreti.grid(row=5, column=0, padx=10, pady=10)
            self.entry_demirleme_ucreti.grid(row=5, column=1, padx=10, pady=10)
        else:
            self.label_demirleme_ucreti.grid_forget()
            self.entry_demirleme_ucreti.grid_forget()

    def kapat(self):
        if self.on_closing:
            self.on_closing()

        self.root.destroy()

    def sefer_ayrintilarini_ekle(self):
        liman_adi = self.entry_liman_adi.get()
        ulke = self.entry_ulke.get()
        nufus = int(self.entry_nufus.get())
        pasaport_gerekli = self.var_pasaport_gerekli.get()
        demirleme_ucreti_gereksinimi = self.var_demirleme_ucreti_gereksinimi.get()
        demirleme_ucreti = None


        if demirleme_ucreti_gereksinimi == "Evet":
            try:
                demirleme_ucreti = float(self.entry_demirleme_ucreti.get())
            except ValueError:
                messagebox.showerror("Hata", "Lütfen geçerli bir demirleme ücreti girin.")
                return


        self.veritabani.liman_ekle(liman_adi, ulke, nufus, pasaport_gerekli, demirleme_ucreti_gereksinimi, demirleme_ucreti)


        self.kapat()


def main():
    veritabani = GemiVeritabani()
    root = tk.Tk()
    uygulama = GemiEklemeFormu(root, veritabani)
    root.mainloop()


if __name__ == "__main__":
    main()
