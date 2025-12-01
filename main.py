import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#-- Main Window Tanımı --#
main_window = tk.Tk()
main_window.title("Omer Faruk Iskender - Ogrenci Yonetim Sistemi v1.0")
main_window.geometry("1341x700+300+100")
main_window.config(bg="lightgray")
try:
    main_window.iconbitmap('okul.ico')
except Exception:
    pass
main_window.resizable(False, False)



#-- Yeni Öğrenci Ekleme Fonksiyonu --#
def ogrenci_ekle():
    #---- Yeni Öğrenci Ekleme Penceresi ----#
    ogrenci_window = tk.Toplevel(main_window)
    ogrenci_window.title("Yeni Öğrenci Ekle")
    ogrenci_window.geometry("400x400+500+200")
    ogrenci_window.config(bg="white")
    try:
        main_window.iconbitmap(resource_path('okul.ico'))
    except Exception:
        pass
    #---- Öğrenci Bilgi Giriş Alanları ----#
    tk.Label(ogrenci_window, text="Öğrenci Adı:", font=("Arial", 14), bg="white").place(x=20, y=30)
    entry_adi = tk.Entry(ogrenci_window, font=("Arial", 14))
    entry_adi.place(x=150, y=30, width=200)
    tk.Label(ogrenci_window, text="Öğrenci Soyadı:", font=("Arial", 14), bg="white").place(x=20, y=80)
    entry_soyadi = tk.Entry(ogrenci_window, font=("Arial", 14))
    entry_soyadi.place(x=150, y=80, width=200)
    tk.Label(ogrenci_window, text="Öğrenci No:", font=("Arial", 14), bg="white").place(x=20, y=130)
    entry_numara = tk.Entry(ogrenci_window, font=("Arial", 14))
    entry_numara.place(x=150, y=130, width=200)
    tk.Label(ogrenci_window, text="Bölüm:", font=("Arial", 14), bg="white").place(x=20, y=180)
    entry_bolum = tk.Entry(ogrenci_window, font=("Arial", 14))
    entry_bolum.place(x=150, y=180, width=200)

    #---- Kaydet Butonu ve Fonksiyonu ----#
    def kaydet_ve_kapat():
        no=entry_numara.get()
        ad=entry_adi.get()
        soyad=entry_soyadi.get()
        bolum=entry_bolum.get()
        #---- Alan Kontrolü ----#
        if not no or not ad or not soyad or not bolum:
            tk.messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
            return
        
        if tree.exists(no):
            tk.messagebox.showwarning("Hata", "Bu öğrenci numarası zaten mevcut.")
            return
        
        #---- Varsayılan Not Değerleri ----#
        varsayilan_degerler = ("", "", "", "Girilmedi","", "", "", "Girilmedi","", "", "", "Girilmedi","", "", "", "Girilmedi")

        tree.insert('', tk.END, iid=no, values=(no, ad, soyad, bolum) + varsayilan_degerler)

        ogrenci_window.destroy()

    btn_kaydet = tk.Button(ogrenci_window, text="Öğrenci Kaydet", font=("Arial", 14), bg="#4CAF50", fg="white", command=kaydet_ve_kapat)
    btn_kaydet.place(x=150, y=250, width=200, height=40)
    


#-- Öğrenci Silme Fonksiyonu --#
def ogrenci_sil():
    selected_item = tree.selection()

    if not selected_item:
        tk.messagebox.showwarning("Uyarı", "Lütfen silinecek öğrenciyi seçin.")
        return
    selected_item = selected_item[0]
    try:
        ogrenci_bilgileri = tree.item(selected_item, 'values')
        onay_mesaji=f"{ogrenci_bilgileri[1]} {ogrenci_bilgileri[2]} (No: {ogrenci_bilgileri[0]}) adlı öğrenciyi silmek istediğinize emin misiniz?"
    except Exception as e:
        print(f"Bilgi Alınamadı: {e}")
        onay_mesaji="Seçilen öğrenciyi silmek istediğinize emin misiniz?"
    if tk.messagebox.askyesno("Öğrenci Sil", onay_mesaji):
        tree.delete(selected_item)     



#-- Öğrenci Bilgileri Güncelleme Fonksiyonu --#
def ogrenci_bilgi_guncelle():

    selected_item = tree.selection()
    if not selected_item:
        tk.messagebox.showwarning("Uyarı", "Lütfen güncellenecek öğrenciyi seçin.")
        return
    item_id = selected_item[0]
    eski_veriler = list(tree.item(item_id)['values'])

    guncelle_window = tk.Toplevel(main_window)
    guncelle_window.title("Öğrenci Bilgileri Güncelleme")
    guncelle_window.geometry("400x400+500+200")
    guncelle_window.config(bg="white")
    try:
        main_window.iconbitmap(resource_path('okul.ico'))
    except Exception:
        pass

    tk.Label(guncelle_window, text="Öğrenci No:", font=("Arial", 14), bg="white").place(x=20, y=30)
    tk.Label(guncelle_window, text="Yeni Adı:", font=("Arial", 14), bg="white").place(x=20, y=80)
    tk.Label(guncelle_window, text="Yeni Soyadı:", font=("Arial", 14), bg="white").place(x=20, y=130)
    tk.Label(guncelle_window, text="Yeni Bölüm:", font=("Arial", 14), bg="white").place(x=20, y=180)
    entry_guncelle_numara = tk.Entry(guncelle_window, font=("Arial", 14))
    entry_guncelle_numara.place(x=150, y=30, width=220)
    entry_guncelle_numara.insert(0, eski_veriler[0])
    entry_yeni_adi = tk.Entry(guncelle_window, font=("Arial", 14))
    entry_yeni_adi.place(x=150, y=80, width=220)
    entry_yeni_adi.insert(0, eski_veriler[1])
    entry_yeni_soyadi = tk.Entry(guncelle_window, font=("Arial", 14))
    entry_yeni_soyadi.place(x=150, y=130, width=220)
    entry_yeni_soyadi.insert(0, eski_veriler[2])
    entry_yeni_bolum = tk.Entry(guncelle_window, font=("Arial", 14))
    entry_yeni_bolum.place(x=150, y=180, width=220)
    entry_yeni_bolum.insert(0, eski_veriler[3])


    def guncellekapat():
        yeni_no = entry_guncelle_numara.get()
        yeni_ad = entry_yeni_adi.get()
        yeni_soyad = entry_yeni_soyadi.get()
        yeni_bolum = entry_yeni_bolum.get()

        if not yeni_no or not yeni_ad or not yeni_soyad or not yeni_bolum:
            tk.messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
            return

        tum_satir_verisi = list(tree.item(item_id)['values'])

        tum_satir_verisi[0] = yeni_no
        tum_satir_verisi[1] = yeni_ad
        tum_satir_verisi[2] = yeni_soyad
        tum_satir_verisi[3] = yeni_bolum

        tree.item(item_id, values=tum_satir_verisi)
        
        tk.messagebox.showinfo("Başarılı", "Öğrenci bilgileri güncellendi.")
        guncelle_window.destroy()

    btn_kaydet = tk.Button(guncelle_window, text="Değişiklikleri Kaydet", font=("Arial", 14),
                            bg="#4CAF50", fg="white", command=guncellekapat)
    btn_kaydet.place(x=150, y=250, width=200, height=40)


#-- Öğrenci Not Ekleme Veya Güncelleme Fonksiyonu --#
def ogrenci_not_guncelle():

    selected_item = tree.selection()
    if not selected_item:
        tk.messagebox.showwarning("Uyarı", "Lütfen notu girilecek öğrenciyi seçin.")
        return

    item_id = selected_item[0]
    veriler = tree.item(item_id)['values']

    not_window = tk.Toplevel(main_window)
    not_window.title("Not Girişi ve Güncelleme")
    not_window.geometry("550x380+400+100")
    not_window.config(bg="white")
    try:
        main_window.iconbitmap(resource_path('okul.ico'))
    except Exception:
        pass
    not_window.resizable(False,False)

    tk.Label(not_window, text="Öğrenci Bilgileri", bg="white", font=("Arial", 12, "bold")).place(x=20, y=20)
    tk.Label(not_window, text="Numara:", bg="white", font=("Arial", 11)).place(x=20, y=60)
    tk.Label(not_window, text=veriler[0], bg="white", width=20, font=("Arial", 11)).place(x=100, y=60)
    tk.Label(not_window, text="Adi:", bg="white", font=("Arial", 11)).place(x=20, y=100)
    tk.Label(not_window, text=veriler[1], bg="white", width=20, font=("Arial", 11)).place(x=100, y=100)
    tk.Label(not_window, text="Soyadı:", bg="white", font=("Arial", 11)).place(x=20, y=140)
    tk.Label(not_window, text=veriler[2], bg="white", width=20, font=("Arial", 11)).place(x=100, y=140)
    tk.Label(not_window, text="Bölümü:", bg="white", font=("Arial", 11)).place(x=20, y=180)
    tk.Label(not_window, text=veriler[3], bg="white", width=20, font=("Arial", 11)).place(x=100, y=180)

    tk.Label(not_window, text="Not Girişleri", bg="white", font=("Arial", 12, "bold")).place(x=300, y=20)
    tk.Label(not_window, text="Ders", font=("Arial", 10, "bold"), bg="white").place(x=300, y=60)
    tk.Label(not_window, text="Vize", font=("Arial", 10, "bold"), bg="white").place(x=400, y=60)
    tk.Label(not_window, text="Final", font=("Arial", 10, "bold"), bg="white").place(x=480, y=60)

    tk.Label(not_window, text="Matematik", font=("Arial", 11), bg="white").place(x=300, y=100)
    ent_mat_vize = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_mat_vize.place(x=400, y=100)
    ent_mat_vize.insert(0,veriler[4])
    ent_mat_final = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_mat_final.place(x=480, y=100)
    ent_mat_final.insert(0, veriler[5])

    tk.Label(not_window, text="Türkçe", font=("Arial", 11), bg="white").place(x=300, y=140)
    ent_tur_vize = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_tur_vize.place(x=400, y=140)
    ent_tur_vize.insert(0, veriler[8])
    ent_tur_final = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_tur_final.place(x=480, y=140)
    ent_tur_final.insert(0, veriler[9])

    tk.Label(not_window, text="Sosyal", font=("Arial", 11), bg="white").place(x=300, y=180)
    ent_sos_vize = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_sos_vize.place(x=400, y=180)
    ent_sos_vize.insert(0, veriler[12])
    ent_sos_final = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_sos_final.place(x=480, y=180)
    ent_sos_final.insert(0, veriler[13])

    tk.Label(not_window, text="Fen", font=("Arial", 11), bg="white").place(x=300, y=220)
    ent_fen_vize = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_fen_vize.place(x=400, y=220)
    ent_fen_vize.insert(0, veriler[16])
    ent_fen_final = tk.Entry(not_window, width=5, font=("Arial", 11), justify="center")
    ent_fen_final.place(x=480, y=220)
    ent_fen_final.insert(0, veriler[17])

    def hesapla_ve_kaydet():
        def not_hesapla_tek(vize_degeri, final_degeri, ders_adi):

            if vize_degeri.strip() == "": vize = 0
            else: vize = int(vize_degeri)
            
            if final_degeri.strip() == "": final = 0
            else: final = int(final_degeri)

            if vize < 0 or vize > 100:
                raise ValueError(f"{ders_adi} vize notu 0 ile 100 arasında olmalı!")
            
            if final < 0 or final > 100:
                raise ValueError(f"{ders_adi} final notu 0 ile 100 arasında olmalı!")

            ort = (vize * 0.4) + (final * 0.6)
            durum = "Geçti" if ort >= 50 else "Kaldı"
            return vize, final, round(ort, 2), durum

        try:
            m_v, m_f, m_ort, m_dur = not_hesapla_tek(ent_mat_vize.get(), ent_mat_final.get(), "Matematik")
            t_v, t_f, t_ort, t_dur = not_hesapla_tek(ent_tur_vize.get(), ent_tur_final.get(), "Türkçe")
            s_v, s_f, s_ort, s_dur = not_hesapla_tek(ent_sos_vize.get(), ent_sos_final.get(), "Sosyal")
            f_v, f_f, f_ort, f_dur = not_hesapla_tek(ent_fen_vize.get(), ent_fen_final.get(), "Fen")
            yeni_satir = (
                veriler[0], veriler[1], veriler[2], veriler[3],
                m_v, m_f, m_ort, m_dur,t_v, t_f, t_ort, t_dur,
                s_v, s_f, s_ort, s_dur,f_v, f_f, f_ort, f_dur
            )

            tree.item(item_id, values=yeni_satir)
            tk.messagebox.showinfo("Başarılı", "Notlar kaydedildi.")
            not_window.destroy()

        except ValueError as hata_mesaji:
            if "notu 0 ile 100 arasında olmalı" in str(hata_mesaji):
                tk.messagebox.showwarning("Geçersiz Not", str(hata_mesaji))
            else:
                tk.messagebox.showerror("Hata", "Lütfen not kutucuklarına sadece SAYI giriniz.")

    btn_kaydet = tk.Button(not_window, text="Notlari Kaydet", bg="green", fg="white", 
                           font=("Arial", 12, "bold"), command=hesapla_ve_kaydet)
    btn_kaydet.place(x=300, y=300, width=240, height=45)



#-- İçe Ve Dışa Veri Dosyası Aktarım Fonksiyonu --#
def aktarim_penceresi_ac():
    aktar_window = tk.Toplevel()
    aktar_window.title("İçe / Dışa Aktar")
    aktar_window.geometry("300x200+500+250")
    try:
        main_window.iconbitmap(resource_path('okul.ico'))
    except Exception:
        pass
    aktar_window.resizable(False, False)
    
    def disa_aktar():
        dosya_yolu = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Dosyası", "*.csv")],
            title="Verileri Kaydet"
        )

        if not dosya_yolu:
            return

        try:
            with open(dosya_yolu, mode='w', newline='', encoding='utf-8') as dosya:
                yazici = csv.writer(dosya)
                
                basliklar = [
                    "No", "Ad", "Soyad", "Bolum", 
                    "Mat Vize", "Mat Final", "Mat Ort", "Mat Durum","Tur Vize", "Tur Final", "Tur Ort", "Tur Durum",
                    "Sos Vize", "Sos Final", "Sos Ort", "Sos Durum","Fen Vize", "Fen Final", "Fen Ort", "Fen Durum"
                ]
                yazici.writerow(basliklar)

                for satir_id in tree.get_children():
                    degerler = tree.item(satir_id)['values']
                    yazici.writerow(degerler)
            
            tk.messagebox.showinfo("Başarılı", "Tüm veriler başarıyla dışa aktarıldı.")
            aktar_window.destroy()

        except Exception as e:
            tk.messagebox.showerror("Hata", f"Dışa aktarma hatası:\n{e}")

    #-- İçe Aktarım Fonksiyonu --#
    def ice_aktar():
        dosya_yolu = filedialog.askopenfilename(
            filetypes=[("CSV Dosyası", "*.csv")],
            title="Öğrenci Listesi Seç",
        )
        
        if not dosya_yolu:
            return

        try:
            with open(dosya_yolu, mode='r', newline='', encoding='utf-8') as dosya:

                okuyucu = csv.reader(dosya)

                next(okuyucu, None) 
                
                eklenen_sayisi = 0
                
                for row in okuyucu:
                    if row: 
                        tree.insert('', tk.END, values=row)
                        eklenen_sayisi += 1
            
            tk.messagebox.showinfo("Başarılı", f"{eklenen_sayisi} satır başarıyla içe aktarıldı.")
            aktar_window.destroy()

        except Exception as e:
            tk.messagebox.showerror("Hata", f"İçe aktarma hatası:\n{e}")

    lbl_info = tk.Label(aktar_window, text="İşlem Seçiniz", font=("Arial", 12))
    lbl_info.pack(pady=10)
    btn_import = tk.Button(aktar_window, text="İÇE AKTAR (CSV)", bg="blue",
                           font=("Arial", 11, "bold"), command=ice_aktar)
    btn_import.pack(fill="x", padx=20, pady=10)
    btn_export = tk.Button(aktar_window, text="DIŞA AKTAR (CSV)", bg="orange",
                           font=("Arial", 11, "bold"), command=disa_aktar)
    btn_export.pack(fill="x", padx=20, pady=10)

tum_veriler_yedek=[]


#-- Öğrenciler Arası Filtreleme Ve Arama Foksiyonu --#
def arama_yap():
    global tum_veriler_yedek
    aranan = entry_arama.get().lower()

    if not tum_veriler_yedek: #Tablo Yedekleme
        for child in tree.get_children():
            tum_veriler_yedek.append(tree.item(child)['values'])

    for item in tree.get_children():
        tree.delete(item)

    for veri in tum_veriler_yedek:
        satir_metni = "".join(str(x).lower() for x in veri)
        
        if aranan in satir_metni:
            tree.insert('', tk.END, values=veri)

    if aranan == "":
        tum_veriler_yedek = []
        


#-- Tablonun bulunacağı alanın tanımlanması --#
tablo_frame = ttk.Frame(main_window, padding="10")
tablo_frame.pack(expand=True, fill="both", pady=70)

#-- Sutün İsimlerinin Tanımlanması --#
columns = (
    "no", "ad", "soyad", "bolum", 
    "mat_vize", "mat_final", "mat_ortalama", "mat_durum","tur_vize", "tur_final", "tur_ortalama", "tur_durum",
    "sos_vize", "sos_final", "sos_ortalama", "sos_durum","fen_vize", "fen_final", "fen_ortalama", "fen_durum"
)

#-- Sutün isimlerinin Tanımlanması (Ön Yüzde Görünen) --#
column_headings = (
    "Öğr. No", "Ad", "Soyad", "Bölüm", 
    "Mat Vize", "Mat Final", "Mat Ort.", "Mat Durum","Tür Vize", "Tür Final", "Tür Ort.", "Tür Durum",
    "Sos Vize", "Sos Final", "Sos Ort.", "Sos Durum","Fen Vize", "Fen Final", "Fen Ort.", "Fen Durum"
)

#--Tablonun Oluşturulması --#
tree = ttk.Treeview(tablo_frame, columns=columns, show="headings")

for col, heading in zip(columns, column_headings):
    tree.heading(col, text=heading)

#-- Colon Genişlileri ve yazı biçimlerini düzenleme --#
tree.column("no", width=60, anchor="center")
tree.column("ad", width=120)
tree.column("soyad", width=120)
tree.column("bolum", width=150)

tree.column("mat_vize", width=70, anchor="center")
tree.column("mat_final", width=70, anchor="center")
tree.column("mat_ortalama", width=70, anchor="center")
tree.column("mat_durum", width=70, anchor="center")
tree.column("tur_vize", width=70, anchor="center")
tree.column("tur_final", width=70, anchor="center")
tree.column("tur_ortalama", width=70, anchor="center")
tree.column("tur_durum", width=70, anchor="center")
tree.column("sos_vize", width=70, anchor="center")
tree.column("sos_final", width=70, anchor="center")
tree.column("sos_ortalama", width=70, anchor="center")
tree.column("sos_durum", width=70, anchor="center")
tree.column("fen_vize", width=70, anchor="center")
tree.column("fen_final", width=70, anchor="center")
tree.column("fen_ortalama", width=70, anchor="center")
tree.column("fen_durum", width=70, anchor="center")

#-- Scrollbar ve grid yerleşimi --#
vsb=ttk.Scrollbar(tablo_frame,orient="vertical",command=tree.yview)
hsb=ttk.Scrollbar(tablo_frame,orient="horizontal",command=tree.xview)
tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
tree.grid(row=0,column=0,sticky="nsew")
vsb.grid(row=0,column=1,sticky="ns")
hsb.grid(row=1,column=0,sticky="ew")
tablo_frame.grid_rowconfigure(0,weight=1)
tablo_frame.grid_columnconfigure(0,weight=1)

def liste_temizle():
    if tk.messagebox.askyesno("Dikkat", "Tüm liste silinecek. Emin misin?"):
        for satir in tree.get_children():
            tree.delete(satir)

#-- Main Window --#
tk.Button(main_window, text="Yeni Öğrenci Ekle", font=("Arial", 16), bg="lightgreen", command=ogrenci_ekle).place(x=10,y=10, width=200, height=50)
tk.Button(main_window, text="Öğrenci Sil", font=("Arial", 16), bg="lightgreen", command=ogrenci_sil).place(x=220,y=10, width=200, height=50)
tk.Button(main_window, text="Öğrenci Güncelle", font=("Arial", 16), bg="lightgreen", command=ogrenci_bilgi_guncelle).place(x=430,y=10, width=200, height=50)
tk.Button(main_window, text="Not Ekle/Güncelle", font=("Arial", 16),bg="lightgreen",command=ogrenci_not_guncelle).place(x=640,y=10, width=200, height=50)
tk.Button(main_window, text="İçe/Dışa Aktar", font=("Arial",16), bg="lightgreen",command=aktarim_penceresi_ac).place(x=850,y=10, width=200, height=50)
tk.Label(main_window, text="Ara:", font=("Arial", 14, "bold")).place(x=1070, y=20)
tk.Button(main_window, text="Liste Temizle", font=("Arial",16), bg="red",command=liste_temizle).place(x=10,y=640, width=200, height=50)

entry_arama = tk.Entry(main_window, font=("Arial", 14))
entry_arama.place(x=1150, y=15, width=180, height=40)
entry_arama.bind("<KeyRelease>", lambda event: arama_yap())

main_window.mainloop()