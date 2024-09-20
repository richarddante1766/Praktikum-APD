print("Program menghitung harga mobil setelah diskon")

A = int(input("Masukkan harga mobil: "))
B = str.upper(input("Masukkan jenis mobil: "))

if B == "TESLA":
    C = A - (A * 0.17)  
elif B == "HYUNDAI":
    C = A - (A * 0.21)  
elif B == "TOYOTA":
    C = A - (A * 0.23)  
else:
    C = None 

if C == None:
    print("Bu Navira tidak jadi membeli mobil.")
else:
    print(f"Bu Navira membeli mobil seharga {C}.")
    