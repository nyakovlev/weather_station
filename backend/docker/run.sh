START_DIR=$(dirname $0)
cd $START_DIR

VERSION=`cat ../VERSION`
docker run -it --rm --net host weather_station:$VERSION $@
