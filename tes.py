from tabulate import tabulate

ruteKereta = ["Jakarta-Bandung", "Purwokerto-Jogja", "Purwokerto-Bekasi"]
namaKeretaJakba = ["Bandung Jaya", "Bandung Premium", "Bandung Luxury"]
namaKeretaPurJo = ["Purjo Jaya", "Purjo Premium", "Purjo Luxury"]
namaKeretaPurBe = ["Purbe Jaya", "Purbe Premium", "Purbe Luxury"]
tipeKereta = ["Ekonomi", "Ekonomi Premium", "Eksekutif"]
hargaKeretaJakba = [50000, 100000, 150000]
hargaKeretaPurjo = [100000, 150000, 180000]
hargaKeretaPurbe = [150000, 200000, 250000]


def getRuteKereta() :
  result = []

  for i in range (len(ruteKereta)) :
    result.append([i + 1, ruteKereta[i]])

  headers = ['No.', 'Rute Kereta',]
  table = tabulate(tabular_data=result, headers=headers, tablefmt='rounded_outline', stralign='center')
  print(table)

def getListKereta(namaKereta, hargaKereta) :
  result = []
  for i in range(len(namaKereta)):
    result.append([i + 1, namaKereta[i], tipeKereta[i], hargaKereta[i]])
  
  headers = ['No.', 'Nama Kereta', 'Tipe Kereta', 'Harga Kereta']
  table = tabulate(tabular_data=result, headers=headers, tablefmt='rounded_outline')
  # table = tabulate([], headers=headers, tablefmt='rounded_outline')

  return table


def home() :
  dataPesanan = []
  print("\t===== Selamat Datang =====")
  print("===== Silahkan Pesan Tiket kereta Api Anda =====\n")

  print("Rute yang tersedia")
  getRuteKereta()

  pilihRute = int(input("\nPilih Rute sesuai dengan nomor di atas 1-3 : "))


  jamBerangkat = float(input("\nMasukkan jam keberangkatan (dari 00.00 sampai 23.59) : "))
  dataPesanan.append([pilihRute, jamBerangkat])

  if pilihRute == 1 :
    print("\t\t===== Rute Jakarta-Bandung =====")
    print(getListKereta(namaKeretaJakba, hargaKeretaJakba))
  elif pilihRute == 2 :
    print("\t\t===== Rute Purwokerto-Jogja =====")
    print(getListKereta(namaKeretaPurJo, hargaKeretaPurjo))
  elif pilihRute == 3 :
    print("\t\t===== Rute Purwokerto-Bekasi =====")
    print(getListKereta(namaKeretaPurBe, hargaKeretaPurbe))
  else :
    print("Pilih Nomer 1-3 !")

  print(f"{dataPesanan}")

home()
