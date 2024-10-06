# Program untuk menghitung biaya kuliah mahasiswa
def hitung_potongan(semester, biaya_sks):
    if semester > 5:
        return biaya_sks * 0.15  # Potongan 15% jika semester > 5
    else:
        return biaya_sks * 0.10  # Potongan 10% jika semester <= 5

def hitung_total(biaya_sks):
    return biaya_sks  # Total adalah biaya SKS

# Data mahasiswa
mahasiswa = [
    {
        "nim": "ABC01",
        "nama": "Adrian",
        "jurusan": "Bhs. Inggris",
        "semester": 6,
        "biaya_sks": 25000
    },
    {
        "nim": "B0002",
        "nama": "Risma",
        "jurusan": "Pend. Olahraga",
        "semester": 4,
        "biaya_sks": 20000
    }
]

# Proses dan tampilkan hasil
print("Hasil Perhitungan Biaya Kuliah Tahun 2021")
print("-" * 80)
print("No  NIM    Nama    Jurusan         Semester  Biaya SKS  Total  Potongan")
print("-" * 80)

for idx, mhs in enumerate(mahasiswa, 1):
    total = hitung_total(mhs["biaya_sks"])
    potongan = hitung_potongan(mhs["semester"], mhs["biaya_sks"])
    
    print(f"{idx:<4}{mhs['nim']:<7}{mhs['nama']:<8}{mhs['jurusan']:<15}{mhs['semester']:<10}{mhs['biaya_sks']:<11}{total:<8}{potongan:.0f}")

print("-" * 80)