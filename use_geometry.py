# from geometry.segitiga import hitung_luas_segitiga
# import geometry.segitiga as gs
from geometry.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometry.persegi_panjang import hitung_luas_persegi_panjang, info as info_persegi_panjang

print(info_segitiga())
print(f'hitung_luas_segitiga {hitung_luas_segitiga(10, 3)}')

print(info_persegi_panjang())
print(f'hitung_luas_persegi_panjang {hitung_luas_persegi_panjang(10, 3)}')