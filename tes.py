from tabulate import tabulate

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

kursi = [ [4, 50, 8, 42, 10, 64, 31, 35, 1, 9, 13, 11, 19, 20, 12, 14, 16, 40, 21, 25, 24, 26, 30, 25]]

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

def home():
    print("\t===== Selamat Datang =====")
    print("===== Silahkan Pesan Tiket Kereta Api Anda =====\n")
    print("Rute yang tersedia")
    getRuteKereta()

    pilihRute = int(input("\nPilih Rute sesuai dengan nomor di atas 1-3: "))
    if pilihRute == 1:
        print("\t\t===== Rute Jakarta-Bandung =====")
        print(getListKereta(namaKeretaJakba, hargaKeretaJakba))
        namaKereta = namaKeretaJakba
        hargaKereta = hargaKeretaJakba
        jadwal = [jadwalBandungJaya, jadwalBandungPremium, jadwalBandungLuxury]
    elif pilihRute == 2:
        print("\t\t===== Rute Purwokerto-Jogja =====")
        print(getListKereta(namaKeretaPurJo, hargaKeretaPurjo))
        namaKereta = namaKeretaPurJo
        hargaKereta = hargaKeretaPurjo
        jadwal = [jadwalPurjoJaya, jadwalPurjoPremium, jadwalPurjoLuxury]
    elif pilihRute == 3:
        print("\t\t===== Rute Purwokerto-Bekasi =====")
        print(getListKereta(namaKeretaPurBe, hargaKeretaPurbe))
        namaKereta = namaKeretaPurBe
        hargaKereta = hargaKeretaPurbe
        jadwal = [jadwalPurbeJaya, jadwalPurbePremium, jadwalPurbeLuxury]
    else:
        print("Pilih Nomor 1-3!")
        return

    pilihTipeKereta = int(input("\nPilih Tipe kereta sesuai dengan nomor di atas 1-3: "))-1

    if pilihTipeKereta in range(3):
        print(f"\t\t===== Tipe {tipeKereta[pilihTipeKereta]} =====")
        print(getJadwalBerangkat(namaKereta, hargaKereta, jadwal[pilihTipeKereta], pilihTipeKereta))
    else:
        print("Pilih Nomor 1-3!")
        return
    pilihJamBerangkat = int(input("\nPilih Jam keberangkatan sesuai dengan nomor di atas: ")) - 1
    if pilihJamBerangkat in range(3):
        print(f"\nAnda telah memilih jam keberangkatan: {jadwal[pilihTipeKereta][pilihJamBerangkat]}")

    print("Berikut Pilihan kursi yang tersedia:", kursi[0])

    while True:
        kursis = input("Apakah kamu ingin mengurutkan nomor kursi yang masih tersedia? y/t: ").strip().lower()
        if kursis == 'y':
            kursi_tersedia = selection_sort(kursi[0][:])
            print("Kursi yang tersedia setelah diurutkan:",kursi_tersedia)
            break
        elif kursis == 't':
            break
        else:
            print("Anda harus memasukkan 'y' untuk ya atau 't' untuk tidak. Silakan coba lagi.")
    while True :
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

home()
