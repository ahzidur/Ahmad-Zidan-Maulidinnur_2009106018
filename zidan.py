import os

biodata = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def awal():
    clear_screen()
    print('Sebelum menggunakan Aplikasi, silakan isi data dibawah ini:')
    nama = str(input('Masukkan Nama Lengkap Anda: '))
    biodata.insert(0,nama)
    nim = str(input('Masukkan NIM Anda: '))
    biodata.insert(1,nim)
    prodi = str(input('Masukkan Program Studi Anda: '))
    biodata.insert(2,prodi)
    kelas = str(input('Masukkan Kelas Anda: '))
    biodata.insert(0,kelas)
    clear_screen()
    print('\t=============================')
    print('\tBiodata')
    print('\t=============================')
    print('Nama Lengkap: %s' % (biodata[0]))
    print('NIM: %s' % (biodata[1]))
    print('Prodi: %s' % (biodata[2]))
    print('Kelas: %s' % (biodata[3]))
    tanya()

def hitung():
    clear_screen()
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
    print('\t7. Keluar Dari Program')
    print('\t===============================')
    print('\tSilahkan Pilih No 1-7')
    print('')
    
    pilih = str(input("Masukkan Pilihan Anda (1/2/3/4/5/6/7): "))
    print('\t=============================')
    print('\tPilih Jenis Bilangan')
    print('\t===============================')
    print('\t1. Bilangan Bulat')
    print('\t2. Bilangan Desimal')
    pilih2 = str(input('Masukkan Pilihan Anda (1/2): '))
    # Meminta input dari user
    if pilih2 == '1':
        nilai1 = int(input('Masukkan bilangan pertama: '))
        nilai2 = int(input('Masukkan bilangan kedua: '))
    elif pilih2 == '2':
        nilai1 = float(input('Masukkan bilangan pertama: '))
        nilai2 = float(input('Masukkan bilangan kedua: '))
    else:
        print('Pilihan tidak tersedia')
        tanya()

    if pilih == '1':
        print(nilai1,"+",nilai2,'=', tambah(nilai1,nilai2))
        tanya()
    elif pilih == '2':
        print(nilai1,"-",nilai2,'=', kurang(nilai1,nilai2))
        tanya()
    elif pilih == '3':
        print(nilai1,"/",nilai2,'=', bagi(nilai1,nilai2))
        tanya()
    elif pilih == '4':
        print(nilai1,"*",nilai2,'=', kali(nilai1,nilai2))
        tanya()
    elif pilih == '5':
        print(nilai1,"**",nilai2,'=', pangkat(nilai1,nilai2))  
        tanya()
    elif pilih == '6':
        print(nilai1,"%",nilai2,'=', sisabagi(nilai1,nilai2))
        tanya()
    elif pilih == '7':
        print('Terima kasih telah menggunakan Aplikasi Kalkulator Sederhana')
        exit
    else:
        print('Input salah !!')
        tanya()

def tanya():
    kembali = str(input('\n\tKembali ke menu (y/t)? '))
    if kembali == 'y':
        hitung()
    elif kembali == 't':
        print('Terima kasih telah menggunakan Aplikasi Kalkulator Sederhana')
        exit
    else:
        print('\n\tsalah input.........!!!')
        tanya()

awal()

#salaminformatika"-"
#ahzidur"v"
#Hz^Grapichs">"