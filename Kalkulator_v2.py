print("Kalkulator sederhana")
print("Operasi yang dapat dipilih :",
      "\n1. Penjumlahan (+)",
      "\n2. Pengurangan (-)",
      "\n3. Perkalian (*)",
      "\n4. Pembagian (/)")

data_angka = []

def ambil_angka():
    while True:
        try:
            jumlah_angka = int(input("Jumlah angka yang ingin anda hitung (minimal 2): "))
            if jumlah_angka < 2:
                print("Minimal harus 2 angka!")
                continue
                
            for i in range(jumlah_angka):
                angka = float(input(f"Angka {i+1} : "))
                data_angka.append(angka)
            return jumlah_angka
        except ValueError:
            print("Error, Harap masukan angka yang valid!")
            data_angka.clear()

def ambil_operasi(jumlah_operasi):
    data_operasi = []
    for i in range(jumlah_operasi):
        while True:
            try:
                op = int(input(f"Operasi {i+1} (1-4): "))
                if 1 <= op <= 4:
                    data_operasi.append(op)
                    break
                else:
                    print("Harap masukkan angka 1-4 saja!")
            except ValueError:
                print("Harap masukkan angka yang valid!")
    return data_operasi

def hitung(angka, operasi):
    hasil = angka[0]
    for i in range(len(operasi)):
        if operasi[i] == 1:
            hasil += angka[i+1]
        elif operasi[i] == 2:
            hasil -= angka[i+1]
        elif operasi[i] == 3:
            hasil *= angka[i+1]
        elif operasi[i] == 4:
            if angka[i+1] == 0:
                print("Error: Pembagian dengan nol!")
                return None
            hasil /= angka[i+1]
    return hasil

# Program utama
jumlah_angka = ambil_angka()
jumlah_operasi = jumlah_angka - 1
operasi = ambil_operasi(jumlah_operasi)

print("\nAngka-angka yang dimasukkan:", data_angka)
print("Operasi yang dipilih:", operasi)

hasil = hitung(data_angka, operasi)
if hasil is not None:
    print("Hasil perhitungan:", hasil)
