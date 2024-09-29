Nama=str.lower(input("Masukkan username anda : "))
Nim=int(input("Masukkan password anda : "))
if Nama != "dante" and Nim != 61:
    print ("Maaf anda salah memasukkan username atau password")
    Jawab = str(input("Apakah anda ingin mengulang? "))
    if Jawab == 'tidak':
        exit ()
elif Nama == 'dante' and Nim == 61:
    print ( )
    print("Program menghitung harga mobil setelah diskon")

    Harga = int(input("Masukkan harga mobil : "))
    Jenis = str.upper(input("Masukkan jenis mobil : "))

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
        print ( )
        Respon = input ("Apakah anda ingin berhenti? ")
        if Respon == 'ya':
            exit ()
else:
    print ("Maaf anda salah memasukkan username atau password")
    Jawab = str(input("Apakah anda ingin mengulang? "))
    if Jawab == 'tidak':
        exit ()
    
Jawab = 'ya'
hitung = 1
while (Jawab == 'ya'):
    hitung +=1
    Nama=str.lower(input("Masukkan username anda :"))
    Nim=int(input("Masukkan password anda :"))
    if Nama != "dante" and Nim != 61:
        print ("Maaf anda salah memasukkan username atau password")
        Jawab = str(input("Apakah anda ingin mengulang? "))
        if Jawab == 'tidak':
            exit ()
    elif Nama == 'dante' and Nim == 61:
        print ( )
        print("Program menghitung harga mobil setelah diskon")

        Harga = int(input("Masukkan harga mobil : "))
        Jenis = str.upper(input("Masukkan jenis mobil : "))

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
            print ( )
            Respon = input ("Apakah anda ingin berhenti? ")
            if Respon == 'ya':
                exit ()
    else:
        print ("Maaf anda salah memasukkan username atau password")
        Jawab = str(input("Apakah anda ingin mengulang? "))
        if Jawab == 'tidak':
            exit ()
    if hitung == 3:
        break
