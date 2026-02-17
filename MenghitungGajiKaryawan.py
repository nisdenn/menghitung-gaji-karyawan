print("=" * 45)
print("   PROGRAM PERHITUNGAN GAJI KARYAWAN")
print("=" * 45)

HARI_KERJA = 30
JAM_NORMAL = 8
PAJAK = 0.05

while True:
    print("\n--- Input Data Karyawan ---")
    nama = input("Nama Karyawan           : ")
    jam_kerja = int(input("Jam Kerja per Hari      : "))
    tarif_per_jam = int(input("Tarif per Jam (Rp)      : "))

    if jam_kerja < 0 or tarif_per_jam < 0:
        print("Input tidak valid! Nilai tidak boleh negatif.")
        continue

    # Hitung gaji harian
    if jam_kerja > JAM_NORMAL:
        jam_lembur = jam_kerja - JAM_NORMAL
        gaji_harian = (JAM_NORMAL * tarif_per_jam) + \
                      (jam_lembur * tarif_per_jam * 1.5)
    else:
        jam_lembur = 0
        gaji_harian = jam_kerja * tarif_per_jam

    gaji_bulanan = gaji_harian * HARI_KERJA
    pajak = gaji_bulanan * PAJAK
    gaji_bersih = gaji_bulanan - pajak

    print("\n--- Rincian Gaji ---")
    print(f"Nama Karyawan    : {nama}")
    print(f"Jam Kerja/Hari   : {jam_kerja} jam")
    print(f"Jam Lembur       : {jam_lembur} jam")
    print(f"Gaji per Bulan   : Rp {gaji_bulanan:,.0f}")
    print(f"Pajak (5%)       : Rp {pajak:,.0f}")
    print(f"Gaji Bersih      : Rp {gaji_bersih:,.0f}")
    print("-" * 45)

    ulang = input("Hitung gaji karyawan lain? (y/n): ")
    if ulang.lower() != "y":
        print("\nProgram selesai. Terima kasih")
        break