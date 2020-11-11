def tambah(x, y):
   return x + y
def kurang(x, y):
   return x - y
def bagi(x, y):
   return x / y
def kali(x, y):
   return x * y
def pangkat(x, y):
   return x ** y 
def sisabagi(x, y):
   return x % y
def hitung():
    print('\tSelamat Datang Didalam Operasi Aritmatika')
    print('\t=============================')
    print('\tProgram Perhitungan Menggunakan Kalkulator')
    print('\t===============================')
    print('\t1. Penjumlahan')
    print('\t2. Pengurangan')
    print('\t3. Pembagian')
    print('\t4. Perkalian')
    print('\t5. Perpangkatan')
    print('\t6. Modulus')
    print('\t7. Keluar (Error) Dari Program')
    print('\t===============================')
    print('\tSilahkan Pilih No 1-7')
    print('')
    
    pilih = input("Masukkan Pilihan Anda (1/2/3/4/5/6/7): ")
    # Meminta input dari user
    nilai1 = int(input("Masukkan bilangan pertama: "))
    nilai2 = int(input("Masukkan bilangan kedua: "))
    if pilih == '1':
       print(nilai1,"+",nilai2,"=", tambah(nilai1,nilai2))
       tanya()
    elif pilih == '2':
       print(nilai1,"-",nilai2,"=", kurang(nilai1,nilai2))
       tanya()
    elif pilih == '3':
       print(nilai1,"/",nilai2,"=", bagi(nilai1,nilai2))
       tanya()
    elif pilih == '4':
       print(nilai1,"*",nilai2,"=", kali(nilai1,nilai2))
       tanya()
    elif pilih == '5':
       print(nilai1,"**",nilai2,"=", pangkat(nilai1,nilai2))  
       tanya()
    elif pilih == '6':
       print(nilai1,"%",nilai2,"=", sisabagi(nilai1,nilai2))
       tanya()
    else:
       print("Input salah !!")
       
def tanya():
    tanya = input('\n\tKembali ke menu (y/t)?')
    if tanya == 'y':
        hitung()
    elif tanya == 't':
        exit
    else:
        print('\n\tsalah input.........!!!')

hitung()

#salaminformatika"-"
#ahzidur"v"
#Hz^Grapichs">"