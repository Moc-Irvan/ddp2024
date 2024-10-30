#Soal No 1
# Buat variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, WarnaKendaraan, Rodakendaraan]
print("Point A")
Kendaraan = ['Honda Vario', 'Sepeda Motor', 120, 'Hitam', 2]
print("My vihacle :")
print(Kendaraan)

# Tambahkan dari list tersebut dibelakang dengan value : [harga kendaraan, tipe kendaraan]
print("Point B")
Kendaraan.append(15000000)
print(Kendaraan)

# Tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
print("Point C")
Kendaraan.insert(2,'Honda')
print(Kendaraan)

#Soal No 2
#Buat program python dengan match case untuk menghitung luas bangun datar :
#Jika pilih 1, maka menghitung luas persegi 
#Jika pilih 2, maka menghitung luas lingkaran
#Jika pilih 3, maka menghitung luas segitiga
print ( 'Cara untuk menghitung luas bangun datar')
print ( "Pilih Menu angka 1-3 : \n1. Persegi \n2. Lingkaran \n3. Segitiga")
pilihmenu = int(input("Silahkan pilih menun dengan mengetikan angka 1-3 :"))

match pilihmenu :
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input( "Masukan nilai yang mau dihitung :"))
        hitung = sisi * sisi 
        print(f"Luas Persegi adalah : {hitung}")
    case 2:
        print("Ini adalah menu untuk menghitung luas Lingkaran")
        r = int(input( "Masukan nilai yang mau dihitung :"))
        hitung = 22/7 * r**2
        print(f"Luas Persegi adalah : {hitung}")
    case 3:
        print("Ini adalah menu untuk menghitung luas segitiga")
        Alas = int(input( "Masukan nilai Alasnya :"))
        Tinggi = int(input( "Masukan nilai Tingginya :"))
        hitung = 1/2 * Alas * Tinggi
        print(f"Luas Persegi adalah : {hitung}")
    case _:
        print("pilihan tidak valid, silahkan pilih antara 1-3")