@echo off
echo Memeriksa instalasi Virtual Environment...

if not exist "venv\Scripts\activate.bat" (
    echo Error: Virtual Environment belum terinstal!
    echo Silakan jalankan file "install_jupyter.bat" terlebih dahulu.
    pause
    exit /b
)

echo Mengaktifkan environment dan memulai Jupyter Notebook...
call venv\Scripts\activate.bat
jupyter notebook
