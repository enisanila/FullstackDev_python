class Kalkulator:
    def tambah(self, x, y):
        return x + y

    def kurang(self, x, y):
        return x - y

    def kali(self, x, y):
        return x * y

    def bagi(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Pembagian oleh nol"
