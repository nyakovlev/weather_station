export VERSION=`cat ./VERSION`

# TODO: build dist/ for UI and copy it to local directory

docker build . -t weather_station:$VERSION
