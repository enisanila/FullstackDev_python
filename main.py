from kalkulator import Kalkulator

def utama():
    kalkulator = Kalkulator()

    print("Program Kalkulator")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print("Hasil:", kalkulator.tambah(angka1, angka2))
    elif pilihan == '2':
        print("Hasil:", kalkulator.kurang(angka1, angka2))
    elif pilihan == '3':
        print("Hasil:", kalkulator.kali(angka1, angka2))
    elif pilihan == '4':
        print("Hasil:", kalkulator.bagi(angka1, angka2))
    else:
        print("Input tidak valid")

if __name__ == "__main__":
    utama()
