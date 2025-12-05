# Sistem Inventaris Barang Sederhana

# Fungsi tambah barang
def tambah_barang(inventaris):
    nama = input("Nama barang: ")
    jumlah = int(input("Jumlah: "))
    harga = int(input("Harga: "))
    
    barang = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
    inventaris.append(barang)
    print("Barang berhasil ditambahkan!")

# Fungsi lihat barang
def lihat_barang(inventaris):
    if not inventaris:
        print("Inventaris kosong.")
    else:
        print("\nDaftar Barang:")
        for i, barang in enumerate(inventaris, start=1):
            print(f"{i}. {barang['nama']} - Jumlah: {barang['jumlah']} - Harga: {barang['harga']}")

# Fungsi edit barang
def edit_barang(inventaris):
    lihat_barang(inventaris)
    if inventaris:
        nomor = int(input("Nomor barang: ")) - 1
        if 0 <= nomor < len(inventaris):
            inventaris[nomor]['nama'] = input("Nama baru: ")
            inventaris[nomor]['jumlah'] = int(input("Jumlah baru: "))
            inventaris[nomor]['harga'] = int(input("Harga baru: "))
            print("Barang berhasil diedit!")
        else:
            print("Nomor tidak valid.")

# Fungsi hapus barang
def hapus_barang(inventaris):
    lihat_barang(inventaris)
    if inventaris:
        nomor = int(input("Nomor barang: ")) - 1
        if 0 <= nomor < len(inventaris):
            barang = inventaris.pop(nomor)
            print(f"Barang '{barang['nama']}' dihapus!")
        else:
            print("Nomor tidak valid.")
