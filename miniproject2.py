import os
import time
from prettytable import PrettyTable

data_antrean = {
    "A-01": {"nama": "Apas", "merek": "Honda Vario", "plat": "KT 5941", "biaya": 150000},
    "A-02": {"nama": "Azzam", "merek": "Yamaha NMAX", "plat": "KT 5678", "biaya": 75000}
}

akun = {
    "admin": "123",
    "user": "321"
}

def input_biaya():
    while True:
        try:
            biaya = int(input("Masukkan Biaya: Rp "))
            if biaya < 0:
                print("Biaya tidak boleh minus!")
                continue
            return biaya
        except ValueError:
            print("Input salah! Harap masukkan angka saja.")

def lihat_antrean(role="admin"):
    os.system("cls")
    
    if role == "admin":
        print("=== DAFTAR ANTREAN SERVIS (ADMIN) ===")
    else:
        print("=== DAFTAR ANTREAN SERVIS (USER) ===")
    
    if len(data_antrean) == 0:
        print("Saat ini antrean kosong.")
    else:
        tabel = PrettyTable()
        
        if role == "admin":
            tabel.field_names = ["No Antrean", "Nama Pelanggan", "Merek Motor", "Plat Nomor", "Biaya Servis"]
            for no in data_antrean:
                nama = data_antrean[no]["nama"]
                merek = data_antrean[no]["merek"]
                plat = data_antrean[no]["plat"]
                biaya = "Rp " + str(data_antrean[no]["biaya"])
                tabel.add_row([no, nama, merek, plat, biaya])
        else:
            tabel.field_names = ["No Antrean", "Nama Pelanggan", "Merek Motor"]
            for no in data_antrean:
                nama = data_antrean[no]["nama"]
                merek = data_antrean[no]["merek"]
                tabel.add_row([no, nama, merek])
                
        print(tabel)

def tambah_antrean():
    lihat_antrean()
    no = input("Masukkan No Antrean (Contoh A-03): ")
    if no in data_antrean:
        print("Nomor antrean sudah ada!")
        return

    nama = input("Masukkan Nama: ")
    merek = input("Masukkan Merek Motor: ")
    plat = input("Masukkan Plat Nomor: ")
    biaya = input_biaya()

    data_antrean.update({no: {"nama": nama, "merek": merek, "plat": plat, "biaya": biaya}})
    print("Data berhasil ditambahkan!")

def ubah_biaya():
    lihat_antrean()
    if len(data_antrean) == 0: return
    no = input("Masukkan No Antrean yang ingin diubah: ")
    if no in data_antrean:
        biaya_baru = input_biaya()
        data_antrean[no]["biaya"] = biaya_baru
        print("Biaya berhasil diperbarui!")
    else:
        print("Nomor antrean tidak ditemukan.")

def hapus_antrean():
    lihat_antrean()
    if len(data_antrean) == 0: return
    no = input("Masukkan No Antrean yang sudah selesai: ")
    if no in data_antrean:
        del data_antrean[no]
        print("Servis untuk " + no + " selesai! Data dihapus.")
    else:
        print("Nomor antrean tidak ditemukan.")

def menu_admin():
    while True:
        os.system("cls")
        print("=== MENU ADMIN ===")
        print("1. Lihat Antrean")
        print("2. Tambah Antrean")
        print("3. Ubah Biaya")
        print("4. Hapus Antrean")
        print("5. Logout")
        pilih = input("Pilih (1-5): ")

        if pilih == "1":
            lihat_antrean("admin")
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            tambah_antrean()
            time.sleep(1.5)
        elif pilih == "3":
            ubah_biaya()
            time.sleep(1.5)
        elif pilih == "4":
            hapus_antrean()
            time.sleep(1.5)
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)

def menu_user():
    while True:
        os.system("cls")
        print("=== MENU USER ===")
        print("1. Lihat Antrean")
        print("2. Logout")
        pilih = input("Pilih (1-2): ")

        if pilih == "1":
            lihat_antrean("user")
            input("\nTekan Enter untuk kembali...")
        elif pilih == "2":
            break
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)

def login():
    while True:
        os.system("cls")
        print("=== SISTEM ANTREAN SERVIS MOTOR ===")
        print("Ketik 'exit' pada Username untuk keluar.")
        
        username = input("Username : ")
        if username == "exit":
            print("Terima kasih!")
            break
            
        password = input("Password : ")
        
        if username in akun and akun[username] == password:
            print("Login sukses! Selamat datang, " + username)
            time.sleep(1)
            
            if username == "admin":
                menu_admin()
            elif username == "user":
                menu_user()
        else:
            print("Username atau Password salah!")
            time.sleep(1.5)

login()