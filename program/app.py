# Membuat daftar siswa
import function
siswa = []
siswa.append({
    "nama" : "Test",
    "umur" : "20",
    "email" : "test@mail.com",
})

while True:
    print("1. List siswa")
    print("2. Info detil siswa")
    print("3. Pendaftaran siswa baru")
    print("4. Update data siswa")
    print("5. Hapus data siswa")
    print("0. Keluar")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.list_siswa(siswa)
    elif menu == "2":
        function.detail_siswa(siswa)
    elif menu == "3":
        tambah_siswa = function.tambah_siswa()
        siswa.append(tambah_siswa)
    elif menu == "4":
        function.edit_siswa(siswa)
    elif menu == "5":
        function.hapus_siswa(siswa)

print("====================================")
print("Terimakasih, jumpa lagi ya... :)")
print("====================================")