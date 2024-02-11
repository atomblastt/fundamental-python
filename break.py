print("Check apakah inputan angka genap atau tidak")

while True:
    data = int(input("Masukkan angka: "))
    if data % 2 == 0:
        print(f"Selamat {data} adalah angka genap")
        break
    else:
        print(f"{data} bukan angka genap, coba lagi")
