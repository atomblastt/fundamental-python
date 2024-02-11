# angka = int(input('masukan angka yang ingin di check : '))

# def check_data_genap(angka):
#     if angka % 2 == 0:
#         return True
    
# while True:
#     if check_data_genap(angka) == True:
#         print(f"SELAMAT, {angka} adalah bilangan genap")
#         break
#     else:
#         angka = int(input(f'{angka} bukan angka genap, masukan angka lagi : '))

def check_data_genap(angka = 1):
    return angka % 2 == 0

angka = int(input('Masukkan angka yang ingin dicek: '))

while not check_data_genap(angka):
    angka = int(input(f'{angka} bukan angka genap, masukkan angka lagi: '))

print(f'SELAMAT, {angka} adalah bilangan genap')

