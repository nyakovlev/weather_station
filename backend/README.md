## Weather station backend

It's assumed that you have python3 and venv installed.

On Ubuntu:
```
sudo apt-get install python3
sudo apt-get install python3-venv
```

To set up environment:
```
source ./setup.sh
```

To run backend:
```
python weather_station.py --station-address="<IP OF YOUR WEATHER STATION>"
```

You should then be able to access your webpage at [http://localhost:8080](http://localhost:8080)

The weather station can also be run as a docker container. Details on building and running a docker container for the backend are available in `docker/`.

Here's the complete set of options available from `weather_station.py`:
```
$ ./weather_station.py --help
usage: weather_station.py [-h] --station-address STATION_ADDRESS [--station-port STATION_PORT] [--ws-port WS_PORT] [--no-web]
                          [--web-port WEB_PORT] [--web-path WEB_PATH]

Runs a webpage and manages interaction with a weather station

optional arguments:
  -h, --help            show this help message and exit
  --station-address STATION_ADDRESS
                        Weather station's IP address
  --station-port STATION_PORT
                        TCP port that weather station is listening on (default: 2149)
  --ws-port WS_PORT     Websocket server port (default: 2148)
  --no-web              Do not serve a webpage
  --web-port WEB_PORT   TCP port to serve webpage (default: 8080)
  --web-path WEB_PATH   Path to web hosting directory (default: ./default_webdir)
```
