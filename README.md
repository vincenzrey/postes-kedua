# postes-kedua

from prettytable import PrettyTable
global tabel
user = {'name' : 'Vincenz', 'password':'semangatkerja', 'Role' : '1'}


tabel = PrettyTable()
tabel.field_names = ["ID", "Nama Barang", "Merk", "Harga"]
tabel.add_row (["1", "Helm Safety", "USA", "Rp. 25000"])
tabel.add_row (["2", "Wearpack", "ASGARD", "Rp. 120000"])
tabel.add_row (["3", "Rompi", "GO SAVE", "Rp. 20.000"]),
tabel.add_row (["4", "Sarung Tangan", "MATAHARI", "Rp. 30.000"])
tabel.add_row (["5", "Sepatu Safety", "CHEETAH", "Rp. 425.000"])
hasil = PrettyTable()
hasil.add_row (["ID", "Nama Barang", "Jumlah", "Total Harga"])

def create():
    id = int(input("masukan id barang : "))
    nama = input("Masukkan nama barang : ")
    merk = input("Masukkan merk barang : ")
    harga = int(input("Masukkan harga : "))
    tabel.add_row([id, nama, merk, harga])
    print(tabel)
    print("Barang telah ditambahkan")

def read():
    print(tabel)

def update():
    id = int(input("Masukan id barang : "))
    nama = input("Masukkan nama barang baru: ")
    merk = input("Masukkan merk baru: ")
    harga = input("Masukkan harga baru: ")
    tabel[id] = [id, nama, merk, harga]
    print("Barang berhasil diperbarui.")

def delete():
    print(tabel)
    id = int(input("Masukkan ID barang yang ingin dihapus: "))
    tabel.del_row(id)
    print(tabel)
    print("Barang telah dihapus")

def transaksi():
    print(tabel)
    id = int(input("Masukkan ID barang yang igin dibeli: "))
    jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
    for row in tabel:
        if row[0] == id:
            nama = row[1]
            harga = int(row[3])
            total_harga = jumlah * harga
            hasil.add_row([id, nama, jumlah, total_harga])
            print(f"Transaksi Aman. Total harganya segini ya : Rp. {total_harga}")
            break
    else:
        print("ID barang tidak ditemukan / invalid")

while True:
    print("Pilih Role Anda: ")
    print("Ketik 1 Sebagai Admin")
    print("Ketik 2 Sebagai Pembeli")
    print("Ketik 3 Untuk Keluar")
    role = input("Pilih Role 1,2,3: ")

    if role == "1":
        username = input("Masukan Username anda: ")
        password = input("Masukan Password anda: ")
        if username == user ['name'] and password == user['password'] :
            print("Tampilan Admin:")
            print("1. Create Atau Menambah Barang")
            print("2. Read Atau Lihat Barang")
            print("3. Update Atau Mengubah Barang")
            print("4. Delete Atau Hapus Barang")
            tampilan_admin = input("Pilih menu (1/2/3/4): ")
            if tampilan_admin == '1':
                create()
            elif tampilan_admin == '2':
                read()
            elif tampilan_admin == '3':
                update()
            elif tampilan_admin == '4':
                delete()
            else:
                print("Menu tidak valid.")
        else :
            print("Nama Atau Password Error")

    elif role == "2":
        print("Tampilan Pembeli:")
        print("1. Beli Barang")
        print("2. Lihat Transaksi")
        tampilan_pembeli = input("Pilih menu (1/2): ")
        if tampilan_pembeli == '1':
            transaksi()
        elif tampilan_pembeli == '2':
            print(hasil)
        else:
            print("Menu tidak valid.")

    elif role == "3":
        print("Terima Kasih telah mengunjungi")
        break
    else:
        print("Role tidak valid.")
[Flowchart postes 2drawio.pdf](https://github.com/vincenzrey/postes-kedua/files/12850954/Flowchart.postes.2drawio.pdf)
![Diagram Tanpa Judul drawio (2)](https://github.com/vincenzrey/postes-kedua/assets/144880422/d48bc44d-f4c5-4550-a6a5-baac6a03dcb1)
output sebagai admin

![Screenshot 2023-10-10 054819](https://github.com/vincenzrey/postes-kedua/assets/144880422/f00640c6-28c6-4ea1-95bf-7ee589a2dc9b)
setelah login admin dapat masuk ke tampilan ad min dan jika memilih create admin dapat menambahkan barang
![image](https://github.com/vincenzrey/postes-kedua/assets/144880422/19f1480b-76f0-4e91-9373-78ceb193ab8c)
jika admin memilih read maka program akan menampilkan tabel
![image](https://github.com/vincenzrey/postes-kedua/assets/144880422/ef0c6580-806c-4136-87de-4b4d773b351a)
jika admin memilih delete maka admin dapat mendelete tabel dengan memasukan row

output pembeli
![image](https://github.com/vincenzrey/postes-kedua/assets/144880422/02ee9759-c3e9-47d6-86c4-2a0739312560)
output jika pembeli memilih beli barang
![image](https://github.com/vincenzrey/postes-kedua/assets/144880422/64c4ba24-5ba0-4c00-88ed-a4a6c184f8a2)
output jika pembeli memilih tampilkan lihat transaksi

output jika memilih keluar
![image](https://github.com/vincenzrey/postes-kedua/assets/144880422/f9833ba5-bd73-40c8-b4ea-95e4718adbca)





