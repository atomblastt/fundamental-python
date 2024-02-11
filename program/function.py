# list siswa
def list_siswa(siswa):
    for data in siswa:
        print("======================")
        print(f"    Nama : {data['nama']}")
        print(f"    Umur : {data['umur']}")
        print(f"    Email : {data['email']}")
        print("")

# info detil siswa
def detail_siswa(siswa):
    email = input("Masukan email siswa yang ingin di edit : ")

    index = -1

    for i in range(0, len(siswa)):
        dataSiswa = siswa[i]
        if email == dataSiswa['email']:
            index = i
            break
        
    if index == -1:
        print("")
        print("======================")
        print(f"siswa dengan email {email} tidak di temukan")
        print("")
    else:
        print("")
        print("======================")
        print(f"Detail siswa dengan email {email}")
        print("======================")
        print(f"    Nama : {siswa[i]['nama']}")
        print(f"    Umur : {siswa[i]['umur']}")
        print(f"    Email : {siswa[i]['email']}")
        print("")

# tambah siswa
def tambah_siswa():
    nama = input("nama : ")
    umur = input("umur : ")
    email = input("email : ")
    siswa = {
        "nama" : nama,
        "umur" : umur,
        "email" : email,
    }
    print("")
    print("======================")
    print(f"data {siswa['nama']} berhasil di tambahkan")
    print("")
    return siswa

# edit siswa
def edit_siswa(siswa):
    email = input("Masukan email siswa yang ingin di edit : ")

    index = -1

    for i in range(0, len(siswa)):
        dataSiswa = siswa[i]
        if email == dataSiswa['email']:
            index = i
            break
    
    if index == -1:
        print("")
        print("======================")
        print(f"siswa dengan email {email} tidak di temukan")
        print("")
    else:
        siswa[index]['nama'] = input("nama : ")
        siswa[index]['umur'] = input("umur : ")
        siswa[index]['email'] = input("email : ")

        print("")
        print("======================")
        print(f" data {email} berhasil di edit")
        print("")

# hapus siswa
def hapus_siswa(siswa):
    email = input("Masukan email siswa yang ingin di hapus : ")

    index = -1

    for i in range(0, len(siswa)):
        dataSiswa = siswa[i]
        if email == dataSiswa['email']:
            index = i
            break
    
    if index == -1:
        print("")
        print("======================")
        print(f"siswa dengan email {email} tidak di temukan")
        print("")
    else:
        del siswa[index]
        print("")
        print("======================")
        print(f"{email} berhasil di hapus")
        print("")
