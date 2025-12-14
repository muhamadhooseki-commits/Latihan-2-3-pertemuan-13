 Program Python: Kalkulator Aman dan Validasi Daftar Nilai

 📁 Struktur Program

 1. Kalkulator Aman (`kalkulator_aman()`)
Program kalkulator yang menangani berbagai jenis error:

 Langkah-langkah Implementasi:

Langkah 1: Persiapan Input
```python
while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        break
    except ValueError:
        print("Error: Input harus berupa angka! Silakan coba lagi.")
```
- Menggunakan loop `while True` untuk memastikan input valid
- `try-except` menangani `ValueError` jika input bukan angka
- Program terus meminta input hingga mendapatkan angka valid

Langkah 2: Penanganan Operator
```python
try:
    if operator == '+':
        hasil = angka1 + angka2
    # ... operator lainnya
    else:
        raise Exception(f"Error: Operator '{operator}' tidak valid!")
```
- Menggunakan `raise Exception` untuk operator tidak valid
- Menangani empat operator dasar: `+`, `-`, `*`, `/`

Langkah 3: Penanganan Pembagian dengan Nol
```python
elif operator == '/':
    if angka2 == 0:
        raise ZeroDivisionError("Error: Pembagian dengan nol tidak diperbolehkan!")
```
- Pengecekan eksplisit untuk pembagian dengan nol
- Menggunakan `raise` untuk membangkitkan error khusus

 Flowchart Kalkulator:
```
Start
  ↓
Input Angka 1 → Error? → Tampilkan Pesan
  ↓ (Valid)
Input Angka 2 → Error? → Tampilkan Pesan
  ↓ (Valid)
Input Operator
  ↓
Cek Operator Valid?
  ↓ (Tidak) → Raise Exception
  ↓ (Ya)
Cek Pembagian Nol?
  ↓ (Ya) → Raise ZeroDivisionError
  ↓ (Tidak)
Hitung Hasil
  ↓
Tampilkan Hasil
  ↓
End
```

 2. Validasi Daftar Nilai (`validasi_daftar_nilai()`)
Program yang menghitung rata-rata dari list berisi data campuran:

 Langkah-langkah Implementasi:

Langkah 1: Persiapan Data
```python
nilai = [80, 90, 'A', 70, 100, 'B']
```
- List berisi campuran integer dan string
- Representasi data nyata yang mungkin tidak bersih

Langkah 2: Iterasi dengan Penanganan Error
```python
for data in nilai:
    try:
        nilai_float = float(data)
        total_nilai += nilai_float
        jumlah_valid += 1
    except (ValueError, TypeError):
        data_tidak_valid.append(data)
        continue
```
- Loop melalui setiap elemen list
- `try-except` di dalam loop mencegah program berhenti saat error
- `continue` melanjutkan ke iterasi berikutnya setelah menangani error

Langkah 3: Perhitungan dan Output
```python
if jumlah_valid > 0:
    rata_rata = total_nilai / jumlah_valid
```
- Menghitung rata-rata hanya dari data valid
- Menampilkan statistik lengkap

Flowchart Validasi Nilai:
```
Start
  ↓
Inisialisasi: total=0, count=0
  ↓
Loop: setiap data dalam list
  ↓
Try: konversi ke float
  ↓ (Error) → Catat data invalid → Continue
  ↓ (Sukses)
Tambahkan ke total
Counter +1
  ↓
Selesai loop?
  ↓ (Ya)
Hitung rata-rata
  ↓
Tampilkan hasil
  ↓
End
```

 
**Topik:** Exception Handling, Input Validation, Data Processing
