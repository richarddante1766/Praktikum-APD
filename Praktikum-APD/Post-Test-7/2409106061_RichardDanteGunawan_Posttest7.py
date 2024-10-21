DataUser = {}
pinjaman_terpilih = None
status_login = False

def registrasi_umur():
    umur = int(input("Silahkan masukan umur anda: "))
    if 18 < umur < 66:
        return True
    else:
        print("Maaf, umur anda tidak mencukupi!")
        return False

def buat_akun():
    nama = input("Masukkan nama anda sesuai KTP: ")
    if nama in DataUser:
        print("Nama anda sudah terpakai! Palpalepalelelele :)")
        return False
    else:
        password = input("Silahkan masukan password anda: ")
        huruf_besar = False
        huruf_kecil = False
        angka = False
        karakter_spesial = False
        karakter_spesial_list = "!@#$%^&*(),.?:{}|<>"

        if len(password) < 6:
            print("Password anda harus berisi minimal 6 karakter!")
            return False
        else:
            for char in password:
                if char.isupper():
                    huruf_besar = True
                if char.islower():
                    huruf_kecil = True
                if char.isdigit():
                    angka = True
                if char in karakter_spesial_list:
                    karakter_spesial = True

            if not huruf_besar:
                print("Password harus mengandung huruf besar")
                return False
            elif not huruf_kecil:
                print("Password harus mengandung huruf kecil")
                return False
            elif not angka:
                print("Password harus mengandung angka")
                return False
            elif not karakter_spesial:
                print("Password harus mengandung karakter spesial")
                return False
            else:
                DataUser[nama] = {'password': password, 'pinjaman': []}
                print(f"Akun anda telah terdaftar sebagai {nama} \n")
                return True

def login_menu():
    global pinjaman_terpilih, status_login

    nama = input("Masukkan nama anda sesuai KTP: ")
    password = input("Masukkan password anda: ")
    
    if nama in DataUser and DataUser[nama]['password'] == password:
        status_login = True
        while True:
            print(f"Selamat datang sobat {nama}!")
            print("Silahkan pilih menu di bawah ini!")
            print("1. Membuat pinjaman")
            print("2. Pembayaran cicilan")
            print("3. Informasi cicilan")
            print("4. Exit")
            print()

            status = input("Masukkan menu yang ingin anda lakukan : ")

            if status == "1":
                print("Pilih nominal yang ingin anda pinjam")
                print("A. Rp. 5jt dengan bunga 2% jangka waktu 5 bulan")
                print("B. Rp. 10jt dengan bunga 4% jangka waktu 10 bulan")
                print("C. Rp. 20jt dengan bunga 6% jangka waktu 12 bulan \n")

                pinjaman_terpilih = str.upper(input("Masukkan nominal yang anda inginkan : "))
                print()

                if pinjaman_terpilih == "A":
                    pokok = 5000000
                    bunga = 0.02
                    lama = 5
                elif pinjaman_terpilih == "B":
                    pokok = 10000000
                    bunga = 0.04
                    lama = 10
                elif pinjaman_terpilih == "C":
                    pokok = 20000000
                    bunga = 0.06
                    lama = 12
                else:
                    print("Pilihan tidak valid.")
                    return

                angsuran_bulanan = round((pokok + (pokok * bunga)) / lama)
                total_angsuran = angsuran_bulanan * lama

                DataUser[nama]['pinjaman'].append({
                    'jenis': pinjaman_terpilih, 
                    'total_angsuran': total_angsuran, 
                    'angsuran_bulanan': angsuran_bulanan, 
                    'lama': lama,
                    'bulan_bayar': 0
                })

                print(f"Angsuran bulanan: Rp. {angsuran_bulanan}\n")
                print(f"Total angsuran: Rp. {total_angsuran} \n")

            elif status == "2":
                print("Pembayaran Cicilan")
                if len(DataUser[nama]['pinjaman']) > 0:
                    jenis = str.upper(input("Masukkan jenis pinjaman (A/B/C) : "))
                    if jenis in ['A', 'B', 'C']:
                        for pinjaman in DataUser[nama]['pinjaman']:
                            if pinjaman['jenis'] == jenis:
                                bulan = int(input("Masukkan jumlah bulan yang ingin dibayarkan : "))
                                if bulan + pinjaman['bulan_bayar'] > pinjaman['lama']:
                                    print("Jumlah bulan yang dimasukkan melebihi sisa bulan.")
                                else:
                                    total_bayar = pinjaman['angsuran_bulanan'] * bulan
                                    pinjaman['bulan_bayar'] += bulan
                                    sisa_pembayaran = pinjaman['total_angsuran'] - (pinjaman['bulan_bayar'] * pinjaman['angsuran_bulanan'])
                                    sisa_bulan = pinjaman['lama'] - pinjaman['bulan_bayar']

                                    print("Pembayaran anda telah berhasil!")
                                    print(f"Total pembayaran anda: Rp. {total_bayar}")
                                    print(f"Sisa pembayaran anda: Rp. {sisa_pembayaran}")
                                    print(f"Sisa bulan: {sisa_bulan}")
                                    print()
                    else:
                        print("Jenis pinjaman tidak valid.")
                        return
                else:
                    print("Anda belum mengambil pinjaman.")
                    return

            elif status == "3":
                if len(DataUser[nama]['pinjaman']) > 0:
                    print("Daftar pinjaman Anda:")
                    for idx, pinjaman in enumerate(DataUser[nama]['pinjaman']):
                        sisa_bulan = pinjaman['lama'] - pinjaman['bulan_bayar']
                        if sisa_bulan <= 0:
                            print(f"{idx + 1}. Pinjaman Anda sudah lunas!")
                        else:
                            print(f"{idx + 1}. Jenis: {pinjaman['jenis']}, Total Angsuran: Rp. {pinjaman['total_angsuran']}, Angsuran Bulanan: Rp. {pinjaman['angsuran_bulanan']}, Sisa Bulan: {sisa_bulan}")
                            print()
                else:
                    print("Anda belum mengambil pinjaman.")
                    return
                
            elif status == "4":
                print("Buddy ijin undur diri!")
                print("Terima kasih telah menggunakan Easy Finance!")
                return
            else:
                print("Input tidak valid, silahkan pilih menu 1, 2, 3, atau 4.")
                return
    else:
        print("Nama dan Password anda salah! Silahkan coba lagi. \n")
        return


while True:
    if registrasi_umur():
        print()
        print("Selamat datang sobat Easy Finance!")
        print("Perkenalkan, Saya Buddy sebagai pemandu anda di sini :)")
        print("Silahkan ketik '1' untuk mendaftar akun baru")
        print("Silahkan ketik '2' untuk login ")
        print("Silahkan ketik '3' untuk exit dari program \n")
        opsi = int(input("Silahkan ketuk menu yang anda pilih: "))

        if opsi == 1:
            if buat_akun():
                print("Akun berhasil dibuat!")
            else:
                print("Pembuatan akun gagal!")
        elif opsi == 2:
            login_menu()
        elif opsi == 3:
            print("Terima kasih telah memilih Easy Finance. Semoga harimu menyenangkan :)")
            break
        else:
            print("Input tidak valid. Silahkan coba lagi!")
    else:
        break