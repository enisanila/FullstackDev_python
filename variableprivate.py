class Mobil:
    def __init__(self, merk, warna, tahun):
        self.__merk = merk  # Variabel merk menjadi pribadi
        self.warna = warna
        self.tahun = tahun

    def get_merk(self):
        return self.__merk

    def set_merk(self, merk_baru):
        self.__merk = merk_baru

mobil1 = Mobil("Toyota", "Hitam", 2020)

# Mengakses atribut yang tidak pribadi
print("Warna mobil:", mobil1.warna)
print("Tahun mobil:", mobil1.tahun)

# Mengakses atribut yang pribadi melalui metode kelas
print("Merk mobil:", mobil1.get_merk())

# Mengubah atribut yang pribadi melalui metode kelas
mobil1.set_merk("Honda")

# Melihat perubahan merk
print("Merk mobil setelah diubah:", mobil1.get_merk())
