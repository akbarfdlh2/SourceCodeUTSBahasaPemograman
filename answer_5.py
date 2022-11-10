print("NAMA : MUHAMAD AKBAR FADILAH")
print("NIM : 20200801269")
print("FAKULTAS : ILMU KOMPUTER")
print("JURUSAN : TEKNIK INFORMATIKA")
print("------------------------------")
pilihan = "y"
while pilihan == "y":
    print("""
    ==============================
    
    Akbar Cafe
    List Menu Minuman
 
    ==============================
    A. ES Mixue : Rp 16.000
    B. ES Boba : Rp 10.000
    C. ES Kopi Susu : Rp 5.000
    D. Ice Cream : Rp 5.000
    ==============================
    """)
    pesan = str(input("Masukkan List Abjad Menu ="))
    jumlahpesan = int(input("Masukkan Jumlah Pesanan ="))
    if pesan == "a":
        listnama = "ES Mixue"
        harga = (16000*jumlahpesan)
        ppn = int(10 * harga)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "b":
        listnama = "ES Boba"
        harga = (10000*jumlahpesan)
        ppn = int(10 * harga)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.2)
            totalharga = int(harga-diskon+ppn)
        else:
            diskon = (0)
            totalharga = int(harga+ppn)
    elif pesan == "c":
        listnama = "ES Kopi Susu"
        harga = int(5000*jumlahpesan)
        ppn = int(10 * harga)
        diskon = 0
        totalharga = int(harga+ppn)
    elif pesan == "d":
        listnama = "Ice Cream"
        harga = int(5000*jumlahpesan)
        ppn = int(10 * harga)
        diskon = 0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan = input(
            "Menu tidak tersedia, silahkan masukkan abjad dengan huruf kecil & pilih menu yang tersedia. Silahkan ulangi kembali Y/N =")

    print("--------------------------")
    print("Ananda Coffe")
    print("--------------------------")
    print("Menu :", listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan = input("Apakah Anda ingin order kembali Y/N =")
