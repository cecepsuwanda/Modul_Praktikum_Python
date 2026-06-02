def tulis_file():
    nama = input("Nama : ")
    umur = input("Umur : ")

    with open("data.txt", "a") as file:
        file.write(f"{nama},{umur}\n")

    print("Data berhasil disimpan")


def baca_file():
    print("\n=== DATA TERSIMPAN ===")

    try:
        with open("data.txt", "r") as file:
            for baris in file:
                data = baris.strip().split(",")
                print(f"Nama: {data[0]} | Umur: {data[1]}")
    except FileNotFoundError:
        print("File belum tersedia")


def main():
    while True:
        print("\n=== MENU ===")
        print("1. Simpan Data")
        print("2. Tampilkan Data")
        print("3. Keluar")

        pilihan = input("Pilih menu: ")

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