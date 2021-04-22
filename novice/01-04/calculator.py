from math import pi

print("Calculator")
print('\n1.Luas; 2.Kuadrat')
choice = input('\nPilih 1 / 2:')
if choice == '1':
    print('\na. Lingkaran \nb. Persegi \nc. Persegi Panjang \nd. Jajar Genjang \ne. Segitiga')
    choice2 = input('\nPilih: a / b / c / d: ')
    if choice2 == 'a':
        r = int(input('Radius: '))
        print('Luas Lingkaran = ', pi * r **2)
    elif choice2 == 'b':
        sisi = int(input('Sisi: '))
        print('Luas Persegi Panjang = ', sisi * sisi)
    elif choice2 == 'c':
        panjang = int(input('Panjang: '))
        lebar = int(input('Lebar: '))
        print('Luas Persegi Panjang = ', panjang * lebar)
    elif choice2 == 'd':
        alas = int(input('Alas: '))
        tinggi = int(input('Tinggi: '))
        print('Luas Persegi Panjang = ', alas * tinggi)
    elif choice2 == 'd':
        alas = int(input('Alas: '))
        tinggi = int(input('Tinggi: '))
        print('Luas Segitiga = ', 0.5 * alas * tinggi)
    else:
        print("\nPilih yang benar !!!")
elif choice == '2':
    number = int(input('Angka: '))
    print(f'Kuadrat dari {number} adalah: ', number ** 2)
else:
    print('\nPilihan tidak ada')    
