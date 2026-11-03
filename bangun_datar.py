class BangunDatar:
    def __init__(self, nama):
        self.nama = nama

    def luas_persegi(self, sisi):
        return sisi * sisi

    def luas_persegi_panjang(self, panjang, lebar):
        return panjang * lebar

    def luas_lingkaran(self, r):
        return 3.14 * r * r

# Membuat objek dari class BangunDatar
hitung = BangunDatar("Kalkulator Bangun Datar")
print(f"--- Selamat Datang di {hitung.nama} ---")

# Menggunakan semua method yang ada di dalam class
hasil_persegi = hitung.luas_persegi(5)
print(f"Luas Persegi (sisi 5): {hasil_persegi}")

hasil_pp = hitung.luas_persegi_panjang(10, 4)
print(f"Luas Persegi Panjang (panjang 10, lebar 4): {hasil_pp}")

hasil_lingkaran = hitung.luas_lingkaran(7)
print(f"Luas Lingkaran (jari-jari 7): {hasil_lingkaran}")