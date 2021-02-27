"""
Program menghitung luas segitiga
Luas segitiga = alas * tinggi / 2
"""
print('Menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga dengan alas={alas} dan tinggi={tinggi} memilki luas {luas_segitiga}')

print('\nMenghitung luas segitiga dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga dengan alas={alas} dan tinggi={tinggi} memilki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung luas segitiga dengan fungsi hasilnya = {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung luas segitiga dengan fungsi hasilnya = {hitung_luas_segitiga(20, 2)}')
print(f'Menghitung luas segitiga dengan fungsi hasilnya = {hitung_luas_segitiga(30, 5)}')
