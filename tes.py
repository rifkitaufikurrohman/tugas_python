from tabulate import tabulate

# DAFTAR RUTE-JAM-HARGA-TIPE KERETA
ruteKereta = ["Jakarta-Bandung", "Purwokerto-Jogja", "Purwokerto-Bekasi"]
namaKeretaJakba = ["Bandung Jaya", "Bandung Premium", "Bandung Luxury"]
namaKeretaPurJo = ["Purjo Jaya", "Purjo Premium", "Purjo Luxury"]
namaKeretaPurBe = ["Purbe Jaya", "Purbe Premium", "Purbe Luxury"]
tipeKereta = ["Ekonomi", "Ekonomi Premium", "Eksekutif"]
hargaKeretaJakba = [50000, 100000, 150000]
hargaKeretaPurjo = [100000, 150000, 180000]
hargaKeretaPurbe = [150000, 200000, 250000]

jadwalBandungJaya = ["10:15", "12:30", "14:10"]
jadwalBandungPremium = ["11:00", "13:00", "15:00"]
jadwalBandungLuxury = ["12:00", "14:00", "16:00"]
jadwalPurjoJaya = ["07:00", "10:00", "14:00"]
jadwalPurjoPremium = ["08:00", "12:00", "16:00"]
jadwalPurjoLuxury = ["19:00", "12:00", "08:00"]
jadwalPurbeJaya = ["08:00", "12:00", "14:00"]
jadwalPurbePremium = ["10:00", "12:00", "14:00"]
jadwalPurbeLuxury = ["22:00", "12:00", "15:00"]

# DAFTAR KURSI
kursi = [ [4, 50, 8, 42, 10, 64, 31, 35, 1, 9, 13, 11, 19, 20, 12, 14, 16, 40, 21, 25, 24, 26, 30, 25]]

# INISIALISASI
data_diri = ["Nama_lengkap", "Nomor_KTP", "Usia"]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def getRuteKereta():
    result = []

    for i in range(len(ruteKereta)):
        result.append([i + 1, ruteKereta[i]])

    headers = ['No.', 'Rute Kereta']
    table = tabulate(result, headers=headers, tablefmt='rounded_outline', stralign='center')
    print(table)

def getListKereta(namaKereta, hargaKereta):
    result = []
    for i in range(len(namaKereta)):
        result.append([i + 1, namaKereta[i], tipeKereta[i], hargaKereta[i]])
    headers = ['No.', 'Nama Kereta', 'Tipe Kereta', 'Harga Kereta']
    table = tabulate(result, headers=headers, tablefmt='rounded_outline')
    # table = tabulate([], headers=headers, tablefmt='rounded_outline')
    return table

def getJadwalBerangkat(namaKereta, hargaKereta, jadwal, pilihTipeKereta):
    result = []
    for i in range(len(jadwal)):
        result.append([
            i + 1,
            namaKereta[pilihTipeKereta],
            hargaKereta[pilihTipeKereta],  
            tipeKereta[pilihTipeKereta],
            jadwal[i]
        ])
    headers = ['No.', 'Nama Kereta', 'Harga Kereta', 'Tipe Kereta', 'Jam Berangkat']
    table = tabulate(result, headers=headers, tablefmt='rounded_outline')
    return table

# HOME RUTE-TIPE-KURSI-PEMBAYARAN-INVOICE-KERETA
def home():
    print("=========== Selamat Datang Di SePure ===========")
    print("===== Silahkan Pesan Tiket Kereta Api Anda =====\n")
    print("Rute yang tersedia")
    getRuteKereta()
    rute = ""

    namaKereta = []
    hargaKereta = []
    jadwal = []


    # PILIH RUTE
    while True:
        try: 
            pilihRute = int(input("\nPilih Rute sesuai dengan nomor di atas 1-3: "))
            if pilihRute == 1:
                print("\t\t===== Rute Jakarta-Bandung =====")
                print(getListKereta(namaKeretaJakba, hargaKeretaJakba))
                JktBdg = 'Jakarta - Bandung'
                rute = JktBdg
                namaKereta = namaKeretaJakba
                hargaKereta = hargaKeretaJakba
                jadwal = [jadwalBandungJaya, jadwalBandungPremium, jadwalBandungLuxury]
                break

            elif pilihRute == 2:
                print("\t\t===== Rute Purwokerto-Jogja =====")
                print(getListKereta(namaKeretaPurJo, hargaKeretaPurjo))
                PwktJgj = 'Purwokerto - Jogja'
                rute = PwktJgj
                namaKereta = namaKeretaPurJo
                hargaKereta = hargaKeretaPurjo
                jadwal = [jadwalPurjoJaya, jadwalPurjoPremium, jadwalPurjoLuxury]
                break

            elif pilihRute == 3:
                print("\t\t===== Rute Purwokerto-Bekasi =====")
                print(getListKereta(namaKeretaPurBe, hargaKeretaPurbe))
                PwktBks = 'Purwokerto - Bekasi'
                rute = PwktBks
                namaKereta = namaKeretaPurBe
                hargaKereta = hargaKeretaPurbe
                jadwal = [jadwalPurbeJaya, jadwalPurbePremium, jadwalPurbeLuxury]
                break
            else:
                print("Pilih Nomor 1-3!")
        except ValueError : 
            print(f"Inputan kamu tidak valid. Silakan masukkan angka integer antara 1-3.")
    

    # TIPE KERETA
    while True :
        try : 
            pilihTipeKereta = int(input("\nPilih Tipe kereta sesuai dengan nomor di atas 1-3: "))-1
            if pilihTipeKereta in range(3):
                print(f"\t\t===== Tipe {tipeKereta[pilihTipeKereta]} =====")
                print(getJadwalBerangkat(namaKereta, hargaKereta, jadwal[pilihTipeKereta], pilihTipeKereta))
                break
            else:
                print("Pilih Nomor 1-3!")
        except ValueError :
            print(f"Inputan kamu tidak valid. Silakan masukkan angka integer antara 1-3.")
    
    
    # JAM KEBERANGKATAN
    while True:
        try : 
            pilihJamBerangkat = int(input("\nPilih Jam keberangkatan sesuai dengan nomor di atas (1-3): ")) - 1
            if pilihJamBerangkat in range(3):
                jam = jadwal[pilihTipeKereta][pilihJamBerangkat]
                print(f"\nAnda telah memilih jam keberangkatan: {jam}")
                break
            else:
                print("Pilih nomor antara 1 dan 3!")
        except ValueError :
            print(f"Inputan kamu tidak valid. Silakan masukkan angka integer antara 1-3.")
        
    


    # PILIH KURSI
    print("Berikut Pilihan kursi yang tersedia:", kursi[0])
    while True:
        kursis = input("Apakah Anda ingin mengurutkan nomor kursi yang masih tersedia? y/t: ").strip().lower()
        if kursis == 'y':
            kursi_tersedia = selection_sort(kursi[0][:])
            print("Kursi yang tersedia setelah diurutkan:",kursi_tersedia)
            break
        elif kursis == 't':
            break
        else:
            print("Anda harus memasukkan 'y' untuk ya atau 't' untuk tidak. Silakan coba lagi.")


    while True :
        try : 
            pilihKursiKereta = int(input("\nPilih Nomor Kursi Kereta sesuai dengan nomor di atas: "))
            if kursis == 'y':
                if pilihKursiKereta in kursi_tersedia:
                    print(f"Anda telah memilih kursi nomor {pilihKursiKereta}.")
                    break
                else:
                    print("Nomor kursi tidak valid atau sudah dipesan! Silahkan pilih nomor lain.")
            elif kursis == 't':
                if pilihKursiKereta in kursi[0]:
                    print(f"Anda telah memilih kursi nomor {pilihKursiKereta}.")
                    break
            else:
                print("Nomor kursi tidak valid atau sudah dipesan! Silahkan pilih nomor lain.")
        except ValueError : 
            print(f"Inputan kamu tidak valid. Silakan masukkan Nomer kursi yang tersedia")

    # DATA DIRI
    print("\n===== ISI DATA DIRI ANDA =====\n")
    while True:
        Nama = input("Nama Lengkap: ")
        if Nama.strip():
            break
        else:
            print("Masukan Nama Yang Benar!")
    while True : 
        try :
            Nomor_KTP = int(input("Nomor KTP: "))
            break
        except ValueError :
            print(f"Inputan kamu tidak valid. Silakan masukkan angka integer untuk No.KTP")

    while True : 
        try :
            Usia = int(input("Usia: "))
            break
        except ValueError :
            print(f"Inputan kamu tidak valid. Silakan masukkan angka integer untuk Usia")


    # PEMBAYARAN
    total = hargaKereta[pilihTipeKereta]
    print("\n======== Pembayaran Yang Tersedia ========\n")
    print("1. ATM/Banking")
    print("2. GOPAY")
    print("3. OVO")
    print("4. DANA")
    print("5. PAYPAL")
    print(f"\nTotal Rp. {total}\n")

    # LOOPING & ERROR MESSAGE PEMILIHAN METODE BAYAR
    while True:
        try:
            pilihMetode = int(input("Pilih Metode Pembayaran Yang Tersedia (Tekan 1-5): "))
            if pilihMetode not in range(1,6):
                raise ValueError("Pilih 1-5, Silahkan Coba Lagi!")
            break
        except ValueError:
            print(f"Pilih 1-5, Silahkan Coba Lagi!")
    metode_pembayaran = ""

    
    # ATM MOBILE
    if pilihMetode == 1:
        print("\nATM/Mobile Yang Tersedia")
        print("1. ATM BNI")
        print("2. ATM BCA")
        print("3. ATM BSI")
        print("4. ATM BRI")
        print("5. ATM MANDIRI")
        bni = 'BNI Mobile'
        bca = 'BCA Mobile'
        bsi = 'BSI Mobile'
        bri = 'BRI Mobile'
        mandiri = 'Mandiri Mobile'

    # LOOPING & ERROR MESSAGE PEMILIHAN BANK
        while True:
            try:
                pilihATM = int(input("Pilih ATM Yang Tersedia (Tekan 1-5): "))
                if pilihATM not in range(1,6):
                    raise ValueError("Pilih 1-5")
                break
            except:
                print("Masukkan ATM Yang Tersedia")

        # LOOPING & ERROR MESSAGE INPUT PIN ATM
        def pin_ATM(bank):
            while True:
                try:
                    pin = input(f"Masukan 6 Digit PIN {bank} Anda: ")
                    if len(pin) != 6 or not pin.isdigit():
                        raise ValueError
                    pin = int(pin)
                    return
                except ValueError:
                    print("PIN Harus Berupa Angka Dan 6 Digit! Silahkan Coba Lagi")

        if pilihATM == 1 :
            pinATM_1 = pin_ATM(bni)
            metode_pembayaran = bni
            print(f"Pembayaran Berhasil Menggunakan {bni}")

        elif pilihATM == 2 :
            pinATM_2 = pin_ATM(bca)
            metode_pembayaran = bca
            print(f"Pembayaran Berhasil Menggunakan {bca}")

        elif pilihATM == 3 :
            pinATM_3 = pin_ATM(bsi)
            metode_pembayaran = bsi
            print(f"Pembayaran Berhasil Menggunakan {bsi}")

        elif pilihATM == 4 :
            pinATM_4 = pin_ATM(bri)
            metode_pembayaran = bri
            print(f"Pembayaran Berhasil Menggunakan {bri}")

        elif pilihATM == 5 :
            pinATM_5 = pin_ATM(mandiri)
            metode_pembayaran = mandiri
            print(f"Pembayaran Berhasil Menggunakan {mandiri}")
        else:
            print(f"Invalid ATM No {pilihATM} Tidak Tersedia")
            return

    # GOPAY
    elif pilihMetode == 2:
        gopay = 'GoPay'
        # LOOPING & ERROR MESSAGE INPUT PIN GOPAY
        while True:
            try:
                pinGopay = input("\nMasukan 6 Digit PIN GoPay Anda: ")
                if len(pinGopay) != 6 or not pinGopay.isdigit():
                    raise ValueError
                pinGopay = int(pinGopay)
                break
            except ValueError:
                print("PIN GoPay Harus Berupa Angka Dan Berisi 6 Digit! Silahkan Coba Lagi!")
        metode_pembayaran = gopay
        print(f"Pembayaran Berhasil Menggunakan {gopay}")

    # OVO
    elif pilihMetode == 3:
        ovo = 'OVO'
        # LOOPING & ERROR MESSAGE INPUT PIN & NO. OVO
        while True:
            try:
                noOvo = input("\nMasukan 10 - 13 Digit No.HP Akun OVO Anda: ")
                if len(noOvo) < 10 or len(noOvo) > 13 or not noOvo.isdigit():
                    raise ValueError
                noOvo = int(noOvo)
                break
            except ValueError:
                print("No HP Harus Berupa Angka Dan Berisi 10-13 Digit! Silahkan Coba Lagi!")
        while True:
            try:
                pinOvo = input("Masukan 6 Digit PIN OVO Anda: ")
                if len(pinOvo) != 6 or not pinOvo.isdigit():
                    raise ValueError
                pinOvo = int(pinOvo)
                break
            except ValueError:
                print("PIN OVO Harus Berupa Angka Dan Berisi 6 Digit! Silahkan Coba Lagi")
        metode_pembayaran = ovo
        print(f"Pembayaran Berhasil Menggunakan {ovo}")

    # DANA
    elif pilihMetode == 4:
        dana = 'Dana'
        # LOOPING & ERROR MESSAGE INPUT PIN & NO. DANA
        while True:
            try:
                noDana = input("\nMasukan 10-13 Digit No.HP Akun Dana Anda: ")
                if len(noDana) < 10 or len(noDana) > 13 or not noDana.isdigit():
                    raise ValueError
                noDana = int(noDana)
                break
            except ValueError:
                print("No HP Harus Angka Dan Berupa 10-13 Digit! Silahkan Coba Lagi")
        while True:
            try:
                pinDana = input("Masukan 6 Digit PIN Dana Anda: ")
                if len(pinDana) != 6 or not pinDana.isdigit():
                    raise ValueError
                pinDana = int(pinDana)
                break
            except ValueError:
                print("PIN Dana Harus Berupa Angka Dan Berisi 6 Digit! Silahkan Coba Lagi")
        metode_pembayaran = dana
        print(f"Pembayaran Berhasil Menggunakan {dana}")

    # PAYPAL
    elif pilihMetode == 5:
        paypal = 'PayPal'
        akunPaypal = input("Masukan Username PayPal Anda: ")
        # LOOPING & ERROR MESSAGE INPUT PIN PAYPAL
        while True:
            try:
                pinPaypal = input("Masukan 6 Digit PIN PayPal Anda:  ")
                if len(pinPaypal) != 6 or not pinPaypal.isdigit():
                    raise ValueError
                pinPaypal = int(pinPaypal)
                break
            except ValueError:
                print("PIN PayPal Harus Berupa Angka Dan Berisi 6 Digit! Silahkan Coba Lagi")
        metode_pembayaran = paypal
        print(f"Pembayaran Berhasil Menggunakan {akunPaypal} {paypal}")

    else:
        print("Invalid Masukan Metode Pembayaran Yang Tersedia Waktu Pemesanan Kadaluwarsa")
        return
    

    # INVOICE
    print("\nProcessing......\n")
    print(35*"=")
    print("    Invoice Tiket Kereta Api")
    print(35*"=")
    print(" PEMBAYARAN BERHASIL")
    print(f"\n Nama Pemesan: {Nama} ")
    print(f" Nomor KTP: {Nomor_KTP}")
    print(f" Usia: {Usia} Tahun ")
    print(f" Rute: {rute} ")
    print(f"\n Waktu Keberangkatan: {jam} ")
    print(f" Nama Kereta: {namaKereta[pilihTipeKereta]} ")
    print(f" Tipe Kereta: {tipeKereta[pilihTipeKereta]} ")
    print(f" Tempat Duduk: {pilihKursiKereta} ")
    print(f"\n Metode Pembayaran: {metode_pembayaran} ")
    print(f" Total: Rp. {total} ")
    print(35*"=")

# LOOPING IF YES    
pesan_lagi = True
while pesan_lagi:
    home()
    while True:
        pemesananLagi = input("Apakah Anda Ingin Melakukan Pemesanan Lagi? (y/t): ")
        if pemesananLagi == 'y':
            break
        elif pemesananLagi == 't':
            print("Terima Kasih Telah Menggunakan Layanan Se-Pure!")
            pesan_lagi = False
            break
        else :
            print("Error Mohon Input (y/t)!")