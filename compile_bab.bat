@echo off
setlocal enabledelayedexpansion

set "ROOT_DIR=%~dp0"
set "OUTPUT_DIR=%ROOT_DIR%output"
set "SOURCE_DIR=%ROOT_DIR%modul_praktikum_python"

if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

echo ============================================================
echo Compiling Individual Modules (modul_praktikum_python\modul)
echo ============================================================

pushd "%SOURCE_DIR%\modul"

for %%F in (modul-*.tex) do (
    set "FILE_NAME=%%~nF"
    echo.
    echo ------------------------------------------------------------
    echo Compiling !FILE_NAME!...
    echo ------------------------------------------------------------

    pdflatex -interaction=nonstopmode -halt-on-error "%%F"
    if !errorlevel! equ 0 (
        rem Tidak ada bibliografi di modul ini; dua lari pdflatex untuk stabilkan referensi silang/TOC subfiles
        pdflatex -interaction=nonstopmode -halt-on-error "%%F"

        if exist "!FILE_NAME!.pdf" (
            echo Moving !FILE_NAME!.pdf to output...
            move /y "!FILE_NAME!.pdf" "%OUTPUT_DIR%\!FILE_NAME!.pdf"
        )
        if exist "!FILE_NAME!.log" (
            echo Moving !FILE_NAME!.log to output...
            move /y "!FILE_NAME!.log" "%OUTPUT_DIR%\!FILE_NAME!.log"
        )
    ) else (
        echo ERROR compiling !FILE_NAME!.
    )
)

popd

echo Cleaning up intermediate files...
call :cleanup "%SOURCE_DIR%"

echo.
echo Operation Completed. Check the output folder for PDF and .log files.
goto :end

:cleanup
set "TARGET_FOLDER=%~1"
pushd "%TARGET_FOLDER%"
for %%E in (aux bbl blg bcf out toc lof lot fls fdb_latexmk nav snm vrb idx ilg ind acn acr alg glg glo gls ist xdy run.xml synctex pdfsync synctex.gz) do (
    del /s /q "*.%%E" 2>nul
)
popd
exit /b 0

:end
echo.
pause
exit /b 0
