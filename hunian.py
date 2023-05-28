class Hunian():
    def __init__(self, jenis, jml_penghuni=1, jml_kamar=1, harga=0):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        # tambahan atribut
        self.harga = harga

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_harga(self):
        return self.harga

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian " + self.jenis + ", ditempati oleh " + str(self.jml_penghuni) + " orang. Harga: $" + str(self.harga)

    def get_gambar(self):
        return "hunian.png"
