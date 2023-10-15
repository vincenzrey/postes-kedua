from prettytable import PrettyTable
global tabel
user = {'name' : 'Vincenz', 'password':'semangatkerja', 'Role' : '1'}


tabel = PrettyTable()
tabel.field_names = ["ID", "Nama Barang", "Merk", "Harga"]
tabel.add_row ([1, "Helm Safety", "USA", "Rp. 25000"])
tabel.add_row ([2, "Wearpack", "ASGARD", "Rp. 120000"])
tabel.add_row ([3, "Rompi", "GO SAVE", "Rp. 20.000"]),
tabel.add_row ([4, "Sarung Tangan", "MATAHARI", "Rp. 30.000"])
tabel.add_row ([5, "Sepatu Safety", "CHEETAH", "Rp. 425.000"])
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
        if id == row[0] :
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