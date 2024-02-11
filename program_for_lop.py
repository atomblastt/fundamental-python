banyakData = int(input("berapa banyak jumlah data orang yang ingin di buat ? "))

nama = []
umur = []

for i in range(0, banyakData):
    print(f"data ke {i}")
    data_nama = input("nama : ")
    data_umur = int(input("umur : "))

    nama.append(data_nama)
    umur.append(data_umur)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun")