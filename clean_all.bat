@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ============================================================
echo Menghapus file sampingan hasil kompilasi LaTeX
echo di seluruh proyek (semua subfolder, kecuali .git)...
echo ============================================================

rem Hapus rekursif tanpa menyentuh .git (hindari *.idx pack Git, dll.)
call :del_ext aux
call :del_ext log
call :del_ext out
call :del_ext toc
call :del_ext lof
call :del_ext lot
call :del_ext fls
call :del_ext fdb_latexmk
call :del_ext synctex.gz
call :del_ext xdv

call :del_ext bbl
call :del_ext blg
call :del_ext bcf
call :del_ext run.xml

call :del_ext lol

rem Indeks/glosarium LaTeX (aman: folder .git dikecualikan, jadi bukan pack index Git)
call :del_ext idx
call :del_ext ind
call :del_ext ilg
call :del_ext glo
call :del_ext gls
call :del_ext glg
call :del_ext acn
call :del_ext acr
call :del_ext alg
call :del_ext ist

call :del_ext nav
call :del_ext snm
call :del_ext vrb

rem Keluaran utama (nonaktifkan panggilan :del_ext pdf jika PDF harus dipertahankan)
call :del_ext pdf

echo.
echo Pembersihan selesai!
pause
goto :eof

:del_ext
set "PAT=%~1"
for /f "delims=" %%F in ('dir /a-d /s /b "*.%PAT%" 2^>nul ^| findstr /v /i "\\.git\\"') do (
  if exist "%%F" del /q "%%F"
)
exit /b
