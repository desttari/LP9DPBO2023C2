# library import
from tkinter import *
from PIL import Image, ImageTk
import urllib.request
import io
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos

# buat object data
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, 150000000, "Emerald"))
hunians.append(Rumah("Sekar MK", 5, 2, 250000000, 400))
hunians.append(Indekos("Bp. Romi", "Cahya", 1000000, 60))
hunians.append(Rumah("Satria", 1, 4, 300000000, 650))

# title panel
root = Tk()
root.title("Praktikum DPBO Python")

# halaman daftar residen
def show_data_page():
    # Hapus semua widget di root
    for widget in root.winfo_children():
        widget.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos":
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

# halaman detail tiap data
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    try:
        # download image from URL
        url = hunians[index].get_gambar()
        response = urllib.request.urlopen(url)
        image_data = response.read()

        # create image object from data
        image = Image.open(io.BytesIO(image_data))

        # resize image
        image = image.resize((500, 300))

        # create photoimage object from image
        photo = ImageTk.PhotoImage(image)

        # create label and display image
        label = Label(d_frame, image=photo)
        label.image = photo
        label.pack()

    except Exception as e:
        # Jika terjadi kesalahan saat mengakses gambar, tampilkan pesan kesalahan
        error_label = Label(d_frame, text="Error: " + str(e))
        error_label.pack()

    # gather and print datas
    jenis = Label(d_frame, text="Jenis: " + hunians[index].get_jenis())
    jenis.pack()

    if hunians[index].get_jenis() == "Indekos":
        penghuni = Label(d_frame, text="Penghuni: " + hunians[index].get_nama_penghuni())
        penghuni.pack()
    else:
        pemilik = Label(d_frame, text="Pemilik: " + hunians[index].get_nama_pemilik())
        pemilik.pack()

    jml_penghuni = Label(d_frame, text="Jumlah Penghuni: " + str(hunians[index].get_jml_penghuni()))
    jml_penghuni.pack()

    jml_kamar = Label(d_frame, text="Jumlah Kamar: " + str(hunians[index].get_jml_kamar()))
    jml_kamar.pack()

    if hunians[index].get_jenis() == "Apartemen":
        harga = Label(d_frame, text="Harga: Rp. " + str(hunians[index].get_harga()))
        harga.pack()
        dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen())
        dokumen.pack()
        nama_bangunan = Label(d_frame, text="Nama Bangunan: " + hunians[index].get_nama_bangunan())
        nama_bangunan.pack()
    elif hunians[index].get_jenis() == "Rumah":
        harga = Label(d_frame, text="Harga: Rp. " + str(hunians[index].get_harga()))
        harga.pack()
        dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen())
        dokumen.pack()
        luas_tanah = Label(d_frame, text="Luas Tanah: " + str(hunians[index].get_luas_tanah()) + " m²")
        luas_tanah.pack()
    
    elif hunians[index].get_jenis() == "Indekos":
        harga = Label(d_frame, text="Harga: Rp. " + str(hunians[index].get_harga()))
        harga.pack()
        luas_kamar = Label(d_frame, text="Luas Kamar: " + str(hunians[index].get_luas_kamar()) + " m²")
        luas_kamar.pack()

# landing page
def show_landing_page():
    # Hapus semua widget di root
    for widget in root.winfo_children():
        widget.destroy()

    frame = LabelFrame(root, text="Home", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    # download image from URL
    url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/030932d3-8fd0-44d9-b238-639b2d366e55/d3g51r9-8905ea1e-fa89-48dd-bf6b-b4145b9260a7.png/v1/fill/w_500,h_526,q_80,strp/random_logo_concept_by_naraosga_d3g51r9-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTI2IiwicGF0aCI6IlwvZlwvMDMwOTMyZDMtOGZkMC00NGQ5LWIyMzgtNjM5YjJkMzY2ZTU1XC9kM2c1MXI5LTg5MDVlYTFlLWZhODktNDhkZC1iZjZiLWI0MTQ1YjkyNjBhNy5wbmciLCJ3aWR0aCI6Ijw9NTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.UsGuSz_Xc1mneAEfPoZJBNEWCz8CIvJu_FTYp8jKd34"
    image_data = urllib.request.urlopen(url).read()

    # create image object from data
    image = Image.open(io.BytesIO(image_data))

    # resize image
    image = image.resize((300, 300))

    # create photoimage object from image
    photo = ImageTk.PhotoImage(image)

    # create label and display image
    label = Label(frame, image=photo)
    label.image = photo
    label.pack()

    b_start = Button(frame, text="Start", command=show_data_page)
    b_start.pack()

    b_exit = Button(frame, text="Exit", command=root.quit)
    b_exit.pack()

show_landing_page()
root.mainloop()
