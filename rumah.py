from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga, luas_tanah):
        super().__init__("Rumah", jml_penghuni, jml_kamar, harga)
        self.nama_pemilik = nama_pemilik
        # tambahan atribut
        self.luas_tanah = luas_tanah 

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_detail(self):
        return "Pemilik: {}\nJumlah Penghuni: {}\nJumlah Kamar: {}\nHarga: ${}".format(
            self.get_nama_pemilik(), self.get_jml_penghuni(), self.get_jml_kamar(), self.get_harga())

    def get_luas_tanah(self):
        return self.luas_tanah

    def get_gambar(self):
        return "https://th.bing.com/th/id/R.7e82aef7d0cc2f754488e287f687aace?rik=gPuFfy13PscHjw&riu=http%3a%2f%2finteriorvogue.com%2fwp-content%2fuploads%2f2016%2f05%2fFabulous-Contemporary-Homes.jpg&ehk=6ix3Uw1mJZJuOpcarN523FzTguwrUI4QofNtLlPyX90%3d&risl=&pid=ImgRaw&r=0"
