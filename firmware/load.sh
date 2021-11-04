PORT=$1

for FILE in *.py; do
    echo "Uploading ${FILE}..."
    ampy --port ${PORT} put ${FILE}
done
