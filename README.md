# LP9DPBO2023C2
LP9 2100506

## Janji
Saya Destira Lestari Saraswati dengan NIM 2100506 mengerjakan LP 9 Praktikum DPBO dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahan-Nya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Requirements Soal
Latihan Praktikum tidak menggunakan Database, tapi harus mengirim bukti screenshot menjalankan contoh kode yang dikirim.

Spesifikasi:
* Lengkapi fitur summary
* Buat landing Page (button yg ngarah ke halaman daftar residen)
* Tampilin gambar
* Tambahin 1 metode yang masih relevan untuk setiap kelas

Kalau mau bikin dari awal sendiri:
* Landing Page juga
* Minimal menggunakan 4 kelas
* Tampilin gambar
* Semua data kelas harus ditampilkan
* Buat diagram kelas di readme

## Program
### Deskripsi Program:
Program di atas merupakan aplikasi sederhana berbasis GUI (Graphical User Interface) yang digunakan untuk menampilkan data hunian seperti apartemen, rumah, dan indekos. Program ini memungkinkan pengguna untuk melihat daftar hunian yang tersedia dan melihat detail hunian tertentu, termasuk informasi seperti gambar, jenis hunian, nama pemilik/penghuni, jumlah penghuni, jumlah kamar, harga, serta informasi khusus terkait jenis hunian tertentu seperti luas tanah atau luas kamar.

### Alur Program:
1. Program dimulai dengan fungsi `show_landing_page()` yang menampilkan halaman beranda dengan gambar dan dua tombol, yaitu "Start" dan "Exit".
2. Jika pengguna menekan tombol "Start", fungsi `show_data_page()` akan dipanggil.
3. Fungsi `show_data_page()` akan menghapus semua widget di root, lalu membuat frame untuk menampilkan data seluruh hunian dan frame untuk tombol-tombol lainnya.
4. Daftar hunian disimpan dalam variabel `hunians`.
5. Untuk setiap hunian dalam daftar `hunians`, widget-label akan dibuat dan ditampilkan di dalam frame data dengan menggunakan perulangan.
6. Setiap label memiliki informasi seperti nomor index hunian, jenis hunian, nama pemilik/penghuni, dan tombol "Details" untuk melihat detail hunian tersebut.
7. Ketika tombol "Details" ditekan, fungsi `details(index)` akan dipanggil dengan indeks hunian sebagai argumen.
8. Fungsi `details(index)` akan membuat jendela baru (Toplevel) untuk menampilkan detail hunian terpilih.
9. Detail hunian seperti gambar, jenis hunian, nama pemilik/penghuni, jumlah penghuni, jumlah kamar, harga, dan informasi khusus terkait jenis hunian tertentu akan ditampilkan di dalam frame data.
10. Jika hunian adalah Apartemen, informasi tambahan seperti gambar, harga dan nama bangunan juga ditampilkan.
11. Jika hunian adalah Rumah, informasi tambahan seperti gambar, harga dan luas tanah ditampilkan.
12. Jika hunian adalah Indekos, informasi tambahan seperti gambar, harga dan luas kamar ditampilkan.
13. Pengguna dapat menutup jendela detail hunian dengan menekan tombol `Exit` pada jendela tersebut.
14. Pengguna juga dapat menutup program dengan menekan tombol `Exit` pada halaman beranda.

### Batasan Program:
1. Program hanya menampilkan data hunian yang telah didefinisikan secara statis dalam kode program. Data tersebut tidak dapat diubah atau ditambahkan oleh pengguna.
2. Gambar apartemen, iindekos dan rumah diambil dari URL yang telah ditentukan dalam kode program. Jika gambar tidak tersedia atau terjadi kesalahan dalam mengakses gambar, pesan kesalahan akan ditampilkan.
3. Program ini tidak memiliki fitur untuk mengedit atau menghapus data hunian.
4. Program hanya menampilkan informasi dasar tentang hunian seperti jenis, nama pemilik/penghuni, jumlah penghuni, jumlah kamar, harga, serta informasi khusus terkait jenis hunian tertentu seperti luas tanah atau luas kamar. Fitur-fitur lain seperti pencarian atau pengurutan data tidak tersedia dalam program ini.
5. Program ini bersifat sederhana dan hanya digunakan sebagai contoh latihan implementasi GUI dasar menggunakan Python.
6. Karena menggunakan URL luar untuk gambar, harus menginstal `PIL (Python Imaging Library)` dan `urllib libraries`.

### Preview Program


https://github.com/desttari/LP9DPBO2023C2/assets/100773981/8fa832ec-3718-4191-b276-fcf1922a0de2





### Screenshot Bukti Program DB
![Screenshotlp9](https://github.com/desttari/LP9DPBO2023C2/assets/100773981/0a2835d2-de4b-4e90-9ae6-07f85af13a30)

