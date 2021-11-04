#!/usr/bin/python3

import argparse
from threading import Thread
from subprocess import Popen
import os
import sys
import signal

import station_link
from websocket_server import WebsocketServer


DEFAULT_WEBDIR_FILE = "default_webdir"
DEFAULT_WEBDIR = os.path.join(os.getcwd(), DEFAULT_WEBDIR_FILE)


def get_nginx_conf(host_dir, port):
    return f"""
http {{
        server {{
        listen {port};
        location / {{
            root {host_dir};
        }}
    }}
}}
"""


def main():
    parser = argparse.ArgumentParser(
        "weather_station.py",
        description="Runs a webpage and manages interaction with a weather station"
    )

    parser.add_argument("--station-address", help="Weather station's IP address", required=True)
    parser.add_argument("--station-port", help="TCP port that weather station is listening on (default: 2149)", default=2149)

    parser.add_argument("--ws-port", help="Websocket server port (default: 2148)", default=2148)

    parser.add_argument("--no-web", help="Do not serve a webpage", action="store_true")
    parser.add_argument("--web-port", help="TCP port to serve webpage (default: 8080)", default=8080)
    default_web_path = os.path.join(os.getcwd(), "build")
    parser.add_argument("--web-path", help=f"Path to web hosting directory (default: ./{DEFAULT_WEBDIR_FILE})", default=default_web_path)

    args=parser.parse_args()
    
    print("Starting ")
    wss = WebsocketServer(args.ws_port)
    wss.start()

    print("Running backend link to weather station...")
    Thread(
        target=station_link.run,
        args=(
            args.station_address,
            args.station_port,
            wss.propagate
        )
    ).start()

    p = None
    if not args.no_web:
        web_path = args.web_path
        print(f"Hosting web directory {web_path} on port {args.web_port}...")
        if not os.path.exists(web_path):
            web_path = DEFAULT_WEBDIR
            print(f"Path does not exist; falling back to {web_path}")
        with open("nginx.conf", "w") as f:
            f.write(get_nginx_conf(web_path, args.web_port))
        p = Popen(["nginx", "-c", os.path.join(os.getcwd(), "nginx.conf")])
    
    def stop(*args):
        if p is not None:
            p.kill()
        sys.exit()
    
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)


if __name__ == "__main__":
    main()
