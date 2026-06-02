

def tulis_file():
    # semester = ?
    kode_mtk = input("Kode Mata Kuliah : ")
    # nm_mtk = ?
    # sks = ?
    n_tugas = int(input("Nilai Tugas   : "))
    n_quiz = int(input("Nilai Quiz     : "))
    n_UTS = int(input("Nilai UTS       : "))
    n_UAS = int(input("Nilai UAS       : "))
    
    # n_akhir = ?
    # hm = ?

    with open("data_nilai.csv","a") as file:
           file.write(f"{nim},{str(nilai)}\n")

def baca_file():

    with open("data_nilai.csv","r") as file:
         for baris in file:
             baris = baris.strip().split(",")
             print(f"NIM : {baris[0]}  Nilai: {baris[1]}")

def main() -> None:
    tulis_file()
    baca_file()
            

if __name__ == "__main__":
    main()  