#1. Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. fungsi ini harus 
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius) :
    fahrenheit=(celcius*9/5)+32 # mengkonversi suhu dari celcius ke fahrenheit
    return fahrenheit # mengebalikan nilai fahrenheit 

suhu_celcius1 = 0
suhu_celcius2 = 100
# cetak 0 celcius ke 32 fahrenheit
suhu_fahrenheit1 = celcius_ke_fahrenheit (suhu_celcius1)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)

#  cetak 100 celcius ke 212 fahrenheit
suhu_fahrenheit2 = celcius_ke_fahrenheit (suhu_celcius2)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan) :
    hitung = bilangan % 2 == 0 # menentukan bilangan ganjil atau genap
    return hitung # mengebalikan nilai hitung 

angka = 4 # mendefenisi bilangan
hasil = genap_ganjil(angka) # memanggil fungsi 
print(f"bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"bilangan {angka2} bernilai {hasil2}")

print()
print('## Nomor 3 ##')
def cek_kelulusan(nilai) :
    if nilai > 60 :
        return 'anda lulus'
    else :
        return 'anda gagal'
    
nilai1 = 60
status = cek_kelulusan(nilai1)
print(f"nilai: {nilai1}, status: {status}")
nilai2 = 80
status = cek_kelulusan(nilai2)
print(f"nilai: {nilai2}, status: {status}")

print()
print('## Nomor 4 ##')
def ganjil():
    for i in range(0, angka):
        if i % 2 != 0:
            print(i, end="")

angka = 20
print("angka ganjil dari angka 0 ke ", angka)
ganjil()

