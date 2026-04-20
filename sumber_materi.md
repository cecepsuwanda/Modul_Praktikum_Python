# Sumber materi: Python dari dasar hingga lanjutan

Dokumen ini merangkum **alur pembelajaran Python** (dasar → menengah → lanjutan) beserta **tautan sumber terbuka** yang relevan. Bagian tautan di bawah mempertahankan sumber yang sudah ada (RPS kampus, modul praktikum, tutorial) dan menambahkan referensi resmi serta komunitas untuk topik menengah–lanjutan.

---

## 1. Alur kurikulum (topik per tingkat)

### A. Dasar (fundamental)

Tujuan: bisa menulis program kecil, memahami sintaks, kontrol alur, fungsi, dan debugging sederhana.

| Topik | Ringkasan | Sumber utama (lihat bagian tautan) |
|--------|-----------|-------------------------------------|
| Instalasi & alat | Interpreter Python 3, editor/IDE, Jupyter Notebook/Lab | Modul UIMA (#6), GitHub praktikum (#4), Python Tutorial bab 2 |
| Sintaks & tipe data | Variabel, operator, `str`/`int`/`float`/`bool`, input/output | Modul Pancasila (#5), UM (#7), W3Schools (#16), Programiz (#17) |
| Struktur kontrol | `if`/`elif`/`else`, `for`/`while`, `break`/`continue` | Modul #5–#7, Tutorial bab 4 |
| Fungsi | Definisi, argumen, ruang lingkup lokal/global | Tutorial bab 4.9, Think Python (#13) |
| Berpikir algoritmik | Pseudocode, tracing, latihan soal | OCW UNS (#3), RPS pemrograman dasar (#1–#2), Think Python |

### B. Menengah (struktur data, modul, berkas, OOP)

Tujuan: program terstruktur, pakai pustaka standar, kelas, dan manajemen dependensi.

| Topik | Ringkasan | Sumber utama |
|--------|-----------|--------------|
| Struktur data | `list`, `tuple`, `dict`, `set`, comprehensions | Tutorial bab 5, PY4E (#11), Real Python (#19) |
| Modul & paket | `import`, paket, `if __name__ == "__main__"` | Tutorial bab 6 |
| Berkas & format | Membaca/menulis teks, `pathlib`, JSON | Tutorial bab 7, ATBS (#12) |
| Pengecualian | `try`/`except`/`finally`, membuat exception sendiri | Tutorial bab 8 |
| OOP | Kelas, `self`, pewarisan, method | Tutorial bab 9, Think Python |
| Pustaka standar & venv | Ikhtisar `stdlib`, virtual environment, `pip` | Tutorial bab 10–12, dokumentasi Library |
| Pengujian dasar | `unittest`, pola arrange–act–assert | Dokumentasi `unittest` (bagian sumber tambahan) |

### C. Lanjutan (produksi, konkurensi, tipe statis, arsitektur)

Tujuan: kode siap kolaborasi/ produksi: pengujian modern, paket, konkurensi, tipe, logging, performa.

| Topik | Ringkasan | Sumber utama |
|--------|-----------|--------------|
| Dekorator & generator | Fungsi tingkat tinggi, `yield`, iterator | HOWTO Functional, Language Reference |
| Context manager | `with`, protokol `__enter__`/`__exit__` | Tutorial / Library `contextlib` |
| Type hints & pemeriksa tipe | Anotasi, `typing`, `mypy` / PEPs | Dokumentasi `typing`, typing.readthedocs.org |
| `asyncio` | Coroutine, task, I/O asynchronous | Dokumentasi `asyncio` |
| Threading & multiproses | CPU-bound vs I/O-bound, `concurrent.futures` | Library `threading`, `multiprocessing` |
| Logging & konfigurasi | `logging`, konvensi level log | HOWTO Logging |
| Pengemasan proyek | `pyproject.toml`, rilis ke PyPI | Python Packaging User Guide |
| Referensi bahasa | Semantik formal, edge cases | The Python Language Reference |
| Ekstensi C / API | Modul native, embedding | Extending and Embedding, Python/C API |

### D. Arah khusus (opsional, sesuai minat / RPS sains data)

| Arah | Topik | Sumber contoh |
|------|--------|----------------|
| Ilmu/analisis data | `numpy`, `pandas`, visualisasi | dokumentasi NumPy & Pandas |
| Otomasi & skrip | CLI, spreadsheet, jadwal tugas | Automate the Boring Stuff (#12) |
| Web / API | HTTP, REST, framework ringan | dokumentasi FastAPI / Flask (sumber tambahan) |

---

## 2. Sumber terbuka: RPS, praktikum, dan konteks kurikulum

1. **RPS Pemrograman Dasar (UNESA, S1 Sains Data)** — PDF RPS resmi; CPMK mencakup penulisan program Python; bobot T=2, P=1 (ada komponen praktikum).  
   https://sindig.unesa.ac.id/rps-pdf/s1-sains-data/pemrograman-dasar.pdf

2. **RPS Pemrograman Dasar (UB, Departemen Statistika / Sains Data)** — PDF RPS; perangkat lunak yang disebut termasuk Python; ada alokasi penilaian praktikum.  
   https://statistika.ub.ac.id/wp-content/uploads/2024/01/RPS-Pemrograman-Dasar.pdf

3. **UNS Open CourseWare — Algoritme & Pemrograman Dasar dengan Python** — Halaman OCW publik dengan materi dan dokumen RPS untuk mata kuliah berbasis Python (MAT320308). URL memakai parameter `params` panjang dari situs OCW UNS.  
   https://ocw.uns.ac.id/site/detailmakul?params=14b317A4054yaVFVGVU16SXdNek6c23bcbb12f578660dbe4043d851963ceb72c9deE0Zkh4Tk1ERXg%3D

4. **Modul praktikum (GitHub): twseptian/pemrograman-python** — Repositori berisi modul praktikum Python (Jupyter) per pertemuan.  
   https://github.com/twseptian/pemrograman-python

---

## 3. Modul praktikum (dokumen terbuka)

5. **Modul praktikum Python (Universitas Pancasila, Lab Komputer)** — PDF panduan praktikum dasar (identifier, variabel, kondisi, perulangan, fungsi).  
   https://teknik.univpancasila.ac.id/labkom/praktikum/Modul%20Praktikum/Pyhton/modul%20praktikum%20python.pdf

6. **Modul pembelajaran pemrograman Python (UIMA, Silab)** — PDF modul instalasi, IDE, sintaks, tipe data, dan struktur kontrol.  
   https://silab.uima.ac.id/wp-content/uploads/2024/10/MODUL-PEMBELAJARAN-PEMROGRAMAN-PHYTON.pdf

7. **Modul pengenalan Python — praktikum (Universitas Negeri Malang, 2016)** — PDF Tim Asisten Praktikum Algoritma dan Pemrograman; teori, latihan, dan tugas praktikum.  
   https://elektro.um.ac.id/wp-content/uploads/2016/04/MODUL-4-PENGENALAN-PYTHON.pdf

---

## 4. Tutorial pemrograman Python 3 (sumber terbuka)

8. **The Python Tutorial (dokumentasi resmi, bahasa Inggris)** — Tutorial resmi Python 3 di docs.python.org.  
   https://docs.python.org/3/tutorial/index.html

9. **The Python Tutorial (dokumentasi resmi, bahasa Indonesia)** — Terjemahan resmi tutorial Python 3.  
   https://docs.python.org/id/3/tutorial/index.html

10. **Python Wiki — BeginnersGuide** — Indeks kurasi komunitas ke tutorial, buku, dan alat belajar untuk pemula.  
    https://wiki.python.org/moin/BeginnersGuide

11. **Python for Everybody (PY4E)** — Kursus/teks terbuka berbasis web (video + materi) untuk Python 3.  
    https://www.py4e.com/

12. **Automate the Boring Stuff with Python** — Buku online gratis (edisi Python 3) tentang otomasi praktis.  
    https://automatetheboringstuff.com/

13. **Think Python, 2e (Green Tea Press)** — Teks terbuka “How to Think Like a Computer Scientist” untuk Python 3.  
    https://greenteapress.com/wp/think-python-2e/

14. **Dive Into Python 3** — Buku/tutorial web gratis yang membahas Python 3 secara mendalam.  
    https://diveintopython3.net/

15. **Google’s Python Class** — Materi singkat Google Developers untuk Python 3 (catatan + latihan).  
    https://developers.google.com/edu/python

16. **W3Schools — Python Tutorial** — Referensi singkat sintaks dan contoh interaktif (Python 3).  
    https://www.w3schools.com/python/

17. **Programiz — Python Programming Tutorial** — Tutorial berchapter dengan contoh kode (disarankan Python 3.x).  
    https://www.programiz.com/python-programming

18. **LearnPython.org** — Tutorial interaktif di browser (dasar Python 3).  
    https://www.learnpython.org/

19. **Real Python** — Artikel tutorial gratis (instalasi, sintaks, struktur data, lanjutan) untuk Python 3.  
    https://realpython.com/

---

## 5. Sumber tambahan (menengah–lanjutan & referensi resmi)

20. **The Python Standard Library** — Indeks modul bawaan; acuan setelah tutorial.  
    https://docs.python.org/3/library/index.html

21. **The Python Language Reference** — Definisi formal bahasa (lanjutan).  
    https://docs.python.org/3/reference/index.html

22. **Functional Programming HOWTO** — Gaya fungsional, iterator, generator.  
    https://docs.python.org/3/howto/functional.html

23. **Logging HOWTO** — Pola logging aplikasi.  
    https://docs.python.org/3/howto/logging.html

24. **`unittest` — unit testing framework**  
    https://docs.python.org/3/library/unittest.html

25. **pytest — kerangka pengujian populer di komunitas**  
    https://docs.pytest.org/

26. **`typing` — anotasi tipe**  
    https://docs.python.org/3/library/typing.html

27. **Typing documentation (mypy docs — referensi praktis type system)**  
    https://typing.readthedocs.io/

28. **`asyncio` — I/O asynchronous**  
    https://docs.python.org/3/library/asyncio.html

29. **`concurrent.futures` — eksekutor thread & process pool**  
    https://docs.python.org/3/library/concurrent.futures.html

30. **`threading` / `multiprocessing`**  
    https://docs.python.org/3/library/threading.html  
    https://docs.python.org/3/library/multiprocessing.html

31. **Python Packaging User Guide** — venv, build, PyPI.  
    https://packaging.python.org/

32. **Extending and Embedding the Python Interpreter**  
    https://docs.python.org/3/extending/index.html

33. **Python/C API Reference Manual**  
    https://docs.python.org/3/c-api/index.html

34. **NumPy documentation** — array numerik (alur sains data).  
    https://numpy.org/doc/stable/

35. **pandas documentation** — tabel/dataframe.  
    https://pandas.pydata.org/docs/

36. **FastAPI** — API modern asynchronous (opsional, setelah `asyncio`/HTTP).  
    https://fastapi.tiangolo.com/

---

## 6. Saran urutan belajar (ringkas)

1. Baca **sintaks & kontrol alur** lewat modul kampus (#5–#7) atau Tutorial resmi (#8/#9), ditemani **latihan** (#4, #17, #18).  
2. Perdalam **struktur data & fungsi** dengan Think Python (#13) atau PY4E (#11).  
3. Latih **otomasi & berkas** dengan ATBS (#12) dan bab 7 Tutorial.  
4. Masuk **OOP, modul, venv** (Tutorial bab 6, 9, 12; Dive Into Python 3 #14).  
5. Untuk **produksi**: pengujian (#24–#25), logging (#23), kemasan (#31).  
6. **Lanjutan**: tipe statis (#26–#27), konkurensi (#28–#30), referensi bahasa (#21), ekstensi (#32–#33).  
7. Jika mengikuti **sains data**: tambahkan #34–#35.

Tautan dapat berubah sewaktu-waktu oleh penyedia; jika patah, gunakan mesin pencari dengan judul sumber atau arahkan ke **python.org** dan **docs.python.org/3/** sebagai jangkar utama.
