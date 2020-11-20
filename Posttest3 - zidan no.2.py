import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        #NIM: 2009106018 + 10 = 28
        angka = int(input("Masukkan angka: "))
        y = 1
        x = 1
        while y <= angka:
            print (x)
            x += 1
            if x == 10:
                x -= 9
            y += 1
        break
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Silahkan coba lagi...")
        time.sleep(1.5)

        
        #salaminformatika"-"
        #ahzidur"v"
        #Hz^Grapichs">"
