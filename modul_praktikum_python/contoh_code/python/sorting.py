"""
Contoh Sorting: Bubble Sort (Python)

Tujuan contoh ini:
- Menunjukkan cara kerja algoritma Bubble Sort secara bertahap.
- Menampilkan kondisi list ke layar pada SETIAP iterasi (setiap langkah perbandingan).

Gambaran singkat Bubble Sort:
- Bubble Sort melakukan perbandingan elemen yang bersebelahan (A[j] dan A[j+1]).
- Jika urutannya salah (A[j] > A[j+1] untuk ascending), keduanya ditukar (swap).
- Setelah 1 putaran/passes (dari kiri ke kanan), elemen terbesar akan “mengapung”
  ke posisi paling kanan dari bagian yang belum terurut.

Kompleksitas:
- Waktu:
  - Terburuk: O(n^2)
  - Rata-rata: O(n^2)
  - Terbaik (jika sudah terurut dan memakai early stop): O(n)
- Ruang: O(1) (in-place)
"""

from __future__ import annotations

from typing import List, Tuple


def bubble_sort_verbose(data: List[int]) -> Tuple[List[int], int]:
    """
    Mengurutkan list `data` secara ascending menggunakan Bubble Sort,
    sambil mencetak prosesnya pada setiap iterasi.

    Kenapa fungsi mengembalikan tuple (hasil, jumlah_perbandingan)?
    - `hasil`: list yang sudah terurut (karena in-place, ini list yang sama).
    - `jumlah_perbandingan`: jumlah langkah perbandingan yang dilakukan.

    Parameter:
    - data: list of int yang akan diurutkan (akan dimodifikasi in-place).
    """

    n = len(data)
    perbandingan = 0

    print("=== Bubble Sort (Verbose) ===")
    print(f"Data awal         : {data}")
    print(f"Jumlah elemen (n) : {n}")
    print()

    # Outer loop = jumlah pass/putaran.
    #
    # Intuisi penting:
    # - Setelah pass ke-i selesai, elemen terbesar dari bagian yang belum terurut
    #   akan berada di ujung kanan (posisi n-1-i).
    # - Karena itu, pada pass berikutnya kita tidak perlu membandingkan sampai ujung kanan lagi.
    for i in range(n - 1):
        print(f"--- Pass {i + 1} ---")

        # Flag untuk mendeteksi apakah ada pertukaran pada pass ini.
        # Jika tidak ada swap sama sekali, artinya list sudah terurut -> stop lebih awal.
        ada_swap = False

        # Inner loop membandingkan pasangan bersebelahan.
        # Batasnya `n - 1 - i` karena elemen terakhir sebanyak `i` buah sudah final posisinya.
        for j in range(0, n - 1 - i):
            perbandingan += 1

            kiri = data[j]
            kanan = data[j + 1]

            # Cetak setiap iterasi perbandingan.
            print(f"Iterasi pass={i + 1}, j={j}: bandingkan {kiri} dan {kanan} -> ", end="")

            # Aturan ascending:
            # - Jika kiri lebih besar dari kanan, urutan salah -> swap.
            if kiri > kanan:
                data[j], data[j + 1] = data[j + 1], data[j]
                ada_swap = True
                print("SWAP")
            else:
                print("TIDAK swap")

            # Kondisi list setelah langkah ini (ditampilkan setiap iterasi).
            print(f"  kondisi list: {data}")

        print(f"Hasil setelah pass {i + 1}: {data}")
        print()

        if not ada_swap:
            print("Tidak ada pertukaran pada pass ini -> list sudah terurut, berhenti lebih awal.")
            print()
            break

    print(f"Data akhir (urut) : {data}")
    print(f"Total perbandingan: {perbandingan}")
    print("============================")
    return data, perbandingan


def main() -> None:
    """
    Titik masuk program.
    Silakan ganti `data` untuk mencoba kasus lain.
    """

    # Contoh data.
    data = [5, 1, 4, 2, 8]

    # Jalankan bubble sort dan tampilkan semua iterasi.
    bubble_sort_verbose(data)


if __name__ == "__main__":
    main()

