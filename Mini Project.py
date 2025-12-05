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
