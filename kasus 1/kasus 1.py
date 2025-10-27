# Program Pemesanan Tiket Bioskop (Versi if-else)

# 1. Masukkan harga dan diskon
HARGA_REGULER = 50000
HARGA_VIP = 100000
DISKON_MEMBER = 0.20  # 20%

# 2. Input dari user
print("--- Selamat Datang di Program Pemesanan Tiket ---")
tipe_tiket = input("Pilih tipe tiket (reguler/vip): ").lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").lower()

# 3. Proses perhitungan dengan if-else

# Menentukan harga awal berdasarkan tipe tiket
if tipe_tiket == "reguler":
    harga_awal = HARGA_REGULER
elif tipe_tiket == "vip":
    harga_awal = HARGA_VIP
else:
    print("Tipe tiket yang Anda masukkan tidak valid.")
    exit() # Menghentikan program jika input salah

# Menghitung total harga berdasarkan status member
if status_member == "ya":
    total_harga = harga_awal * (1 - DISKON_MEMBER)
    print("Anda mendapatkan diskon 20%!")
elif status_member == "tidak":
    total_harga = harga_awal
else:
    print("Status member yang Anda masukkan tidak valid.")
    exit() # Menghentikan program jika input salah

# 4. Menampilkan hasil akhir
print(f"\n--- Detail Pembayaran ---")
print(f"Tipe Tiket: {tipe_tiket.capitalize()}")
print(f"Harga Awal: Rp{harga_awal:,}")
print(f"Total Harga yang Harus Dibayar: Rp{total_harga:,.0f}")
