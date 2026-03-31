@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion
cd /d "%~dp0"

rem Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [Error] Python not found. Install Python 3.8+
    pause
    exit /b 1
)

rem Check dependencies
python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Installing requests...
    python -m pip install requests --quiet
)

rem Check script
if not exist "%~dp0generate_product_seo.py" (
    echo [Error] generate_product_seo.py not found.
    pause
    exit /b 1
)

rem Check if API is configured
set "API_CONFIGURED=0"
if exist "%~dp0.seo_config.json" (
    findstr /i "api_key" "%~dp0.seo_config.json" >nul 2>&1
    if not errorlevel 1 set "API_CONFIGURED=1"
)

:STEP1_API
echo.
echo ================================================
echo   Step 1: API Configuration
echo ================================================
echo.
if "!API_CONFIGURED!"=="1" (
    echo API Key already configured.
    set /p "CHANGE_API=Change API Key? (y/N): "
    if /I "!CHANGE_API!"=="y" (
        python "%~dp0generate_product_seo.py" --config
        if errorlevel 1 goto :END
    )
) else (
    echo API Key not configured yet.
    set /p "SET_API=Configure API Key now? (Y/n): "
    if /I "!SET_API!"=="n" goto :STEP1_API
    python "%~dp0generate_product_seo.py" --config
    if errorlevel 1 goto :END
)

:STEP2_FOLDER
echo.
echo ================================================
echo   Step 2: Select Category
echo ================================================
echo.
echo   A - Process ALL categories
echo   1 - Japanese-Knives
echo   2 - Chinese-Knives
echo   3 - Western-Knives
echo   4 - Cookware
echo   5 - Axes-Outdoor
echo   6 - Accessories
echo   7 - Pocket-Knives
echo   N - Enter custom folder name
echo.
set /p "FOLDER_CHOICE=Your choice: "

if /I "!FOLDER_CHOICE!"=="A" (
    set "MODE=--all"
    goto :STEP3_COLS
)
if /I "!FOLDER_CHOICE!"=="N" (
    set /p "CUSTOM_FOLDER=Enter folder name: "
    if "!CUSTOM_FOLDER!"=="" goto :STEP2_FOLDER
    set "MODE=--single !CUSTOM_FOLDER!"
    goto :STEP3_COLS
)
if "!FOLDER_CHOICE!"=="1" set "MODE=--single 1" & goto :STEP3_COLS
if "!FOLDER_CHOICE!"=="2" set "MODE=--single 2" & goto :STEP3_COLS
if "!FOLDER_CHOICE!"=="3" set "MODE=--single 3" & goto :STEP3_COLS
if "!FOLDER_CHOICE!"=="4" set "MODE=--single 4" & goto :STEP3_COLS
if "!FOLDER_CHOICE!"=="5" set "MODE=--single 5" & goto :STEP3_COLS
if "!FOLDER_CHOICE!"=="6" set "MODE=--single 6" & goto :STEP3_COLS
if "!FOLDER_CHOICE!"=="7" set "MODE=--single 7" & goto :STEP3_COLS

echo Invalid choice.
goto :STEP2_FOLDER

:STEP3_COLS
echo.
echo ================================================
echo   Step 3: Select Columns
echo ================================================
echo.
echo   1 - Short description
echo   2 - Long description
echo   3 - SEO Title
echo   4 - Meta Description
echo   5 - Focus Keyword
echo.
echo   L - Light mode (3,4,5 - saves tokens)
echo   A - All columns
echo   C - Custom selection (space separated)
echo.
set /p "COL_CHOICE=Your choice: "

if /I "!COL_CHOICE!"=="L" (
    set "COLS=--cols focus_kw seo_title meta_desc"
    goto :RUN_SCRIPT
)
if /I "!COL_CHOICE!"=="A" (
    set "COLS="
    goto :RUN_SCRIPT
)
if /I "!COL_CHOICE!"=="C" (
    set /p "CUSTOM_COLS=Enter column numbers (e.g., 3 4 5): "
    set "COL_KEYS="
    for %%i in (!CUSTOM_COLS!) do (
        if "%%i"=="1" set "COL_KEYS=!COL_KEYS! short_desc"
        if "%%i"=="2" set "COL_KEYS=!COL_KEYS! description"
        if "%%i"=="3" set "COL_KEYS=!COL_KEYS! seo_title"
        if "%%i"=="4" set "COL_KEYS=!COL_KEYS! meta_desc"
        if "%%i"=="5" set "COL_KEYS=!COL_KEYS! focus_kw"
    )
    if "!COL_KEYS!"=="" goto :STEP3_COLS
    set "COLS=--cols!COL_KEYS!"
    goto :RUN_SCRIPT
)

rem Handle single number input
set "COL_KEYS="
if "!COL_CHOICE!"=="1" set "COLS=--cols short_desc" & goto :RUN_SCRIPT
if "!COL_CHOICE!"=="2" set "COLS=--cols description" & goto :RUN_SCRIPT
if "!COL_CHOICE!"=="3" set "COLS=--cols seo_title" & goto :RUN_SCRIPT
if "!COL_CHOICE!"=="4" set "COLS=--cols meta_desc" & goto :RUN_SCRIPT
if "!COL_CHOICE!"=="5" set "COLS=--cols focus_kw" & goto :RUN_SCRIPT

echo Invalid choice.
goto :STEP3_COLS

:RUN_SCRIPT
echo.
echo ================================================
echo   Running...
echo ================================================
echo.
python "%~dp0generate_product_seo.py" !MODE! !COLS!

echo.
if errorlevel 1 (
    echo [Error] Script failed with code %errorlevel%
) else (
    echo [Done]
)

:END
echo.
set /p "RESTART=Run again? (y/N): "
if /I "!RESTART!"=="y" goto :STEP1_API
pause
endlocal
