
import math
16
print(
    
    "CALCULATOR")

while True:
    print("\nPilih Operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (x^y)")
    print("6. Akar Kuadrat (sqrt)")
    print("7. Modulus (%)")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("11. Asin")
    print("12. Acos")
    print("13. Atan")
    print("14. Log (Basis 10)")
    print("15. Ln (Log Natural)")
    print("16. Faktorial (!)")
    print("17. Pi")
    print("18. e")
    print("19. Keluar")

    pilihan = input("Masukkan pilihan (1-19): ")

    if pilihan == "1":
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))
        hasil = bil1 + bil2
        print("Hasil =", hasil)

    elif pilihan == "2":
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))
        hasil = bil1 - bil2
        print("Hasil =", hasil)

    elif pilihan == "3":
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))
        hasil = bil1 * bil2
        print("Hasil =", hasil)

    elif pilihan == "4":
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))
        if bil2 != 0:
            hasil = bil1 / bil2
            print("Hasil =", hasil)
        else:
            print("Error: Tidak bisa dibagi nol!")

    elif pilihan == "5":
        bil1 = float(input("Masukkan bilangan: "))
        bil2 = float(input("Masukkan pangkat: "))
        hasil = bil1 ** bil2
        print("Hasil =", hasil)

    elif pilihan == "6":
        bil1 = float(input("Masukkan bilangan: "))
        if bil1 >= 0:
            hasil = math.sqrt(bil1)
            print("Hasil =", hasil)
        else:
            print("Error: Bilangan tidak boleh negatif!")

    elif pilihan == "7":
        bil1 = float(input("Masukkan bilangan pertama: "))
        bil2 = float(input("Masukkan bilangan kedua: "))
        hasil = bil1 % bil2
        print("Hasil =", hasil)

    elif pilihan == "8":
        bil1 = float(input("Masukkan sudut (derajat): "))
        hasil = math.sin(math.radians(bil1))
        print("Hasil Sin =", hasil)

    elif pilihan == "9":
        bil1 = float(input("Masukkan sudut (derajat): "))
        hasil = math.cos(math.radians(bil1))
        print("Hasil Cos =", hasil)

    elif pilihan == "10":
        bil1 = float(input("Masukkan sudut (derajat): "))
        hasil = math.tan(math.radians(bil1))
        print("Hasil Tan =", hasil)

    elif pilihan == "11":
        bil1 = float(input("Masukkan nilai: "))
        hasil = math.degrees(math.asin(bil1))
        print("Hasil Asin =", hasil, "derajat")

    elif pilihan == "12":
        bil1 = float(input("Masukkan nilai: "))
        hasil = math.degrees(math.acos(bil1))
        print("Hasil Acos =", hasil, "derajat")

    elif pilihan == "13":
        bil1 = float(input("Masukkan nilai: "))
        hasil = math.degrees(math.atan(bil1))
        print("Hasil Atan =", hasil, "derajat")

    elif pilihan == "14":
        bil1 = float(input("Masukkan bilangan: "))
        hasil = math.log10(bil1)
        print("Hasil Log =", hasil)

    elif pilihan == "15":
        bil1 = float(input("Masukkan bilangan: "))
        hasil = math.log(bil1)
        print("Hasil Ln =", hasil)

    elif pilihan == "16":
        bil1 = int(input("Masukkan bilangan bulat: "))
        if bil1 >= 0:
            hasil = math.factorial(bil1)
            print("Hasil Faktorial =", hasil)
        else:
            print("Error: Faktorial tidak untuk bilangan negatif!")

    elif pilihan == "17":
        print("Nilai Pi =", math.pi)

    elif pilihan == "18":
        print("Nilai e =", math.e)

    elif pilihan == "19":
        print("Terima kasih telah menggunakan kalkulator!")
        break

    else:
        print("Pilihan tidak valid!")
