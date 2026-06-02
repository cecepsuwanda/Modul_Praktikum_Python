def hitung_nilai_akhir(tugas, quiz, uts, uas):
    return (0.2 * tugas) + (0.2 * quiz) + (0.3 * uts) + (0.3 * uas)

def hitung_huruf_mutu(nilai):
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
    semester = input("Semester          : ")
    nim = input("NIM               : ")
    kode_mtk = input("Kode Mata Kuliah  : ")
    nm_mtk = input("Nama Mata Kuliah  : ")
    sks = int(input("SKS               : "))

    n_tugas = int(input("Nilai Tugas       : "))
    n_quiz = int(input("Nilai Quiz        : "))
    n_UTS = int(input("Nilai UTS         : "))
    n_UAS = int(input("Nilai UAS         : "))

    n_akhir = hitung_nilai_akhir(
        n_tugas,
        n_quiz,
        n_UTS,
        n_UAS
    )

    hm = hitung_huruf_mutu(n_akhir)

    with open("data_nilai.csv", "a") as file:
        file.write(
            f"{semester},{nim},{kode_mtk},{nm_mtk},{sks},"
            f"{n_tugas},{n_quiz},{n_UTS},{n_UAS},"
            f"{n_akhir:.2f},{hm}\n"
        )

    print("\nData berhasil disimpan")
    print(f"Nilai Akhir : {n_akhir:.2f}")
    print(f"Huruf Mutu  : {hm}")


def baca_file():
    print("\n=== DATA NILAI MAHASISWA ===")

    try:
        with open("data_nilai.csv", "r") as file:
            for baris in file:
                data = baris.strip().split(",")

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
        print("File data_nilai.csv belum ada.")


def main():
    while True:
        print("\n=== MENU ===")
        print("1. Input Nilai")
        print("2. Tampilkan Nilai")
        print("3. Keluar")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tulis_file()
        elif pilihan == "2":
            baca_file()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()