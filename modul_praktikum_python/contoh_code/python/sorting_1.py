"""
Contoh Sorting (Selection Sort) - versi verbose (menampilkan setiap iterasi).

Intuisi Selection Sort:
- Di setiap "pass" i, kita memilih (select) elemen terkecil dari bagian yang belum rapi
  (mulai indeks i sampai akhir), lalu menukarnya ke posisi i.
- Setelah pass i selesai, bagian kiri (0..i) sudah terurut benar.

Kompleksitas:
- Waktu: O(n^2) karena selalu melakukan pencarian minimum untuk tiap posisi i.
- Memori: O(1) (in-place), karena hanya melakukan pertukaran elemen di list yang sama.
"""

from __future__ import annotations


def selection_sort_verbose(data: list[int]) -> list[int]:
    """
    Mengurutkan list angka dengan algoritma Selection Sort, sambil mencetak
    prosesnya pada setiap iterasi.

    Parameter:
    - data: list[int]
      List yang akan diurutkan. Fungsi ini mengurutkan *in-place* (list asli ikut berubah).

    Return:
    - list[int]
      Mengembalikan referensi list yang sama (yang sudah terurut).
    """

    n = len(data)

    print("=== SELECTION SORT (VERBOSE) ===")
    print(f"Data awal : {data}")
    print()

    # Outer loop: menentukan posisi i yang akan "diisi" oleh elemen minimum
    # dari subarray data[i..n-1].
    for i in range(n - 1):
        # Asumsi awal: elemen minimum berada di posisi i.
        min_index = i

        # Inner loop: cari indeks elemen minimum di bagian yang belum terurut.
        # Bagian yang belum terurut dimulai dari i+1 hingga n-1.
        for j in range(i + 1, n):
            # Jika menemukan nilai yang lebih kecil, perbarui min_index.
            if data[j] < data[min_index]:
                min_index = j

        # Pada titik ini, min_index adalah posisi elemen terkecil untuk pass i.
        print(f"Pass {i + 1}/{n - 1}")
        print(f"- Posisi yang akan diisi (i)   : {i}")
        print(f"- Nilai kandidat di posisi i  : {data[i]}")
        print(f"- Indeks minimum ditemukan    : {min_index}")
        print(f"- Nilai minimum ditemukan     : {data[min_index]}")

        # Jika min_index != i, kita perlu swap agar elemen minimum pindah ke posisi i.
        # Jika min_index == i, berarti posisi i sudah berisi elemen minimum, jadi swap tidak perlu.
        if min_index != i:
            print(f"- Swap: data[{i}] <-> data[{min_index}] ({data[i]} <-> {data[min_index]})")
            data[i], data[min_index] = data[min_index], data[i]
        else:
            print("- Swap: tidak diperlukan (posisi i sudah minimum)")

        # Cetak kondisi list setelah pass i selesai.
        # Bagian kiri (0..i) sudah "fixed" (benar dan tidak akan berubah lagi).
        kiri_terurut = data[: i + 1]
        sisa = data[i + 1 :]
        print(f"- Setelah pass: {data}")
        print(f"  Bagian sudah terurut : {kiri_terurut}")
        print(f"  Bagian belum terurut : {sisa}")
        print()

    print(f"Data akhir: {data}")
    return data


def main() -> None:
    # Contoh data (bisa kamu ganti).
    contoh = [64, 25, 12, 22, 11]

    # Panggil selection sort verbose.
    # Catatan: list `contoh` akan berubah karena sorting dilakukan in-place.
    selection_sort_verbose(contoh)


if __name__ == "__main__":
    main()

