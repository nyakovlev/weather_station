## Weather station backend

It's assumed that you have python3 and venv installed.

On Ubuntu:
```
sudo apt-get install python3
sudo apt-get install python3-venv
```

To set up dependencies:
```
source ./setup.sh
```

To run backend:
```
python wstation_backend.py --web-port=80 --backend-port=2149
```

The weather station can also be run as a docker container. Details on building and running a docker container for the backend are available in `docker/`.
