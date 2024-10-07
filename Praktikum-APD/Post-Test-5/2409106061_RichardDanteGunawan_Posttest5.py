DataUser = []

while True:
    print("Halo! Selamat datang di aplikasi Easy Finance")
    print("Silahkan lakukan registrasi umur terlebih dahulu \n")
    umur = int(input("Silahkan masukan umur anda: "))
    
    if 18 < umur < 66:
        print()
        print("Selamat datang sobat Easy Finance!")
        print("Perkenalkan, Saya Buddy sebagai pemandu anda di sini :)")
        print("Silahkan ketik '1' untuk mendaftar akun baru")
        print("Silahkan ketik '2' untuk login ")
        print("Silahkan ketik '3' untuk exit dari program \n")
        opsi = int(input("Silahkan ketuk menu yang anda pilih: "))

        if opsi == 1:
            print("Halo pengguna baru! Ayo buat akun dulu :V")
            nama = input("Masukkan nama anda sesuai KTP: ")
            nama1 = False
            for i in DataUser:
                if i[0] == nama:
                    nama1 = True
                    break
            if nama1:
                print("Nama anda sudah terpakai! Palpalepalelelele :)")
            else:
                password = input("Silahkan masukan password anda: ")
                huruf_besar = False
                huruf_kecil = False
                angka = False
                karakter_spesial = False
                karakter_spesial = "!@#$%^&*(),.?:{}|<>"
                
                if len(password) < 6:
                    print("Password anda harus berisi minimal 6 karakter!")
                else:
                    for char in password:
                        if char.isupper():
                            huruf_besar = True
                        if char.islower():
                            huruf_kecil = True
                        if char.isdigit():
                            angka = True
                        if char in karakter_spesial:
                            karakter_spesial = True

                    if not huruf_besar:
                        print("Password harus mengandung huruf besar")
                    elif not huruf_kecil:
                        print("Password harus mengandung huruf kecil")
                    elif not angka:
                        print("Password harus mengandung angka")
                    elif not karakter_spesial:
                        print("Password harus mengandung karakter spesial")
                    else:
                        DataUser.append([nama, password, []])
                        print(f"Akun anda telah terdaftar sebagai {nama} \n")

        elif opsi == 2:
            print("Silahkan login dulu, ya, Sobat :)")
            nama = input("Masukkan nama anda sesuai KTP: ")
            password = input("Masukkan password anda: ")
            for i in DataUser:
                if i[0] == nama and i[1] == password:
                    while True:
                        print(f"Selamat datang sobat {nama}!")
                        print("Silahkan pilih menu di bawah ini!")
                        print("1. Membuat pinjaman")
                        print("2. Pembayaran cicilan")
                        print("3. Informasi cicilan")
                        print("4. Exit")
                        print()

                        status = input("Masukkan menu yang ingin anda lakukan : ")
                        print(" ")

                        if status == "1":
                            print("Pilih nominal yang ingin anda pinjam")
                            print("A. Rp. 5jt dengan bunga 2% jangka waktu 5 bulan")
                            print("B. Rp. 10jt dengan bunga 4% jangka waktu 10 bulan")
                            print("C. Rp. 20jt dengan bunga 6% jangka waktu 12 bulan \n")

                            pinjaman = str.upper(input("Masukkan nominal yang anda inginkan : "))
                            print(" ")

                            if pinjaman == "A":
                                pokok = 5000000
                                bunga = 0.02
                                lama = 5
                            elif pinjaman == "B":
                                pokok = 10000000
                                bunga = 0.04
                                lama = 10
                            elif pinjaman == "C":
                                pokok = 20000000
                                bunga = 0.06
                                lama = 12
                            else:
                                print("Pilihan tidak valid.")
                                continue

                            angsuran_bulanan = round((pokok + (pokok * bunga)) / lama)
                            total_angsuran = angsuran_bulanan * lama

                            i[2].append({
                                'jenis': pinjaman, 
                                'total_angsuran': total_angsuran, 
                                'angsuran_bulanan': angsuran_bulanan, 
                                'lama': lama,
                                'bulan_bayar': 0
                            })

                            print(f"Angsuran bulanan: Rp. {angsuran_bulanan}\n")
                            print(f"Total angsuran: Rp. {total_angsuran} \n")

                        elif status == "2":
                            print("Pembayaran Cicilan")
                            if len(i[2]) > 0:
                                jenis = str.upper(input("Masukkan jenis pinjaman (A/B/C) : "))
                                if jenis in ['A', 'B', 'C']:
                                    for pinjaman in i[2]:
                                        if pinjaman['jenis'] == jenis:
                                            bulan = int(input("Masukkan jumlah bulan yang ingin dibayarkan : "))
                                            if bulan + pinjaman['bulan_bayar'] > pinjaman['lama']:
                                                print("Jumlah bulan yang dimasukkan melebihi sisa bulan.")
                                            else:
                                                angsuran_bulanan = pinjaman['angsuran_bulanan']
                                                pinjaman['bulan_bayar'] += bulan
                                                total_bayar = angsuran_bulanan * bulan
                                                sisa_pembayaran = pinjaman['total_angsuran'] - (pinjaman['bulan_bayar'] * angsuran_bulanan)
                                                sisa_bulan = pinjaman['lama'] - pinjaman['bulan_bayar']

                                                print("Pembayaran anda telah berhasil!")
                                                print(f"Total pembayaran anda: Rp. {total_bayar}")
                                                print(f"Sisa pembayaran anda: Rp. {sisa_pembayaran}")
                                                print(f"Sisa bulan: {sisa_bulan}")
                                                print()
                                            break
                                    else:
                                        print("Jenis pinjaman tidak valid.")
                                else:
                                    print("Jenis pinjaman tidak valid.")
                            else:
                                print("Anda belum mengambil pinjaman.")

                        elif status == "3":
                            if len(i[2]) > 0:
                                print("Daftar pinjaman Anda:")
                                for idx in range(len(i[2])):
                                    pinjaman = i[2][idx]
                                    sisa_bulan = pinjaman['lama'] - pinjaman['bulan_bayar']
                                    if sisa_bulan <= 0:
                                        print(f"{idx + 1}. Pinjaman Anda sudah lunas!")
                                    else:
                                        print(f"{idx + 1}. Jenis: {pinjaman['jenis']}, Total Angsuran: Rp. {pinjaman['total_angsuran']}, Angsuran Bulanan: Rp. {pinjaman['angsuran_bulanan']}, Sisa Bulan: {sisa_bulan}")
                                        print()
                            else:
                                print("Anda belum mengambil pinjaman.")
                            
                        elif status == "4":
                            print("Terima kasih telah menggunakan Easy Finance!")
                            break
                        else:
                            print("Input tidak valid, silahkan pilih menu 1, 2, 3, atau 4.")
                            break
            else:
                print ("Nama dan Password anda salah! Silahkan coba lagi. \n")
        
        elif opsi == 3:
            print("Apakah anda ingin keluar dari aplikasi?")
            print ("1. Iya")
            print ("2. Tidak")
            keluar = input ("Input pilihan:")
            print ("")
            if keluar == "1":
                print ("Terima kasih telah memilih Easy Finance. Semoga harimu menyenangkan :)")
                break
            elif keluar == "2":
                continue
            else: 
                print ("Input tidak valid. Silahkan coba lagi!")
        else:
            print ("Input tidak valid. Silahkan coba lagi!")
    else:
        print("Maaf, umur anda tidak mencukupi!")
        exit()
