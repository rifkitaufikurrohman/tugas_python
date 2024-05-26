# Contoh data jadwal
jadwal = [
    ["06:00", "09:00", "12:00"],  # Jadwal untuk tipe kereta 1
    ["07:00", "10:00", "13:00"],  # Jadwal untuk tipe kereta 2
    ["08:00", "11:00", "14:00"]   # Jadwal untuk tipe kereta 3
]

# Misalkan pengguna memilih tipe kereta ke-1 (indeks 0)
pilihTipeKereta = 0

# JAM KEBERANGKATAN
# while True:
#     try:
#         pilihJamBerangkat = int(input("\nPilih Jam keberangkatan sesuai dengan nomor di atas (1-3): ")) - 1
#         if pilihJamBerangkat in range(3):
#             jam = jadwal[pilihTipeKereta][pilihJamBerangkat]
#             print(f"\nAnda telah memilih jam keberangkatan: {jam}")
#             break
#         else:
#             print("Pilih nomor antara 1 dan 3!")
#     except ValueError:
#         print("Masukkan angka yang valid!")

while True :
    pilihTipeKereta = int(input("\nPilih Tipe kereta sesuai dengan nomor di atas 1-3: "))-1

    if pilihTipeKereta in range(3):
        print(f"\t\t===== Tipe {tipeKereta[pilihTipeKereta]} =====")
        print(getJadwalBerangkat(namaKereta, hargaKereta, jadwal[pilihTipeKereta], pilihTipeKereta))
        break
    else:
        print("Pilih Nomor 1-3!")
    