from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga, nama_bangunan):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, harga)
        self.nama_pemilik = nama_pemilik
        # tambahan atribut
        self.nama_bangunan = nama_bangunan

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nHarga : $" + str(self.harga) + "\n"

    def get_nama_bangunan(self):
        return self.nama_bangunan
    
    def get_gambar(self):
        return "https://mir-s3-cdn-cf.behance.net/project_modules/1400/3e4e6f53705025.593e872712cd9.jpg"
