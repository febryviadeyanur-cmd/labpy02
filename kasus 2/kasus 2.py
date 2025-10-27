# Program Kalkulator Sederhana
# Menerima dua angka dan operator aritmatika

# Meminta input dari user
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

# Menggunakan if-else-elif untuk menentukan operasi
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil penjumlahan: {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil pengurangan: {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil perkalian: {hasil}")
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil pembagian: {hasil}")
    else:
        print("Error: Pembagian oleh nol tidak diperbolehkan.")
else:
    print("Operator tidak valid. Gunakan +, -, *, atau /.")
