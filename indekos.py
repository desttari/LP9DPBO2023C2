from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga, luas_kamar):
        super().__init__("Indekos", 1, 1, harga)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        # tambahan atribut
        self.luas_kamar = luas_kamar

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos."

    def get_detail(self):
        return "Pemilik: {}\nPenghuni: {}\nHarga: ${}".format(self.nama_pemilik, self.nama_penghuni, self.harga)

    def get_luas_kamar(self):
        return self.luas_kamar
    
    def get_gambar(self):
        return "https://cdn.wallpapersafari.com/45/46/08WwjX.jpg"
