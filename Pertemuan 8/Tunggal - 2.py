angka = [30, 7, 5, 8, 35]

angka_cari = int(input("Masukkan angka yang dicari: "))

if angka_cari in angka:
    print("Angka {} ditemukan.".format(angka_cari))
else:
    print("Angka {} tidak ditemukan.".format(angka_cari))
