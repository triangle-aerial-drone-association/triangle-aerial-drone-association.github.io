SCRIPT_DIR=$(dirname "$0")

REPO_PATH="$SCRIPT_DIR/.."
DOWNLOAD_URL="https://gitfront.io/r/TriangleAerialDroneAssociation/RAmknZkyp1n2/TADA-Guide-Scripts/"
DOWNLOAD_PATH="$REPO_PATH/download-temp"

mkdir -p "$DOWNLOAD_PATH"

cd "$DOWNLOAD_PATH" || exit
rm -f "$REPO_PATH"/*.txt

wget --recursive --level=5 --no-clobber --page-requisites --adjust-extension --span-hosts --convert-links --restrict-file-names=windows --domains=gitfront.io --no-parent -np -nH --cut-dirs=4 -P . "$DOWNLOAD_URL"

rm -f robots.txt

if [ -e index.html ]; then
    mv index.html TADAResources.html
fi

# Use sed to remove the footer section from HTML files
sed -i '' '/<div class="footer">/,/<\/div>/d' TADAResources.html

cp -R . "$REPO_PATH/"

cd ..
rm -rf "$DOWNLOAD_PATH"

cd "$REPO_PATH" || exit

git add .
git commit -m "Updated GitFront Page on $(date)"
git push origin main
