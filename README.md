NAMA: MAREXCEL ELIBINO  NIM: 2609116087  KELAS: C

MINI PROJECT 2

1. Deskripsi Singkat Program:
Program ini dibuat pakai Python buat ngatur antrean servis motor di bengkel. Di Mini Project 2 ini, kodenya udah dikembangin pakai **Nested Dictionary** buat nyimpen data-datanya, terus dibungkus pakai **Fungsi (def)** biar rapi dan gampang dipanggil. Ada juga sistem **Login** buat bedain hak akses:
* **Admin**: Bisa ngeliat semua data, nambah antrean, ngubah biaya, sampe ngehapus data yang udah selesai.
* **User**: Cuma bisa ngecek daftar antrean doang (data privasi kayak plat nomor sama biaya disembunyiin).


2. Gambar Flowcart dan Penjelasan Alur:
   <img width="3217" height="1752" alt="flowchart_antrean_servis_motor" src="https://github.com/user-attachments/assets/daabd8b3-ece6-4ab0-8df0-c6857f4b5877" />
1. Mulai & Login:
-Program pas dijalanin langsung nampilin halaman login. Kita tinggal masukin username sama password-nya. Kalau mau keluar program, tinggal ketik exit.
2.Cek Role (Admin / User):
-Nanti program ngecek akun yang dimasukin masuk ke role mana:
-Kalau Admin: Bakal masuk ke menu admin yang punya 5 fitur lengkap. Bisa liat tabel antrean data full (mulai dari nomor, nama, merek motor, plat nomor, sampai biaya servis), nambahin data baru (lengkap dengan validasi angka biar gak error), ngubah biaya, ngehapus data kalau servisnya udah beres, atau logout.
-Kalau User: Bakal masuk ke menu user yang pilihannya lebih simpel. Cuma bisa liat daftar antrean versi ringkas (cuma nampilin No Antrean, Nama, sama Merek Motor doang, jadi data privasi kayak plat sama biaya aman gak keliatan), sama tombol buat logout.
3.Selesai:
Setiap beres milih menu, kita bisa balik lagi ke pilihan sebelumnya atau logout buat balik ke halaman login awal.


Dokumentasi Program & Output, disertai dengan penjelasannya:
Ini bagian manggil library luar dan bawaan Python. Ada os buat bersihin terminal, time buat ngasih jeda, sama PrettyTable buat bikin tabel biar rapi.
<img width="1006" height="121" alt="Screenshot 2026-10-06 155422" src="https://github.com/user-attachments/assets/2e98b8c9-b000-4e18-b7c7-928b57ed525f" />












Ini Nested Dictionary (dictionary di dalam dictionary) yang diajarin di materi. Fungsinya buat nyimpen data motor (kayak nama, merek, plat, sama biaya servis).
<img width="1386" height="120" alt="Screenshot 2026-10-06 164128" src="https://github.com/user-attachments/assets/105cf794-13df-4361-826c-6b45cdb62431" />








Dictionary biasa buat nyimpen data username dan password buat sistem login (admin dan user).
<img width="1051" height="123" alt="Screenshot 2026-10-06 164437" src="https://github.com/user-attachments/assets/5c0eb562-7b93-456b-a92a-62bd0f999f28" />











Fungsi input_biaya() ini bertugas untuk meminta input biaya servis dari pengguna dengan menerapkan sistem error handling (try-except). Di dalamnya, program mencoba mengubah input teks menjadi angka bulat (int); jika pengguna tidak sengaja mengetik huruf atau selain angka, program tidak akan crash atau error, melainkan otomatis menangkap kesalahan tersebut di bagian except ValueError untuk mencetak pesan peringatan "Input salah!" lalu menyuruh pengguna menginput ulang angkanya.
<img width="1276" height="254" alt="Screenshot 2026-10-06 164804" src="https://github.com/user-attachments/assets/eaf61c07-f4a9-44d1-9961-70099aef8edc" />












Fungsi ini bertugas untuk menampilkan daftar antrean dalam bentuk tabel menggunakan library PrettyTable. Di dalamnya terdapat pengecekan peran (role): jika yang membuka adalah admin, kolom tabel yang ditampilkan lengkap (No Antrean, Nama, Merek, Plat, dan Biaya); sedangkan jika yang membuka adalah user, kolom plat nomor dan biaya disembunyikan sehingga hanya menampilkan No Antrean, Nama Pelanggan, dan Merek Motor saja.
<img width="1175" height="735" alt="Screenshot 2026-10-06 165058" src="https://github.com/user-attachments/assets/21454320-f684-4e60-8251-b57b2ab039cd" />








Fungsi ini digunakan untuk menampilkan menu khusus User secara berulang menggunakan perulangan while True. Di dalamnya terdapat pilihan bagi user untuk melihat daftar antrean (dengan memanggil fungsi lihat_antrean("user")) atau memilih logout (menggunakan perintah break untuk keluar dari menu dan kembali ke halaman login). Jika user mengetik pilihan selain angka 1 atau 2, program akan menampilkan pesan "Pilihan tidak valid!" selama 1 detik.
<img width="1322" height="396" alt="Screenshot 2026-10-06 165314" src="https://github.com/user-attachments/assets/3123c55b-3481-423b-9dda-25bf2c81d640" />








Fungsi ini adalah gerbang utama jalannya program yang bertugas untuk menangani sistem login.
Di dalamnya, pengguna diminta memasukkan username dan password. Jika pengguna mengetik exit pada username, program akan menampilkan ucapan terima kasih lalu berhenti menggunakan perintah break.   Program mengecek kecocokan data menggunakan percabangan: jika username terdaftar di dictionary akun dan password-nya benar, program akan menampilkan pesan sukses, menunggu 1 detik, lalu mengecek rolenya.   Jika username adalah "admin", program akan membuka menu_admin(); jika "user", program akan membuka menu_user(). Sebaliknya, jika salah, program akan mencetak pesan "Username atau Password salah!".   Baris paling bawah (login()) berfungsi untuk memanggil dan menjalankan seluruh fungsi login tersebut saat pertama kali program di-run.  
<img width="1184" height="682" alt="Screenshot 2026-10-06 165521" src="https://github.com/user-attachments/assets/dd943086-f9bc-47f0-b530-a0b622043e52" />








<img width="1920" height="1080" alt="Screenshot 2026-10-06 160035" src="https://github.com/user-attachments/assets/6821bb9f-5820-49d2-b166-e0bac2774400" />
disini saya login sistem antrean servis motor dengan login admin
username: admin pw:123












<img width="1920" height="1080" alt="Screenshot 2026-10-06 160108" src="https://github.com/user-attachments/assets/f43e16b1-d616-481b-9d03-e182403e02b8" />
disini kita udah masuk sistem dan terdapat 5 pilihan (lihat antrean,tambah antrean, ubah biaya, hapus antrean, log out)










<img width="1920" height="1080" alt="Screenshot 2026-10-06 160122" src="https://github.com/user-attachments/assets/8e7ff1eb-eb61-41c5-852b-3b467467c469" />
saya pilih lihat antrean di sistem terdapat 2 motor orang yang sedang di sistem bengkel







<img width="1920" height="1080" alt="Screenshot 2026-10-06 160250" src="https://github.com/user-attachments/assets/d3a8aec9-7bde-4622-b2a3-7c80433b915c" />
saya lanjut memilih tambah antrean, disini saya menambah 1 motor yang akan di perbaiki (A-03,Excell,Honda Beat,200000) lalu saya enter akan muncul tambah antrean berhasil!








<img width="1920" height="1080" alt="Screenshot 2026-10-06 160340" src="https://github.com/user-attachments/assets/3de78dc1-91d9-49bd-bf38-e1c3de2f49ce" />
ke menu ubah biaya disini saya bisa ubah biaya motor apas (Honda Vario) saya ubah biaya 250000











<img width="1920" height="1080" alt="Screenshot 2026-10-06 160709" src="https://github.com/user-attachments/assets/6c5faaab-ecbd-43ea-b91c-91d2e3dd7f62" />
disini saya memilih ke menu hapus antrean. saya mau hapus motor Yamaha Nmax (Azzam) karena service sudah selesai. setelah mengirim no A-02 lalu tekan enter akan muncul Hapus Antrean Berhasil.









<img width="1920" height="1080" alt="Screenshot 2026-10-06 160108" src="https://github.com/user-attachments/assets/5a6fd4f2-0bf8-4852-a010-11466001a76c" />
<img width="1920" height="1080" alt="Screenshot 2026-10-06 160904" src="https://github.com/user-attachments/assets/e181c7cc-d4d0-4a5f-b3c0-0588738facb1" />
di menu ke 5 ada log out, disini saya akan memilih logout lalu akan ke arah awal login username dan arah exit









<img width="1920" height="1080" alt="Screenshot 2026-10-06 160814" src="https://github.com/user-attachments/assets/143e5f8b-a453-4133-b97d-faea2951b3e0" />
disini saya arah login username user
username: user pw:321









<img width="1920" height="1080" alt="Screenshot 2026-10-06 160830" src="https://github.com/user-attachments/assets/8d1689f5-ec6a-45c6-9618-364a1557d25c" />
disini kita sebagai user hanya bisa mengakses lihat antrean dan logout, lalu saya memilih lihat antrean service motor







<img width="1920" height="1080" alt="Screenshot 2026-10-06 172817" src="https://github.com/user-attachments/assets/92ad0139-b4d4-459f-bc40-5157cb5d189f" />
disini bisa di liat terdapat 2 motor orang service dan dibawah ada arah tekan enter untuk kembali ke menu awal








<img width="1300" height="166" alt="Screenshot 2026-10-06 173036" src="https://github.com/user-attachments/assets/8cfe205f-7ed0-4b65-a326-647a4c93bfc6" />
disini saya pilih logout dan kita akan balik lagi ke login username dan password seperti di awal
























