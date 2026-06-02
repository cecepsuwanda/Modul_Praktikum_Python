# Program sederhana untuk menyimpan dan menampilkan data nama serta umur
# Program menggunakan file teks untuk menyimpan data secara permanen

def tulis_file():
    """
    Fungsi untuk menginput data nama dan umur dari pengguna,
    kemudian menyimpannya ke dalam file teks 'data.txt'.
    Setiap data disimpan dalam format: nama,umur (dipisahkan koma)
    """
    # Input data dari pengguna
    nama = input("Nama : ")
    umur = input("Umur : ")

    # Menyimpan data ke file dalam mode append (menambahkan di akhir file)
    # Jika file belum ada, maka file akan dibuat secara otomatis
    with open("data.txt", "a") as file:
        file.write(f"{nama},{umur}\n")

    # Konfirmasi bahwa data telah berhasil disimpan
    print("Data berhasil disimpan")


def baca_file():
    """
    Fungsi untuk membaca dan menampilkan data yang telah disimpan di file 'data.txt'.
    Data ditampilkan dalam format yang mudah dibaca: Nama: [nama] | Umur: [umur]
    """
    print("\n=== DATA TERSIMPAN ===")

    try:
        # Membuka file dalam mode read (baca)
        with open("data.txt", "r") as file:
            # Membaca setiap baris dalam file
            for baris in file:
                # Memisahkan data berdasarkan koma dan menghilangkan karakter newline
                data = baris.strip().split(",")
                # Menampilkan data dalam format yang rapi
                print(f"Nama: {data[0]} | Umur: {data[1]}")
    except FileNotFoundError:
        # Menangani kasus ketika file belum ada (belum pernah menyimpan data)
        print("File belum tersedia")


def main():
    """
    Fungsi utama program yang menyediakan menu interaktif untuk pengguna.
    Pengguna dapat memilih untuk menyimpan data, menampilkan data, atau keluar dari program.
    """
    while True:
        # Menampilkan menu pilihan kepada pengguna
        print("\n=== MENU ===")
        print("1. Simpan Data")
        print("2. Tampilkan Data")
        print("3. Keluar")

        # Input pilihan menu dari pengguna
        pilihan = input("Pilih menu: ")

        # Memproses pilihan pengguna
        if pilihan == "1":
            # Memanggil fungsi tulis_file untuk menyimpan data
            tulis_file()
        elif pilihan == "2":
            # Memanggil fungsi baca_file untuk menampilkan data
            baca_file()
        elif pilihan == "3":
            # Keluar dari loop (menghentikan program)
            break
        else:
            # Menangani input yang tidak valid
            print("Pilihan tidak valid")


# Menjalankan fungsi main() jika file ini dijalankan secara langsung
# (bukan di-import dari file lain)
if __name__ == "__main__":
    main()