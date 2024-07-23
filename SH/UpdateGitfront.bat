@echo off

SET SCRIPT_DIR=%~dp0
SET SCRIPT_DIR=%SCRIPT_DIR:~0,-1%

SET REPO_PATH=%SCRIPT_DIR%\..
SET DOWNLOAD_URL=https://gitfront.io/r/TriangleAerialDroneAssociation/RAmknZkyp1n2/TADA-Guide-Scripts/
SET DOWNLOAD_PATH=%REPO_PATH%\download-temp

mkdir %DOWNLOAD_PATH%

cd %DOWNLOAD_PATH%
del /q %REPO_PATH%\*.txt

wget --recursive --level=5 --no-clobber --page-requisites --adjust-extension --span-hosts --convert-links --restrict-file-names=windows --domains gitfront.io --no-parent -np -nH --cut-dirs=4 -P . %DOWNLOAD_URL%

del robots.txt

if exist index.html rename index.html subsite.html

powershell -Command "((Get-Content -path %DOWNLOAD_PATH%\subsite.html -Raw) -replace '<div class=\"footer\">[\s\S]*?<\/div>', '') | Set-Content -Path %DOWNLOAD_PATH%\subsite.html"

xcopy /s /e /y * %REPO_PATH%\

cd ..
rd /s /q %DOWNLOAD_PATH%

cd %REPO_PATH%

git add .
git commit -m "Updated GitFront Page on %date%"
git push origin main
