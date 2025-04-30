print("Kalkulator sederhana")
angka_1 = int(input("Masukkan angka pertama : "))
angka_2 = int(input("Masukkan angka kedua : "))
hasil = ()
print("Operasi apa yang ingin anda gunakan?",
      "\n1. Penjumlahan",
      "\n2. Pengurangan",
      "\n3. Perkalian",
      "\n4. Pembagian")
operasi = int(input("Operasi yang anda pilih (angkanya saja) :"))

def penjumlahan():
    hasil = angka_1 + angka_2
    return hasil

def pengurangan():
    hasil = angka_1 - angka_2
    return hasil

def perkalian():
    hasil = angka_1 * angka_2
    return hasil

def pembagian():
    hasil = angka_1 / angka_2
    return hasil

if operasi == 1:
    print(penjumlahan())
elif operasi == 2:
    print(pengurangan())
elif operasi == 3:
    print(perkalian())
elif operasi == 4:
    print(pembagian())

