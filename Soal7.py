# Program untuk menghitung total penerimaan Jamsostek

def hitung_total(nik, jenis_jamsostek, wilayah, biaya_jamsostek):
    # Tentukan potongan berdasarkan wilayah dan jenis
    potongan = 0
    if wilayah == 1 and jenis_jamsostek == "11":
        potongan = 4000
    elif wilayah == 2 and jenis_jamsostek == "03":
        potongan = 6500
    
    # Hitung total yang diterima
    if wilayah == 1:
        total = biaya_jamsostek - 4000
    else:
        total = biaya_jamsostek - 6500
    
    return potongan, total

# Data peserta
peserta = [
    {
        "nik": "14440-11",
        "jenis_jamsostek": "11",
        "wilayah": 1,
        "biaya_jamsostek": 50000
    },
    {
        "nik": "18211-03",
        "jenis_jamsostek": "03",
        "wilayah": 2,
        "biaya_jamsostek": 65000
    }
]

# Tampilkan hasil
print("DAFTAR KODE PESERTA JAMSOSTEK BUMIPUTERA")
print("-" * 70)
print("NIK\t\tJenis\tWilayah\tBiaya\t\tPotongan\tTotal")
print("-" * 70)

for p in peserta:
    potongan, total = hitung_total(
        p["nik"],
        p["jenis_jamsostek"],
        p["wilayah"],
        p["biaya_jamsostek"]
    )
    
    print(f"{p['nik']}\t{p['jenis_jamsostek']}\t{p['wilayah']}\t{p['biaya_jamsostek']}\t\t{potongan}\t\t{total}")

print("-" * 70)