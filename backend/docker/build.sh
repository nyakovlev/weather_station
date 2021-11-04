START_DIR=$(dirname $0)
cd $START_DIR

VERSION=`cat ../VERSION`

cd ../../ui
npm run build
cp -R ./build ../backend
cd ../backend

docker build . --file docker/Dockerfile -t weather_station:$VERSION
