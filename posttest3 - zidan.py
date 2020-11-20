import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def awal():
    clear_screen()
    print('\tSelamat Datang Didalam Aplikasi Toko Kue Sule')
    print('\t=============================')
    print('\tProgram Perhitungan Menggunakan Kalkulator')
    print('\t===============================')
    print('\t1. Kue Keju')
    print('\t2. Kue Coklat')
    print('\t3. Keluar Dari Program')
    print('\t===============================')
    print('\tSilahkan Pilih No 1-3')
    print('')
    
    pilih = str(input("Masukkan Pilihan Anda (1/2/3): "))
    # Meminta input dari user
    if pilih == '1':
        kue_keju = 6000
        clear_screen()
        print('\t=============================')
        print('\tKue Keju')
        print('\t=============================')
        print('\tPromo:')
        print('\tDiskon 10% pembelian 4-15 kue keju')
        print('\tDiskon 15% pembelian 16-25 kue keju')
        jumlah = int(input('\tJumlah kue keju> '))
        if(jumlah >= 0 and jumlah < 4):
            harga = kue_keju*jumlah
            print('\tTotal: Rp.', harga)
        elif(jumlah > 5 and jumlah < 16):
            diskon = int((kue_keju*jumlah)*10/100)
            print('\tDiskon. Rp.', diskon)
            harga = int((kue_keju*jumlah)-diskon)
            print('\tTotal: Rp.', harga)
        elif(jumlah > 15 and jumlah < 26):
            diskon = int((kue_keju*jumlah)*15/100)
            print('\tDiskon. Rp.', diskon)
            harga = int((kue_keju*jumlah)-diskon)
            print('\tTotal: Rp.', harga)
        else:
            print('\tJumlah tidak tersedia')
            tanya()
        bayar = int(input('\tBayar> '))
        if(bayar >= harga):
            print('\tKembalian: Rp.', bayar-harga)
        else:
            print('\tUang tidak cukup')
            tanya()
        tanya()
    elif pilih == '2':
        kue_coklat = 3500
        clear_screen()
        print('\t=============================')
        print('\tKue Coklat')
        print('\t=============================')
        print('\tPromo:')
        print('\tDiskon 7% pembelian 5-20 kue coklat')
        print('\tDiskon 12% pembelian 21-35 kue coklat')
        jumlah = int(input('Jumlah kue coklat> '))
        if(jumlah >= 0 and jumlah < 5):
            harga = kue_coklat*jumlah
            print('\tTotal: Rp.', harga)
        elif(jumlah > 4 and jumlah < 21):
            diskon = int((kue_coklat*jumlah)*7/100)
            print('\tDiskon. Rp.', diskon)
            harga = int((kue_coklat*jumlah)-diskon)
            print('\tTotal: Rp.', harga)
        elif(jumlah > 20 and jumlah < 36):
            diskon = int((kue_coklat*jumlah)*12/100)
            print('\tDiskon. Rp.', diskon)
            harga = int((kue_coklat*jumlah)-diskon)
            print('\tTotal: Rp.', harga)
        else:
            print('\tJumlah tidak tersedia')
            tanya()
        bayar = int(input('\tBayar> '))
        if(bayar >= harga):
            print('\tKembalian: Rp.', bayar-harga)
        else:
            print('\tUang tidak cukup')
            tanya()
        tanya()
    elif pilih == '3':
        print('\tTerima kasih telah menggunakan Aplikasi Toko Kue Sule')
        exit
    else:
        print('\tInput salah !!')
        tanya()

def tanya():
    kembali = str(input('\n\tKembali ke menu (y/t)? '))
    if kembali == 'y':
        awal()
    elif kembali == 't':
        print('\tTerima kasih telah menggunakan Aplikasi Toko Kue Sule')
        exit
    else:
        print('\n\tsalah input.........!!!')
        tanya()

awal()

#salaminformatika"-"
#ahzidur"v"
#Hz^Grapichs">"