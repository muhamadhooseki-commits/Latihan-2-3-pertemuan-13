def kalkulator_aman():
    """
    Program kalkulator sederhana dengan penanganan error:
    1. Menangani input non-angka dengan ValueError
    2. Menangani pembagian dengan nol dengan ZeroDivisionError
    3. Menangani operator tidak valid dengan raise Exception
    """
    print("=" * 50)
    print("KALKULATOR AMAN")
    print("=" * 50)
    
    # Input angka pertama dengan penanganan error
    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            break
        except ValueError:
            print("Error: Input harus berupa angka! Silakan coba lagi.")
    
    # Input angka kedua dengan penanganan error
    while True:
        try:
            angka2 = float(input("Masukkan angka kedua: "))
            break
        except ValueError:
            print("Error: Input harus berupa angka! Silakan coba lagi.")
    
    # Input operator
    operator = input("Masukkan operator (+, -, *, /): ")
    
    # Proses perhitungan dengan penanganan error
    try:
        if operator == '+':
            hasil = angka1 + angka2
            print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
        
        elif operator == '-':
            hasil = angka1 - angka2
            print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
        
        elif operator == '*':
            hasil = angka1 * angka2
            print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
        
        elif operator == '/':
            # Cek pembagian dengan nol
            if angka2 == 0:
                raise ZeroDivisionError("Error: Pembagian dengan nol tidak diperbolehkan!")
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")
        
        else:
            # Operator tidak valid
            raise Exception(f"Error: Operator '{operator}' tidak valid! Gunakan +, -, *, atau /.")
    
    except ZeroDivisionError as e:
        print(e)
    
    except Exception as e:
        print(e)


# Program 2: Validasi Daftar Nilai
def validasi_daftar_nilai():
    """
    Program untuk menghitung rata-rata nilai dari list yang berisi
    campuran angka dan string dengan penanganan error
    """
    print("\n" + "=" * 50)
    print("VALIDASI DAFTAR NILAI")
    print("=" * 50)
    
    # Daftar nilai dengan data campuran
    nilai = [80, 90, 'A', 70, 100, 'B']
    
    print(f"Daftar nilai: {nilai}")
    
    # Inisialisasi variabel
    jumlah_valid = 0
    total_nilai = 0
    data_tidak_valid = []
    
    # Iterasi melalui setiap elemen dalam list
    for data in nilai:
        try:
            # Coba konversi ke float
            nilai_float = float(data)
            total_nilai += nilai_float
            jumlah_valid += 1
            print(f"Data valid: {data} -> ditambahkan ke perhitungan")
        
        except (ValueError, TypeError) as e:
            # Tangkap error jika data bukan angka
            data_tidak_valid.append(data)
            print(f"Data tidak valid: {data} (dilewati)")
            continue  # Lanjut ke iterasi berikutnya
    
    # Hitung rata-rata jika ada data valid
    if jumlah_valid > 0:
        rata_rata = total_nilai / jumlah_valid
        print(f"\nHasil Perhitungan:")
        print(f"Jumlah data valid: {jumlah_valid}")
        print(f"Total nilai: {total_nilai}")
        print(f"Data tidak valid yang dilewati: {data_tidak_valid}")
        print(f"Rata-rata nilai: {rata_rata:.2f}")
    else:
        print("Tidak ada data valid untuk dihitung rata-ratanya.")


# Menu utama untuk memilih program yang akan dijalankan
def main():
    print("PROGRAM LATIHAN PYTHON")
    print("=" * 50)
    
    while True:
        print("\nPilih program yang ingin dijalankan:")
        print("1. Kalkulator Aman")
        print("2. Validasi Daftar Nilai")
        print("3. Keluar")
        
        pilihan = input("Masukkan pilihan (1-3): ")
        
        if pilihan == '1':
            kalkulator_aman()
        elif pilihan == '2':
            validasi_daftar_nilai()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")


# Menjalankan program utama
if __name__ == "__main__":
    main()