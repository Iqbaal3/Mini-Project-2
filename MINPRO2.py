from prettytable import PrettyTable 

from pwinput import pwinput

data_users_premium = {
        #username : password
        "Iqbal" : "1471",
        "labqi" : "1741",
    }

data_users_basic = {
        #username : password
        "heisenberg" : "1111",
        "el camino" : "4444" ,
    }

# Data makanan: nama makanan : kalori , protein (per 100g)
data_makanan = {
    "nasi": (130, 2.7),
    "ayam": (240, 27),
    "ubi": (110, 2),
    "telur": (155, 13),
    "tahu": (76, 8),
    "tempe": (193, 20),
    "apel": (52, 0.3),
    "pisang": (89, 1.1),
}

# List konsumsi (masih kosong)
konsumsi = []

#function login

def login():

    Keterangan = 0

    print("==========SILAHKAN LOGIN TERLEBIH DAHULU==========")
    kesempatan = 3
    while kesempatan > 0 :
        try:
            input_username = input("Masukkan username anda: ")
            input_password = pwinput("Masukkan password anda (contoh : 1234): ", "*")
            
        except KeyboardInterrupt:
            print("Jangan Mengklik CTRL + C saat program berlangsung!")
            continue
        except EOFError:
            print("Jgn tekan CTRL + Z ya!!!")
            continue

        if input_username in data_users_premium and data_users_premium[input_username] == input_password: 
            print("!Yeay, Login Berhasil sebagai USER PREMIUM!")
            Keterangan += 1
            break

        elif input_username in data_users_basic and data_users_basic[input_username] == input_password: 
            print("!Yeay, Login Berhasil!")
            Keterangan += 2
            break

        else : 
            kesempatan -= 1
            print(f"Login Gagal, silahkan input username dan password lagi (kesempatan sisa : {kesempatan})")
            if kesempatan == 0 :
                print("Kesempatan Anda Habis, Login Gagal") 
                exit()

    return Keterangan


#function menu utama
def Menu_utama():
    print("========================================================")
    print("                     MENU UTAMA")
    table = PrettyTable(["No","Perintah","Keterangan"])
    table.add_row(["1","Tambah","Tambah makanan yang di konsumsi"])
    table.add_row(["2","List","Lihat makanan yang sudah ditambahkan"])
    table.add_row(["3","Edit","Edit/Update makanan di list konsumsi"])
    table.add_row(["4","Hapus","Hapus makanan dari list konsumsi"])
    table.add_row(["5","Selesai","Akhiri dan lihat total"])
    print(table)

#function Hapus
def hapus ():
    if len(konsumsi) == 0:
        ("Belum ada makanan yang di tambahkan")  
    else: 
        nomor = 0
        for nomor in range(len(konsumsi)):
            nama, berat = konsumsi[nomor]
            print(f"{nomor + 1} {nama}: {berat} gram")
        
        hapus = int(input("Masukkan nomor makanan yang ingin dihapus: ")) - 1
        if 0 <= hapus < len(konsumsi):
            terhapus = konsumsi.pop(hapus)
            print(f"{terhapus[0]} sebanyak {terhapus[1]} gram telah dihapus.")
        else:
            print("Nomor tidak valid")

#function edit
def edit ():
    if len(konsumsi) == 0:
        ("Belum ada makanan yang di tambahkan")
    else:
        nomor = 0
        for nomor in range(len(konsumsi)):
            nama, berat = konsumsi[nomor]
            print(f"{nomor + 1} {nama}: {berat} gram")
        
        nomor = int(input("Masukkan nomor makanan yang ingin diubah: ")) - 1
        if 0 <= nomor < len(konsumsi):
            makanan = input("Ubah menjadi makanan apa?: ")
            if makanan in data_makanan:
                berat = float(input("Masukkan berat makanan dalam gram (contoh: 100): "))
                if berat > 0:
                    terhapus = konsumsi.pop(nomor)
                    konsumsi.insert(nomor,(makanan, berat))
                    print(f"{terhapus[0]} telah di ubah menjadi {makanan} .") 
                else:
                    print("Maaf, Berat harus lebih dari 0 gram")
            else :
                print("Maaf, Makanan tidak ditemukan dalam daftar progam")
        else:
            print("Nomor tidak valid")

#Function Tambah Makanan
def tambah ():
    print("=================================================")
    print("Daftar Makanan Beserta Kalori & Protein")
    for makanan in data_makanan:
        kalori, protein = data_makanan[makanan]
        print(f"- {makanan}: {kalori} kalori, {protein}g protein")

    while True:    
        makanan = input("Masukkan nama makanan (Ketik 'Selesai' untuk berhenti): ")
        if makanan == "Selesai" :
            break
        elif makanan in data_makanan :    
            berat = float(input("Masukkan berat makanan dalam gram (contoh: 100): "))
            if berat > 0:
                konsumsi.append((makanan, berat))
                print(f"{makanan} sebanyak {berat} gram berhasil ditambahkan.")
            else:
                print("Maaf, Berat harus lebih dari 0 gram")
        else :
            print("Maaf, Makanan tidak ditemukan dalam daftar progam")

#function menampilkan list
def listt () :
        if len(konsumsi) == 0:
            print("Belum ada makanan yang ditambahkan")
        else:
            print("Daftar makanan yang dikonsumsi:")
            for nama, berat in konsumsi:
                print(f"- {nama} sebanyak {berat} gram")
    

def hitung ():
    total_kalori = 0
    total_protein = 0

    for nama, berat in konsumsi:
        kalori_per_100g, protein_per_100g = data_makanan[nama]
        kalori = kalori_per_100g * berat / 100
        protein = protein_per_100g * berat / 100
        total_kalori += kalori
        total_protein += protein

    # TOTAL
    print(" ======================")
    print(" Total Asupan Hari Ini ")
    print(" ======================")
    print(f"Kalori : {total_kalori} Kalori")
    print(f"Protein: {total_protein} Gram")

#Mulai Program
status = login()

if status == 1:
    while True :
        print("=====================PENGGUNA PREMIUM=====================")
        Menu_utama()
        perintah = input("Masukkan perintah 1-5, (contoh : 1) : ")
        if perintah == "1":
            tambah ()
        elif perintah == "2":
            listt ()
        elif perintah == "3":
            edit ()
        elif perintah == "4":
            hapus ()
        elif perintah == "5":
            hitung()
            break
        else:
            ("perintah tidak valid")
elif status == 2:
    while True :
        print("=====================PENGGUNA BASIC=======================")
        Menu_utama()
        perintah = input("Masukkan perintah 1-5, (contoh : 1) : ")
        if perintah == "1":
            tambah ()
        elif perintah == "2":
            listt ()
        elif perintah == "3":
            print("Maaf, Fitur tidak tersedia, silahkan beli PREMIUM untuk mengakses ;v")
        elif perintah == "4":
            print("Maaf, Fitur tidak tersedia, silahkan beli PREMIUM untuk mengakses ;v")
        elif perintah == "5":
            hitung()
            break
        else:
            ("perintah tidak valid")
else:
    ("tidak valid")
