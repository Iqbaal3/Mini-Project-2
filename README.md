# Mini-Project-2 Praktikum DDP
**Nama  : Iqbal Nurriz Ramadhan**
**Kelas : Sistem Informasi (B)**
**NIM    : 2509116067**

Mini Project yang saya buat disini pengembangan dari tema sebelumnya yaitu Program "Pelacak Asupan Kalori & Protein Harian" Sesuai dengan namanya program ini bertujuan menghitung jumlah Kalori & Protein yang telah di konsumsi. Program ini bermanfaat untuk orang orang yang sedang melakukan Bulking ataupun Cutting (Diet).  Program ini sudah menerapkan CRUD (Create, Read, Update, Delete) yang di wakili masing-masing pilihan yaitu:
1) Tambah - untuk menambahkan makanan yang telah di konsumsi
2) List - Untuk melihat list/daftar makanan yang telah di input/konsumsi
3) Edit - untuk mengubah makanan yang telah di input menjadi makanan lain
4) Hapus - menghapus makanan dari list makanan yang telah di konsumsi
5) Selesai - menyudahi program serta menghitung total keseluruhan dari protein dan kalori yang telah di input/konsumsi lalu menampilkannya.

Untuk dapat menggunakan program pengguna/users harus login terlebih dahulu dengan username dan password. dari username dan password ini akan menentukan role pengguna. Program ini berjalan dengan 2 role yaitu Role Basic dan Role Premium yang dimana role basic hanya dapat mengakses 3 fitur yaitu Tambah, list, selesai. sementara role premium dapat mengakses keseluruhan fitur. program ini juga dapat menyembunyikan password yang sedang di input.

# Flowchart / Alur Program
<img width="2408" height="2160" alt="Image" src="https://github.com/user-attachments/assets/f932d4b2-d49b-4caf-8126-5548c336e84e" />

# Output tiap tiap kondisi
**LOGIN**
1. Kondisi Login Premium

login berhasil ke premium karena username dan password sesuai dengan dictionary data_users_premium
   <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/de2ebc0e-2adb-467f-8708-3a36a4a5d160" />
2. Kondisi Login Basic

login berhasil ke basic karena username dan password sesuai dengan dictionary data_users_premium
   <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/757b1afe-6c42-4bb8-9951-d8be3d88f62c" />
3. Kondisi Login Gagal

login gagal karena username atau password tidak sesuai dengan dictionary data_users_premium maupun data_users_basic
   <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/51422401-7041-49ff-9ce9-e78328be4393" />
   
**TAMBAH**
  1. Kondisi Tambah makanan berhasil

berhasil menambah makanan karena nama makanan yang di input terdapat pada dictionary data_makanan serta jumlah beratnya valid
 <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/ed85d3b5-7ce3-4fd9-938a-a94ff56d0882" />
  2. Kondisi Tambah makanan gagal karena makanan tidak valid

gagal menambah makanan karena nama makanan yang di input tidak terdapat pada dictionary data_makanan
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/a9d75c96-b94d-4018-8db1-38e0a4506b70" />
  3. Kondisi Tambah makanan gagal karena jumlah makanan makanan tidak valid

gagal menambah makanan karena berat makanan yang di input tidak valid (berupa huruf ataupun minus)
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/c2e40d92-6506-41b7-ab2d-b4a657ffe5c2" />

**LIST**
1. Kondisi menampilkan list/daftar berhasil

program menamilkan seluruh makanan yang ada di list konsumsi beserta beratnya
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/79c03129-fddd-4476-8adf-82b420d1b789" />
2. Kondisi menampilkan list/daftar gagal

Dapat terjadi karena belum ada makanan yang di input dengan fitur tambah, sehingga list konsumsi masih kosong
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/c24f7047-bb28-4902-8196-305cb451b5ba" />
**EDIT**
1. Kondisi Edit berhasil

Berhasil karena sudah ada makanan di list konsumsi, lalu user menginput nama makanan yang ada di dictionary data_makanan dan beratnya valid. cara kerjanya yaitu program menghapus makanan di konsumsi sesuai dengan nomor/indeks yang di ketikkan pengguna lalu program menambahkan makanan yang telah pengguna input tetapi tetap harus sesuai dengan makanan yang ada di dictionary data_makanan. lalu menambahkan beratnya.
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/baf5f7ff-08da-4d9a-a857-f08f67ff40c4" /> 
2. Kondisi Edit tetapi belum ada makanan yang di tambahkan

Belum ada makanan di list konsumsi sehingga fitur edit masih belum bisa di gunakan
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/eabfebe3-532b-4397-909c-9091fe525c8c" />
3. Kondisi Edit gagal karena nomor makanan tidak valid

Users menginput nomor yang salah/huruf, sehingga program tidak tahu akan mengganti makanan yang mana.
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/b8d1e445-243b-44ba-a758-e318693ea4f2" />
4. kondisi Edit gagal karena makanan tidak valid

Terjadi karena Users menginputkan makanan yang tidak ada di dictionary data_makanan
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/7a2e2efb-2b8a-440f-ade5-c25f2f9b8cc4" />
5. Kondisi Edit gagal karena berat makanan tidak valid

Terjadi karena pengguna menginput berat yang kurang dari 1 ataupun menginput huruf
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/145d6852-6c2e-4724-944d-ba4fa0aefa2a" />

6. Kondisi Users Basic mencoba fitur Edit

program tidak memanggil fungsi edit seperti pada pengguna premium
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/92282f07-a3e0-4dd8-8989-316a144b0a52" />
   
**HAPUS**
1. Kondisi Hapus Berhasil

Terjadi karena list konsumsi sudah terisi dan pengguna menginput nomor/indeks yang sesuai.
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/4d571e65-1766-4976-8851-d0c31fd49ccd" />
2. Kondisi Hapus gagal karena nomor tidak valid

Terjadi karena input nomor/indek yg di masukkan pengguna tidak valid ataupun berupa huruf
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/b1055c23-c0f8-4458-8943-e9c9603236c6" />
3. Kondisi Hapus namun belum menambah makanan

karena list konsumsi masih kosong, sehingga fitur konsumsi tidak dapat di teruskan
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/a0bb868e-43e2-4628-a679-98e9b04057f0" />
4. Kondisi Pengguna Basic mencoba fitur Hapus

program tidak memanggil fungsi hapus seperti pada pengguna premium.
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/6816514b-91e3-4e86-bd12-6cc422027118" />

**SELESAI**
1. Kondisi Selesai berhasil

Ketika users telah menginput makanan yang di konsumsi beserta beratnya dengan valid menggunakan fitur tambah, maka ketika ia menggunakan fitur selesai program dapat menghitung berat yang ada di list konsumsi lalu di kali dengan jumlah protein di dictionary data_makanan. dan hasil keseluruhannya akan di tampilkan.
   <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/021d61f1-9df2-40c1-a343-a7286dcad77b" /> 
2. Kondisi selesai gagal/belum menambah makanan

Jika user tidak/belum menginput makanan, maka program tidak dapat menghitung sebab list konsumsi masih kosong dan akan menampilkan jumlahnya = 0.
   <img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/43564138-2b8e-40f1-bf0c-8f8570cdc793" />
**Kondisi Lainnya**
1. Kondisi jika mengklik CTRL + Z atau CTRL + C saat program berlangsung

Terjadi karena terdapat syntax try dan except pada bagian input, sehingga jika mengklik CTRL + C (dapat menghentikan program seketika) dan CTRL + Z, program tidak akan error / exit
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/d4ac8daa-242f-41a5-9a21-26ad36cbbc88" />

2. Kondisi Jika perintah bukan angka 1-5

Hanya tersedia 5 fitur sehingga ketika pengguna menginput angka selain 1-5 atau huruf maka sistem akan menapilkan kata "Perintah tidak valid"
<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/f907527b-5d62-4881-97be-397d4f443891" />
   



