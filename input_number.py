print("Kalkulator Tambah")

# Validasi input angka pertama
while True:
    try:
        a = int(input("Masukkan angka pertama: "))
        break  # Keluar dari loop jika input valid
    except ValueError:
        print("Inputan Pertama harus berupa angka. Coba lagi.")

# Validasi input angka kedua
while True:
    try:
        b = int(input("Masukkan angka kedua: "))
        break  # Keluar dari loop jika input valid
    except ValueError:
        print("Inputan Kedua harus berupa angka. Coba lagi.")

hasil = a + b
print(f"Hasil dari {a} + {b} = {hasil}")
