def sum_data(*angka):
    hasil = 0
    for i in angka:
        hasil = hasil + i
    return (angka, hasil)

angka, hasil = sum_data(10, 5, 20, 203203)
print(f"angka = {angka}, jika di jumlahkan maka hasilnya = {hasil}")