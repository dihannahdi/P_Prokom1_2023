# Pre Declaration

barang = {}
inputed = 1

# Program untuk bisnis

def BEP(mod, lab):      # Progarm yang menghitung Break Even Point (BEP) yang berarti suatu 
                        # titik impas adalh posisi dimana laba yang didapatkan mempunyai nilai setara dengan 
                        # yang diperlukan dalam sebuah usaha. Bisa juga disebut dengan tidak mengalami kerugian                 
    if(mod == 0):       # Jika tidak ada modal, bisnis tidak bisa dimulai
        return("Bisnis tidak bisa dimulai.")
    elif(lab == 0):     # Jika tidak ada laba, BEP tidak akan tercapai
        return("Nilai BEP Tidak akan tercapai.")
    else:               # Selain itu, maka BEP bisa dihitung
        coba = int(input("Ada berapa opsi modal lain yang anda sediakan? "))
        for i in range(1, coba + 1):
            mod = int(input("Masukkan nilai modal ke-%d anda: " % (i)))
            hasil = mod / laba(stok_awal, stok_akhir, harga_beli, harga_jual)               # BEP = modal dibagi pengurangan antara
                                                                                            # harga beli dan harga jual
            print("Bisnis akan mencapai BEP saat produksi barang sejumlah %d buah" % (hasil))
    
# Fungsi menghitung Stok Keluar 
def stok_keluar(a, b, pemasukan):
    
    if(a <= 0):         # Jika stok awal kurang dari 0, berarti kekurangan stok
     return a
    elif(a == b):       # Jika stok awal sama dengan stok akhir, berarti tidak ada stok keluar
        return 0
    elif(b > a):        # Jika stok akhir lebih dari stok awal, berarti stoknya bertambah 
        return 0
    else:               # Selain itu, artinya ada pengurangan stok
        pilihan = input("Apakah ingin mengubah harga? [Y/N]: ")
        if(pilihan == 'N'):
            pass
        else:
            awal = int(input("Masukkan harga awal: "))
            akhir = int(input("Masukkan harga akhir: "))
        pemasukan = akhir-awal
        for i in range(0, abs(b-a)):    
            pemasukan += pemasukan
            print("Pemasukan pada barang ke-%d adalah %d" % (i, pemasukan))
        return(abs(b-a))

def laba(a, b, x, y):
    pemasukan = y-x
    c = stok_keluar(stok_awal, stok_akhir, pemasukan)
    if(c <= 0):
        return("Tidak ada barang yang akan dijual")
    elif(x == y):
        return("Tidak ada keuntungan")
    else:
        pilihan2 = input("Apakah ingin mengubah stok masuk dan keluar? [Y/N]: ")
        if(pilihan2 == 'N'):
            pass
        else:
            a = int(input("Masukkan stok barang masuk yang baru: "))
            b = int(input("Masukkan stok barang keluar yang baru: "))
        akhir = c * abs(x - y)
        labs = 0
        for i in range(0, abs(a-b)):
            labs += abs(x-y)
            print("Laba pada barang ke-%d adalah %d" % (i, labs))
        return akhir
    
stok_awal = int(input("Masukkan jumlah stok awal: "))
stok_akhir = int(input("Masukkan jumlah stok akhir: "))
harga_beli = int(input("Masukkan jumlah harga beli: "))
harga_jual = int(input("Masukkan jumlah harga jual: "))
modal = int(input("Masukkan modal: "))

print("---")
print(BEP(modal, laba(stok_akhir, stok_awal, harga_beli, harga_jual)))
print("---")