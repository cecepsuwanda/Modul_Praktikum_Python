# Program untuk mengelola data nilai mahasiswa
# Program ini dapat menghitung nilai akhir, huruf mutu,
# menyimpan data ke file CSV, dan membaca data dari file CSV

def hitung_nilai_akhir(tugas, quiz, uts, uas):
    """
    Fungsi untuk menghitung nilai akhir berdasarkan bobot:
    - Tugas: 20%
    - Quiz: 20%
    - UTS: 30%
    - UAS: 30%
    """
    return (0.2 * tugas) + (0.2 * quiz) + (0.3 * uts) + (0.3 * uas)

def hitung_huruf_mutu(nilai):
    """
    Fungsi untuk mengkonversi nilai angka ke huruf mutu
    berdasarkan standar nilai:
    - A: >= 80
    - B: >= 70
    - C: >= 60
    - D: >= 50
    - E: < 50
    """
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

def tulis_file():
    """
    Fungsi untuk menginput data mahasiswa dan menyimpannya ke file CSV.
    Data yang disimpan meliputi:
    - Informasi mahasiswa (semester, NIM, kode MK, nama MK, SKS)
    - Nilai-nilai (tugas, quiz, UTS, UAS)
    - Nilai akhir dan huruf mutu yang dihitung
    """
    # Input data mahasiswa
    semester = input("Semester          : ")
    nim = input("NIM               : ")
    kode_mtk = input("Kode Mata Kuliah  : ")
    nm_mtk = input("Nama Mata Kuliah  : ")
    sks = int(input("SKS               : "))

    # Input nilai
    n_tugas = int(input("Nilai Tugas       : "))
    n_quiz = int(input("Nilai Quiz        : "))
    n_UTS = int(input("Nilai UTS         : "))
    n_UAS = int(input("Nilai UAS         : "))

    # Hitung nilai akhir dan huruf mutu
    n_akhir = hitung_nilai_akhir(
        n_tugas,
        n_quiz,
        n_UTS,
        n_UAS
    )

    hm = hitung_huruf_mutu(n_akhir)

    # Simpan data ke file CSV
    with open("data_nilai.csv", "a") as file:
        file.write(
            f"{semester},{nim},{kode_mtk},{nm_mtk},{sks},"
            f"{n_tugas},{n_quiz},{n_UTS},{n_UAS},"
            f"{n_akhir:.2f},{hm}\n"
        )

    # Tampilkan hasil
    print("\nData berhasil disimpan")
    print(f"Nilai Akhir : {n_akhir:.2f}")
    print(f"Huruf Mutu  : {hm}")

def baca_file():
    """
    Fungsi untuk membaca dan menampilkan data dari file CSV.
    Menampilkan informasi lengkap nilai mahasiswa termasuk
    nilai akhir dan huruf mutu.
    """
    print("\n=== DATA NILAI MAHASISWA ===")

    try:
        # Buka dan baca file CSV
        with open("data_nilai.csv", "r") as file:
            for baris in file:
                # Pisahkan data berdasarkan koma
                data = baris.strip().split(",")

                # Tampilkan data dengan format yang rapi
                print("-" * 60)
                print(f"Semester      : {data[0]}")
                print(f"NIM           : {data[1]}")
                print(f"Kode MK       : {data[2]}")
                print(f"Nama MK       : {data[3]}")
                print(f"SKS           : {data[4]}")
                print(f"Nilai Tugas   : {data[5]}")
                print(f"Nilai Quiz    : {data[6]}")
                print(f"Nilai UTS     : {data[7]}")
                print(f"Nilai UAS     : {data[8]}")
                print(f"Nilai Akhir   : {data[9]}")
                print(f"Huruf Mutu    : {data[10]}")
    except FileNotFoundError:
        # Tangani jika file belum ada
        print("File data_nilai.csv belum ada.")

def main():
    """
    Fungsi utama program yang menampilkan menu dan
    mengatur alur program berdasarkan pilihan pengguna.
    """
    while True:
        # Tampilkan menu
        print("\n=== MENU ===")
        print("1. Input Nilai")
        print("2. Tampilkan Nilai")
        print("3. Keluar")

        # Input pilihan pengguna
        pilihan = input("Pilih menu : ")

        # Proses berdasarkan pilihan
        if pilihan == "1":
            tulis_file()
        elif pilihan == "2":
            baca_file()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid")

# Jalankan program jika file dijalankan langsung
if __name__ == "__main__":
    main()