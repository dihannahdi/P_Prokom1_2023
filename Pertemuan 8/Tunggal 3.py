angka = [1, 3, 5, 7, 9]

angka_balik = []

for i in range(len(angka) - 1, -1, -1):
    angka_balik.append(angka[i])

for i in range(len(angka)):
    angka_balik[i] = angka_balik[i] + 1

print(angka_balik)
