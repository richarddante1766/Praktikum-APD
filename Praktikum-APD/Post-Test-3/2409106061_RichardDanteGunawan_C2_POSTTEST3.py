print("Program menghitung harga mobil setelah diskon")

Harga = int(input("Masukkan harga mobil: "))
Jenis = str.upper(input("Masukkan jenis mobil: "))

if Jenis == "TESLA":
    Hasil = Harga - (Harga * 0.17)  
elif Jenis == "HYUNDAI":
    Hasil = Harga - (Harga * 0.21)  
elif Jenis == "TOYOTA":
    Hasil = Harga - (Harga * 0.23)  
else:
    Hasil = None 

if Hasil == None:
    print("Bu Navira tidak jadi membeli mobil.")
else:
    print(f"Bu Navira membeli mobil seharga {Hasil}.")