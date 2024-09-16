print("Posttest 2")

X = str(input("Masukkan Nama: "))
Y = int(input("Masukkan NIM: "))
Z = int(input("Masukkan harga setiap mobil: "))

A = Z - (Z * 0.17)
B = Z - (Z * 0.21)
C = Z - (Z * 0.23)
D = Z % 7

print(f"Mobil Tesla seharga {Z} diskon 17% menjadi {A}, Mobil Toyota seharga {Z} diskon 21% menjadi {B}, Mobil Hyundai seharga {Z} diskon 23% menjadi {C}, dan {Z} modulus 7 adalah {D}.")