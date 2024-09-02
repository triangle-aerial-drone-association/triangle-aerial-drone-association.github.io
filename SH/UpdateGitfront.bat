@echo off

SET SCRIPT_DIR=%~dp0
SET SCRIPT_DIR=%SCRIPT_DIR:~0,-1%
SET REPO_PATH=%SCRIPT_DIR%\..
SET DOWNLOAD_URL=https://gitfront.io/r/TriangleAerialDroneAssociation/RAmknZkyp1n2/TADA-Guide-Scripts/
SET DOWNLOAD_PATH=%REPO_PATH%\download-temp

mkdir %DOWNLOAD_PATH%

cd %DOWNLOAD_PATH%
del /q %REPO_PATH%\*.txt

wget --recursive --level=5 --no-clobber --page-requisites --adjust-extension --span-hosts ^
     --convert-links --restrict-file-names=windows --domains gitfront.io --no-parent ^
     -np -nH --cut-dirs=4 -P . %DOWNLOAD_URL%

echo User-agent: * > robots.txt
echo Disallow: /TADAResources.html >> robots.txt

if exist index.html rename index.html TADAResources.html
if exist style.css rename style.css TADAResources.css

powershell -Command ^
    "(Get-ChildItem -Path %DOWNLOAD_PATH% -Filter *.html -Recurse | ForEach-Object {" ^
    "    ((Get-Content -Path $_.FullName -Raw) " ^
    "        -replace '</head>', '<link rel=\"shortcut icon\" type=\"image/x-icon\" href=\"images/favicon.ico\">\n</head>' " ^
    "        -replace '<div class=\"footer\">[\s\S]*?<\/div>', '' " ^
    "        -replace 'style.css', 'TADAResources.css' " ^
    "        -replace 'TADA-Guide-Scripts · GitFront', 'TADA Resources' " ^
    "        -replace 'TADA-Guide-Scripts', 'TADA Resources') " ^
    "    | Set-Content -Path $_.FullName })"

xcopy /s /e /y * %REPO_PATH%\

cd ..
rd /s /q %DOWNLOAD_PATH%

cd %REPO_PATH%
git add .
git commit -m "Updated GitFront Page on %date%"
@REM git push origin main
@REM git push remote origin main
