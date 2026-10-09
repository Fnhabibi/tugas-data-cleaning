print("=== LAUNDRY BERSIH WANGI PEMALANG ===")

nama = input("Nama pelanggan: ")
berat = float(input("Berat cucian (kg): "))

print("\nPilih Paket:")
print("1. Cuci setrika ekspres - Rp 10000/kg")
print("2. Cuci Setrika reguler - Rp 8000/kg")
print("3. Cuci lipat ekspres  - Rp 8000/kg")
print("4. Cuci lipat reguler - Rp 6000/kg")
print("5. setrika saja - Rp 5000/kg")

pilihan = input("Pilih 1/2/3/4/5: ")

# Tentukan harga pakai IF
if pilihan == "1":
    harga_per_kg = 6000
    paket = "Cuci Kering"
elif pilihan == "2":
    harga_per_kg = 8000
    paket = "Cuci Setrika"
elif pilihan == "3":
    harga_per_kg = 5000
    paket = "Setrika Saja"
else:
    harga_per_kg = 8000
    paket = "Cuci Setrika (Default)"

# Proses hitung
total = berat * harga_per_kg

# Diskon member
member = input("Member? (y/n): ")
if member == "y" or member == "Y":
    diskon = total * 10 / 100
    total_bayar = total - diskon
else:
    diskon = 0
    total_bayar = total

# Cetak Struk
print("\n========== STRUK ==========")
print(f"Pelanggan : {nama}")
print(f"Paket     : {paket}")
print(f"Berat     : {berat} ")
print(f"Harga/kg  : Rp {harga_per_kg}")
print(f"Subtotal  : Rp {int(total)}")
print(f"Diskon    : Rp {int(diskon)}")
print(f"TOTAL BAYAR : Rp {int(total_bayar)}")
print("===========================")
print("Terima kasih! Diambil 2 hari lagi")