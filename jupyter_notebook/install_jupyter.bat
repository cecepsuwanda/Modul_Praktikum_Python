@echo off
echo ========================================================
echo Pemasangan Environment Jupyter Notebook Lokal
echo ========================================================
echo.

echo [1/4] Membuat Virtual Environment (venv)...
python -m venv venv

echo [2/4] Mengaktifkan Virtual Environment...
call venv\Scripts\activate.bat

echo [3/4] Melakukan upgrade PIP...
python -m pip install --upgrade pip

echo [4/4] Menginstal modul Jupyter Notebook...
pip install notebook

echo.
echo ========================================================
echo INSTALASI SELESAI!
echo Jupyter Notebook telah terinstal di dalam folder ini.
echo.
echo Untuk menjalankan Jupyter Notebook, cukup eksekusi file:
echo "jalankan_jupyter.bat"
echo ========================================================
pause
