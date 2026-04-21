"""
Contoh pencarian linier (linear search / sequential search) dalam Python.

Apa itu pencarian linier?
------------------------
Pencarian linier memeriksa setiap elemen daftar satu per satu, dari awal
hingga akhir (atau sampai elemen yang dicari ketemu). Cocok untuk daftar
kecil atau ketika data belum diurutkan. Kompleksitas waktu kasus terburuk
adalah O(n): jika tidak ada atau ada di posisi terakhir, kita bisa membandingkan
hingga n kali (n = panjang daftar).
"""


def linear_search(items: list[int], target: int) -> int:
    """
    Mencari indeks pertama di mana `target` muncul di dalam `items`.

    Algoritma:
    1. Mulai dari indeks 0.
    2. Bandingkan elemen saat ini dengan `target`.
       - Jika sama, kembalikan indeks tersebut (pencarian selesai).
       - Jika tidak, lanjut ke elemen berikutnya.
    3. Jika sampai akhir daftar tidak ketemu, kembalikan -1.

    Args:
        items: Daftar bilangan bulat yang akan dicari.
        target: Nilai yang ingin ditemukan.

    Returns:
        Indeks (0-based) jika `target` ditemukan, atau -1 jika tidak ada.
    """
    # range(len(items)) menghasilkan 0, 1, 2, ..., len(items)-1
    for index in range(len(items)):
        # Bandingkan elemen di posisi `index` dengan nilai yang dicari
        if items[index] == target:
            # Ketemu di posisi pertama yang cocok — langsung kembalikan
            return index

    # Loop selesai tanpa return di dalam if artinya tidak ada yang cocok
    return -1


def main() -> None:
    """
    Demo interaktif: pengguna memasukkan beberapa angka, lalu angka yang dicari.
    """
    # Contoh data tetap untuk praktikum; bisa diganti dengan input pengguna
    print("--- Demo pencarian linier ---")
    print("Data contoh: bilangan dalam daftar [5, 12, 8, 1, 9, 3]")

    data = [5, 12, 8, 1, 9, 3]

    # input() mengembalikan string; int() mengubahnya menjadi bilangan bulat
    target = int(input("Masukkan angka yang ingin dicari: "))

    posisi = linear_search(data, target)

    if posisi != -1:
        # Indeks dimulai dari 0; untuk pembaca manusia kadang dipakai "urutan ke-n"
        print(f"Ditemukan di indeks {posisi} (elemen ke-{posisi + 1} dari kiri).")
    else:
        print("Tidak ditemukan dalam daftar.")


if __name__ == "__main__":
    main()
